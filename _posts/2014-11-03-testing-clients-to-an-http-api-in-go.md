---
id: 4371
title: Testing Clients to an HTTP API in Go
author: Marcus Kazmierczak
layout: post
guid: https://mkaz.com/?p=4371
permalink: /2014/11/03/testing-clients-to-an-http-api-in-go/
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
videourl:
  - 
categories:
  - solutions log
tags:
  - golang
  - testing
---
An example on how to test a client which calls out to an external API, without requiring the API server to be up and running. From [Testing Techniques][1] video by Andrew Gerrand at Google I/O 2014.

Go has a standard library `net/http/httptest` which you can use to create a test HTTP server, similar to Go's normal HTTP server. The test server will create a server that listens locally on a random port.

A test consists of

  * Create test server
  * Setup server to return what you want
  * Pass server URL to your test

Here's a simple example from my [fetcher library][2] which tests retrieving a URL with a GET parameter.

I setup my test server to just echo back whatever parameter gets passed in, so then I just need to confirm what I pass in, is what I get back.

Create test `fetcher_test.go` and run from my package dir using `go test`

<pre lang="golang">// This tests GET request with passing in a parameter.
func TestGetParams(t *testing.T) {

    // echoHandler, passes back form parameter p
    echoHandler := func( w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, r.FormValue("p"))
    }

    // create test server with handler
    ts := httptest.NewServer(http.HandlerFunc(echoHandler))
    defer ts.Close()

    // call library I want to test, using test server ts
    f := fetcher.NewFetcher()
    f.Params.Add("p", "hello")
    result, err := f.Fetch(ts.URL, "GET")
    if err != nil {
        t.Errorf("Error: %v", err)
    }

    // confirm result
    if result != "hello" {
        t.Errorf("Unexpected result: %v", result)
    }
}
</pre>

That's all there is to it, check out the video for a ton more useful information around testing in Go. Plus read the [testing][3] and [httptest][4] package documentation.

 [1]: https://www.youtube.com/watch?v=ndmB0bj7eyw
 [2]: https://github.com/mkaz/fetcher
 [3]: http://golang.org/pkg/testing/
 [4]: http://golang.org/pkg/net/http/httptest/