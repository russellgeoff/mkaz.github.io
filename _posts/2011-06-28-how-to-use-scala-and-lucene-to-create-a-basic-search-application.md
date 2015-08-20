---
id: 718
title: How to use Scala and Lucene to create a basic search application
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=718
permalink: /2011/06/28/how-to-use-scala-and-lucene-to-create-a-basic-search-application/
categories:
  - scala
---
How to use Scala and Lucene to create a basic search application. One of the powerful benefits of Scala is that it has full access to any Java libraries; giving you a tremendous number of available resources and technology. This example doesn&rsquo;t tap into the full power of Lucene, but highlights how easy it is to incorporate Java libraries into a Scala project.

This example is based off a Twitter analysis app I&rsquo;ve been noodling on; which I am utilizing Lucene. The code below takes a list of tweets from a text file; creates an index that you can search and extract info from.

All code and working demo app available here: <https://github.com/mkaz/Scala-and-Lucene>

### Create the Index

For this example, the data are simply lines in a file; each line is a tweet to be indexed.  
The indexer loops through the file creates a Lucene document from each line and adds it to the index.

<pre><code class="scala">  val analyzer = new StandardAnalyzer(Version.LUCENE_CURRENT)
  val directory = new NIOFSDirectory(new java.io.File("tmp/lucene"))
  val writer = new IndexWriter(directory, analyzer, IndexWriter.MaxFieldLength.UNLIMITED)

  val fileLines = io.Source.fromFile("data/tweets.txt").getLines.toList
  fileLines foreach { line =&gt;
      writer.addDocument(simpleDoc(line))
  }

  /** Simple Lucene Document */
  private def simpleDoc(text: String) = {
    val doc = new Document()
    doc.add(new Field("tweet", text, Field.Store.YES, Field.Index.ANALYZED, Field.TermVector.YES))
    doc
  }
</code></pre>

### Retrieve Popular Terms from Index

This example extracts the terms from the index and sorts them based on frequency count. You could use this to see what&rsquo;s popular or common trends.

<pre><code class="scala">  val allTerms = collection.mutable.HashMap[String, Int]()

  val reader = IndexReader.open(directory, true)

  // create map of popular terms
  val terms = reader.terms
  while (terms.next) {
    allTerms += terms.term.toString -&gt; terms.docFreq()
  }

  // sort map
  allTerms.toList sortBy { _._2 } foreach {
    case (key, value) =&gt;
      println(key + ": " + value)
  }
</code></pre>

### Search Index

An example of a basic search using Lucene&rsquo;s term query.

<pre><code class="scala">  val searcher = new IndexSearcher(directory, true)
  val query = new TermQuery(new Term("tweet", q))

  // perform search, return top 10
  val docs = searcher.search(query, 10)
  docs.scoreDocs foreach { docId =&gt;
    val d = searcher.doc(docId.doc)
    println(d.get("tweet"))
    println
  }
</code></pre>

This was just an introduction to using Lucene and Scala, showing the ease of leveraging existing Java libraries. Lucene is a very powerful tool and provides numerous ways to store and query data; a more complex search app would utilize these features more in depth. Here&rsquo;s an example using [Lucene to perform Spatial Distance Searches][1] and another example using [Lucene to create Summarizations][2]

To learn more about Lucene, you should check out [Lucene in Action][3] or other books available on the subject.

I hope you found it useful.

 [1]: http://blog.fakod.eu/2010/11/02/spatial-lucene-example-in-scala/
 [2]: http://sujitpal.blogspot.com/2009/02/summarization-with-lucene.html
 [3]: http://www.amazon.com/gp/product/1933988177/ref=as_li_ss_tl?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=217145&creative=399369&creativeASIN=1933988177
