---
id: 710
title: Using Scala with JDBC to connect to MySQL
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=710
permalink: /2011/05/27/using-scala-with-jdbc-to-connect-to-mysql/
categories:
  - solutions log
tags:
  - jdbc
  - mysql
  - scala
---
A howto on connecting Scala to a MySQL database using JDBC. There are a number of database libraries for Scala, but I ran into a problem getting most of them to work. I attempted to use scala.dbc, scala.dbc2, Scala Query and Querulous but either they aren&rsquo;t supported, have a very limited featured set or abstracts SQL to a weird pseudo language.

The Play Framework has a new database library called [ANorm][1] which tries to keep the interface to basic SQL but with a slight improved scala interface. The jury is still out for me, only used on one project minimally so far. Also, I&rsquo;ve only seen it work within a Play app, does not look like it can be extracted out too easily.

So I ended up going with basic Java JDBC connection and it turns out to be a fairly easy solution.

Here is the code for accessing a database using Scala and JDBC. You need to change the connection string parameters and modify the query for your database. This example was geared towards MySQL, but any Java JDBC driver should work the same with Scala.

### Basic Query

<pre><code class="scala">  import java.sql.{Connection, DriverManager, ResultSet};

  // Change to Your Database Config
  val conn_str = "jdbc:mysql://localhost:3306/DBNAME?user=DBUSER&password=DBPWD"

  // Load the driver
  classOf[com.mysql.jdbc.Driver]

  // Setup the connection
  val conn = DriverManager.getConnection(conn_str)
  try {
      // Configure to be Read Only
      val statement = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY)

      // Execute Query
      val rs = statement.executeQuery("SELECT quote FROM quotes LIMIT 5")

      // Iterate Over ResultSet
      while (rs.next) {
          println(rs.getString("quote"))
      }
  }
  finally {
      conn.close
  }
</code></pre>

You will need to download the mysql-connector jar. [Download the mysql connector jar from here.][2]

Or if you are using maven, the pom snippets to load the mysql connector, you&rsquo;ll need to check what the latest version is.

<pre><code class="xml">  &lt;dependency&gt;
    &lt;groupId&gt;mysql&lt;/groupId&gt;
    &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
    &lt;version&gt;5.1.12&lt;/version&gt;
  &lt;/dependency&gt;
</code></pre>

To run the example, save the following to a file (query_test.scala) and run using, the following specifying the classpath to the connector jar:

`scala -cp mysql-connector-java-5.1.12.jar:. query_test.scala `

### Insert, Update and Delete

To perform an insert, update or delete you need to create an updatable statement object. The execute command is slightly different and you will most likely want to use some sort of parameters. Here&rsquo;s an example doing an insert using jdbc and scala with parameters.

<pre><code class="scala">  // create database connection
  val dbc = "jdbc:mysql://localhost:3306/DBNAME?user=DBUSER&password=DBPWD"
  classOf[com.mysql.jdbc.Driver]
  val conn = DriverManager.getConnection(dbc)
  val statement = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_UPDATABLE)

  // do database insert
  try {
    val prep = conn.prepareStatement("INSERT INTO quotes (quote, author) VALUES (?, ?) ")
    prep.setString(1, "Nothing great was ever achieved without enthusiasm.")
    prep.setString(2, "Ralph Waldo Emerson")
    prep.executeUpdate
  }
  finally {
    conn.close
  }
</code></pre>

 [1]: http://scala.playframework.org/documentation/scala-0.9/anorm
 [2]: http://dev.mysql.com/downloads/connector/j/