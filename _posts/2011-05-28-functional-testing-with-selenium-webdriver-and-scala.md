---
id: 712
title: Functional Testing with Selenium WebDriver and Scala
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=712
permalink: /2011/05/28/functional-testing-with-selenium-webdriver-and-scala/
twitter_cards_summary_img_size:
  - 'a:7:{i:0;i:374;i:1;i:380;i:2;i:2;i:3;s:24:"width="374" height="380"";s:4:"bits";i:8;s:8:"channels";i:3;s:4:"mime";s:10:"image/jpeg";}'
categories:
  - solutions log
tags:
  - functional testing
  - scala
  - selenium
  - webdriver
---
Selenium&rsquo;s WebDriver tools can be used together with Scala, ScalaTest and sbt to create a great functional testing toolkit. This will give you the ability to test in various browsers, use a fast &ldquo;headless&rdquo; browser and even test iPhone and Android apps and web sites; though I haven&rsquo;t gotten to mobile testing yet.

<img src="https://mkaz.com/img/icon_quality.jpg" alt="100% Quality" title="100% Quality" border="0" width="177" height="180" align="right" /> [WebDriver][1] is a set of java libraries providing drivers which pass instructions to the browser allowing you to script control of a web page and verify results. These drivers start up your web browser on your computer and runs the tests; which you can watch as it goes. There are drivers for Firefox, IE, Safari, Chrome and as mentioned above iPhone and Android emulators. One of the great features of controlling a real browser is you can test real user interactions such as AJAX or other complex Javascript.

Additionally there is an HtmlUnitDriver which does not control a browser, but uses the HtmlUnit library to simulate a browser, allowing these tests to run much faster since you are not waiting for a browser to start and passing data back and forth.

The benefits I see using the WebDriver framework over regular Selenium tests is (1) faster tests running and (2) the ability to use a full set of programming paradigms around the tests. I find it easier to create scenarios and reusable tests by being able to create classes, extensions and normal programming logic. This is another benefit to using Scala with the [power and extensibility of Scala Traits][2].

So let&rsquo;s jump in to some examples and see what capabilities the tools have.

### Quick Start

  1. Install Scala: <http://www.scala-lang.org/>
  2. Install SBT: <http://code.google.com/p/simple-build-tool/>
  3. Check out my scaft test framework from github: git://github.com/mkaz/scaft.git
  4. Run tests

<div id="divider">
</div>

### How to Run Tests with SBT

Start sbt  
`$ sbt`

Run all tests  
`> test`

Run a single test  
`> test-only GoogleSearch`

<div id="divider">
</div>

### Developing Tests

Here&rsquo;s an example of a basic test, which will fetch the Google homepage and verify the title is correct.

<pre><code class="scala">  import org.scalatest.FlatSpec
  import org.openqa.selenium._
  import org.openqa.selenium.htmlunit._

  class GoogleSearch extends FlatSpec {

    val driver = new HtmlUnitDriver
    driver.get("http://www.google.com")

    // verify we retrieved the page and have the title
    "Google" should "have the proper title" in {
      assert(driver.getTitle() === "Google")
    }
  }
</code></pre>

To verify specific elements exist on the page, you can select them in various ways, by html tag, class, id, form name and even using by using XPath queries. You&rsquo;ll want to bookmark the [Web Driver API][3] for reference.

Here&rsquo;s an example using Google again, which will find the query input field by name, type in a query, submit and verify we received ten results and the term is in the the results set.

<pre><code class="scala">  class GoogleSearch extends FlatSpec {

    val driver = new HtmlUnitDriver
    driver.get("http://www.google.com")

    // verify we retrieved the page and have the title
    "Google" should "have the proper title" in {
      assert(driver.getTitle() === "Google")
    }

    it should "be able to perform a query" in {
      // do a search and confirm results

      // get form element
      val inputElement = driver.findElement(By.name("q"))

      // type in search query
      inputElement.sendKeys("vizsla puppies")

      // submit form - can be done from any form element
      // you dont need to locate the submit button
      inputElement.submit
    }

    // after a page submit, the driver object will be
    // on the next page, so now we can test results

    it should "have ten results" in {
      // find result set block
      val resultSet = driver.findElementById("rso")

      // count # of results
      val lis = resultSet.findElements(By.tagName("li"))
      assert(lis.size = 10)
    }

    it should "have term in result set" in {
      val firstResult = driver.findElement(By.xpath("//*[@id='rso']/li[1]/h3"))
      assert(firstResult.getText contains "vizsla puppies")
    }

  }
</code></pre>

* * *

### Using Firefox Driver for Ajax

Here&rsquo;s an ajax interactive example using Google Maps. The test will go to Google Maps, perform a search and verify the results, which are returned via ajax.

<pre><code class="scala">  /**
    * Test of Google Maps - Firefox Driver
    * verify map search and ajax result
    */
  class GoogleMaps extends FlatSpec {

    val driver = new FirefoxDriver
    driver.get("http://maps.google.com")

    // verify we retrieve the page and have the title
    "Google Maps" should "have the proper title" in {
      assert(driver.getTitle() === "Google Maps")
    }

    it should "be able to perform a query" in {

      // get form element
      val inputElement = driver.findElement(By.name("q"))

      // type in search query
      inputElement.sendKeys("San Francisco")

      // submit form
      inputElement.submit
    }

    // find span with place title
    it should "have the proper location title" in {
      val titleElement = driver.findElement(By.xpath("//span[@class='pp-place-title']/span"))
      assert(titleElement.getText == "San Francisco, CA")
    }

  }
</code></pre>

### Additional Resources

  * [ScalaTest][4] &#8211; The tests are written using ScalaTest, which supports several different ways to create tests.
  * [Watir][5], a similar functional test tool using Ruby
  * [Geb][6], another similar functinoal test tool using Groovy

 [1]: http://code.google.com/p/selenium/
 [2]: http://www.ibm.com/developerworks/java/library/j-scala04298/index.html
 [3]: http://selenium.googlecode.com/svn/trunk/docs/api/java/index.html
 [4]: http://www.scalatest.org/
 [5]: http://watir.com/
 [6]: http://geb.codehaus.org/