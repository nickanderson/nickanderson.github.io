---
title: Dynamic method calls in CFEngine
author: Nick Anderson
type: post
date: 2012-10-16T20:07:21+00:00
url: /2012/10/16/dynamic-method-calls-in-cfengine/
categories:
  - Posts
tags:
  - CFEngine

---
[<img class="alignright size-medium wp-image-1076" title="dynamic" src="http://www.cmdln.org/images/wp-content/uploads/2012/10/dynamic-300x225.jpg" alt="" width="300" height="225" srcset="http://www.cmdln.org/images/wp-content/uploads/2012/10/dynamic-300x225.jpg 300w, http://www.cmdln.org/images/wp-content/uploads/2012/10/dynamic.jpg 400w" sizes="(max-width: 300px) 100vw, 300px" />][1]Methods type promises are powerful abstraction tools in CFEngine 3. Methods allow you to activate bundles (optionally parametrized) from other bundles. This allows encapsulation of knowledge and lends itself to re-usability.

I just want to share an example of calling bundles dynamically. It&#8217;s a contrived example, but I thought it was neat so here it is.

<div class="gistem">
  <div id="gist-3901453" class="gist">
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="highlight">
          <pre><div class='line' id='LC1'>
  R: in bundle agent handler1: I got value1
</div>

<div class='line' id='LC2'>
  R: in bundle agent handler1: I got value2
</div>

<div class='line' id='LC3'>
  &nbsp;!! Method invoked repairs
</div>

<div class='line' id='LC4'>
  &nbsp;!! Method invoked repairs
</div>

<div class='line' id='LC5'>
  R: in bundle agent handler2: I got value1
</div>

<div class='line' id='LC6'>
  R: in bundle agent handler2: I got value2
</div>

<div class='line' id='LC7'>
  &nbsp;!! Method invoked repairs
</div>

<div class='line' id='LC8'>
  &nbsp;!! Method invoked repairs
</div>

<div class='line' id='LC9'>
  <br />
</div></pre>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/raw/3901453/0b683269921c056b4e821dd2c63ca6b622122e26/output" style="float:right;">view raw</a> <a href="https://gist.github.com/3901453#file_output" style="float:right;margin-right:10px;color:#666">output</a> <a href="https://gist.github.com/3901453">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
    
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="highlight">
          <pre><div class='line' id='LC1'>
  body common control {
</div>

<div class='line' id='LC2'>
  <br />
</div>

<div class='line' id='LC3'>
  &nbsp;&nbsp;&nbsp;&nbsp;bundlesequence =&gt; {"main",};
</div>

<div class='line' id='LC4'>
  <br />
</div>

<div class='line' id='LC5'>
  }
</div>

<div class='line' id='LC6'>
  <br />
</div>

<div class='line' id='LC7'>
  bundle agent main{
</div>

<div class='line' id='LC8'>
  vars:
</div>

<div class='line' id='LC9'>
  &nbsp;&nbsp;"mybundles" slist =&gt; { "handler1","handler2" };
</div>

<div class='line' id='LC10'>
  &nbsp;&nbsp;"myvalues" slist =&gt; { "value1", "value2" };
</div>

<div class='line' id='LC11'>
  <br />
</div>

<div class='line' id='LC12'>
  methods:
</div>

<div class='line' id='LC13'>
  &nbsp;&nbsp;"$(mybundle)" usebundle =&gt; handler_iterator("$(mybundles)", "@(main.myvalues)");
</div>

<div class='line' id='LC14'>
  <br />
</div>

<div class='line' id='LC15'>
  }
</div>

<div class='line' id='LC16'>
  <br />
</div>

<div class='line' id='LC17'>
  bundle agent handler_iterator(handler, values)
</div>

<div class='line' id='LC18'>
  # This expects a single value
</div>

<div class='line' id='LC19'>
  {
</div>

<div class='line' id='LC20'>
  methods:
</div>

<div class='line' id='LC21'>
  &nbsp;&nbsp;"$(handler)" usebundle =&gt; $(handler)("@(handler_iterator.values)");
</div>

<div class='line' id='LC22'>
  <br />
</div>

<div class='line' id='LC23'>
  }
</div>

<div class='line' id='LC24'>
  bundle agent handler1(value1)
</div>

<div class='line' id='LC25'>
  {
</div>

<div class='line' id='LC26'>
  reports:
</div>

<div class='line' id='LC27'>
  &nbsp;&nbsp;cfengine::
</div>

<div class='line' id='LC28'>
  &nbsp;&nbsp;&nbsp;&nbsp;"in bundle agent handler1: I got $(value1)";
</div>

<div class='line' id='LC29'>
  }
</div>

<div class='line' id='LC30'>
  <br />
</div>

<div class='line' id='LC31'>
  bundle agent handler2(value1)
</div>

<div class='line' id='LC32'>
  {
</div>

<div class='line' id='LC33'>
  reports:
</div>

<div class='line' id='LC34'>
  &nbsp;&nbsp;cfengine::
</div>

<div class='line' id='LC35'>
  &nbsp;&nbsp;"in bundle agent handler2: I got $(value1)";
</div>

<div class='line' id='LC36'>
  }
</div>

<div class='line' id='LC37'>
  <br />
</div></pre>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/raw/3901453/67c8bda449460da4d5b8c1983d5b0bbaacc63b13/test.cf" style="float:right;">view raw</a> <a href="https://gist.github.com/3901453#file_test.cf" style="float:right;margin-right:10px;color:#666">test.cf</a> <a href="https://gist.github.com/3901453">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
  </div>
</div>

#### Breakdown

##### bundle agent main

Here we define two lists, a list of bundle names and a list of values. Because of implicit list iteration we then call &#8220;handler_iterator&#8221; 2 times. Once for each value of the mybundles list. Each activation also passes in the myvalues list.

##### Bundle agent handler_iterator

handler\_iterator is where the neat part happens. You can see that we call the bundle $(handler) (outside of quotes) with the parameter @(handler\_iterator.values). This is what I found so interesting. I Have called bundles dynamically in the past, but I have always put the variable inside of quotes. That worked fine but it prevented me from using parameters when calling because the parameters were seen as part of the bundle name.  Here is an example of the handler_iterator bundle trying to use a parametrized value inside of quotes.

<div class="gistem">
  <div id="gist-3901469" class="gist">
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="highlight">
          <pre><div class='line' id='LC1'>
  bundle agent handler_iterator(handler, values)
</div>

<div class='line' id='LC2'>
  # This expects a single value
</div>

<div class='line' id='LC3'>
  {
</div>

<div class='line' id='LC4'>
  methods:
</div>

<div class='line' id='LC5'>
  &nbsp;&nbsp;"$(handler) $(values)" usebundle =&gt; "$(handler)($(values))";
</div>

<div class='line' id='LC6'>
  <br />
</div>

<div class='line' id='LC7'>
  }
</div></pre>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/raw/3901469/68b0a864b987496cdd8d936bb5d8777ca6fc6f6a/example%20of%20bundle%20inside%20quotes" style="float:right;">view raw</a> <a href="https://gist.github.com/3901469#file_example of bundle inside quotes" style="float:right;margin-right:10px;color:#666">example of bundle inside quotes</a> <a href="https://gist.github.com/3901469">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
    
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="highlight">
          <pre><div class='line' id='LC1'>
  &nbsp;!! A method attempted to use a bundle "handler1(value1)" that was apparently not defined!
</div>

<div class='line' id='LC2'>
  I: Report relates to a promise with handle ""
</div>

<div class='line' id='LC3'>
  I: Made in version &#39;not specified&#39; of &#39;./test.cf&#39; near line 21
</div>

<div class='line' id='LC4'>
  &nbsp;!! A method attempted to use a bundle "handler1(value2)" that was apparently not defined!
</div>

<div class='line' id='LC5'>
  I: Report relates to a promise with handle ""
</div>

<div class='line' id='LC6'>
  I: Made in version &#39;not specified&#39; of &#39;./test.cf&#39; near line 21
</div>

<div class='line' id='LC7'>
  &nbsp;!! Method failed in some repairs or aborted
</div>

<div class='line' id='LC8'>
  &nbsp;!! A method attempted to use a bundle "handler2(value1)" that was apparently not defined!
</div>

<div class='line' id='LC9'>
  I: Report relates to a promise with handle ""
</div>

<div class='line' id='LC10'>
  I: Made in version &#39;not specified&#39; of &#39;./test.cf&#39; near line 21
</div>

<div class='line' id='LC11'>
  &nbsp;!! A method attempted to use a bundle "handler2(value2)" that was apparently not defined!
</div>

<div class='line' id='LC12'>
  I: Report relates to a promise with handle ""
</div>

<div class='line' id='LC13'>
  I: Made in version &#39;not specified&#39; of &#39;./test.cf&#39; near line 21
</div>

<div class='line' id='LC14'>
  &nbsp;!! Method failed in some repairs or aborted
</div>

<div class='line' id='LC15'>
  <br />
</div></pre>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/raw/3901469/718fbe133ea02c04d6d55badaf599f90fdc7679b/output" style="float:right;">view raw</a> <a href="https://gist.github.com/3901469#file_output" style="float:right;margin-right:10px;color:#666">output</a> <a href="https://gist.github.com/3901469">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
  </div>
</div>

Since $(handler) is a single value (we iterated over the list of bundles in bundle agent main) only one method activation will happen for each activation of handler_iterator.

##### bundle agent handlerx

The handlers themselves just report once for each item in the list passed to them.

##### Specific Use Case

Well, I don&#8217;t have one. I can however imagine that based on some variable event you might want to call a bundle with some variable parameter. Something like the <a href="https://github.com/cfengine/design-center/tree/master/sketches/utilities/nagios_plugin_agent" target="_blank">nagios_plugin_agent</a> sketch comes to mind. (It can call a variable bundle right now).

 [1]: http://www.cmdln.org/images/wp-content/uploads/2012/10/dynamic.jpg
