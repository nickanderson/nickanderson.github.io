---
title: Canonifying a list with CFEngine 3
author: Nick Anderson
type: post
date: 2013-03-29T14:12:14+00:00
url: /2013/03/29/canonifying-a-list-with-cfengine-3/
categories:
  - Posts
tags:
  - canonify
  - CFEngine
  - list
  - pattern

---
John Sanders [<img class="alignright  wp-image-1159" alt="Glass_pour_section_on_restaurant_wine_list" src="http://www.cmdln.org/images/wp-content/uploads/2013/03/Glass_pour_section_on_restaurant_wine_list-300x225.jpg" width="162" height="122" srcset="http://www.cmdln.org/images/wp-content/uploads/2013/03/Glass_pour_section_on_restaurant_wine_list-300x225.jpg 300w, http://www.cmdln.org/images/wp-content/uploads/2013/03/Glass_pour_section_on_restaurant_wine_list-1024x768.jpg 1024w, http://www.cmdln.org/images/wp-content/uploads/2013/03/Glass_pour_section_on_restaurant_wine_list.jpg 1280w" sizes="(max-width: 162px) 100vw, 162px" />][1]shared a pattern for canonifying lists in #CFEngine on irc.freenode.net yesterday. It&#8217;s a useful reference so I thought I would replicate it here.

<div class="gistem">
  <div id="gist5271023" class="gist">
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="file-data">
          <table cellpadding="0" cellspacing="0" class="lines highlight">
            <tr>
              <td class="line-numbers">
                <span class="line-number" id="file-output-L1" rel="file-output-L1">1</span> <span class="line-number" id="file-output-L2" rel="file-output-L2">2</span> <span class="line-number" id="file-output-L3" rel="file-output-L3">3</span> <span class="line-number" id="file-output-L4" rel="file-output-L4">4</span> <span class="line-number" id="file-output-L5" rel="file-output-L5">5</span> <span class="line-number" id="file-output-L6" rel="file-output-L6">6</span>
              </td>
              
              <td class="line-data">
                <pre class="line-pre"><div class="line" id="file-output-LC1">
  % cf-agent -KIf ./example_canonify_list.cf
</div>

<div class="line" id="file-output-LC2">
  R: canonified site: www_example_com
</div>

<div class="line" id="file-output-LC3">
  R: canonified site: www_example2_com
</div>

<div class="line" id="file-output-LC4">
  R: alternate canonified site: www_example_com
</div>

<div class="line" id="file-output-LC5">
  R: alternate canonified site: www_example2_com
</div>

<div class="line" id="file-output-LC6">
  !! Method invoked repairs
</div></pre>
              </td>
            </tr>
          </table>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/nickanderson/5271023/raw/d57a43831308cf31f0a5fe237b3d3436ed3d3049/Output" style="float:right">view raw</a> <a href="https://gist.github.com/nickanderson/5271023#file-output" style="float:right; margin-right:10px; color:#666;">Output</a> <a href="https://gist.github.com/nickanderson/5271023">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
    
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="file-data">
          <table cellpadding="0" cellspacing="0" class="lines highlight">
            <tr>
              <td class="line-numbers">
                <span class="line-number" id="file-example_canonify_list-cf-L1" rel="file-example_canonify_list-cf-L1">1</span> <span class="line-number" id="file-example_canonify_list-cf-L2" rel="file-example_canonify_list-cf-L2">2</span> <span class="line-number" id="file-example_canonify_list-cf-L3" rel="file-example_canonify_list-cf-L3">3</span> <span class="line-number" id="file-example_canonify_list-cf-L4" rel="file-example_canonify_list-cf-L4">4</span> <span class="line-number" id="file-example_canonify_list-cf-L5" rel="file-example_canonify_list-cf-L5">5</span> <span class="line-number" id="file-example_canonify_list-cf-L6" rel="file-example_canonify_list-cf-L6">6</span> <span class="line-number" id="file-example_canonify_list-cf-L7" rel="file-example_canonify_list-cf-L7">7</span> <span class="line-number" id="file-example_canonify_list-cf-L8" rel="file-example_canonify_list-cf-L8">8</span> <span class="line-number" id="file-example_canonify_list-cf-L9" rel="file-example_canonify_list-cf-L9">9</span> <span class="line-number" id="file-example_canonify_list-cf-L10" rel="file-example_canonify_list-cf-L10">10</span> <span class="line-number" id="file-example_canonify_list-cf-L11" rel="file-example_canonify_list-cf-L11">11</span> <span class="line-number" id="file-example_canonify_list-cf-L12" rel="file-example_canonify_list-cf-L12">12</span> <span class="line-number" id="file-example_canonify_list-cf-L13" rel="file-example_canonify_list-cf-L13">13</span> <span class="line-number" id="file-example_canonify_list-cf-L14" rel="file-example_canonify_list-cf-L14">14</span> <span class="line-number" id="file-example_canonify_list-cf-L15" rel="file-example_canonify_list-cf-L15">15</span> <span class="line-number" id="file-example_canonify_list-cf-L16" rel="file-example_canonify_list-cf-L16">16</span> <span class="line-number" id="file-example_canonify_list-cf-L17" rel="file-example_canonify_list-cf-L17">17</span> <span class="line-number" id="file-example_canonify_list-cf-L18" rel="file-example_canonify_list-cf-L18">18</span> <span class="line-number" id="file-example_canonify_list-cf-L19" rel="file-example_canonify_list-cf-L19">19</span> <span class="line-number" id="file-example_canonify_list-cf-L20" rel="file-example_canonify_list-cf-L20">20</span> <span class="line-number" id="file-example_canonify_list-cf-L21" rel="file-example_canonify_list-cf-L21">21</span> <span class="line-number" id="file-example_canonify_list-cf-L22" rel="file-example_canonify_list-cf-L22">22</span> <span class="line-number" id="file-example_canonify_list-cf-L23" rel="file-example_canonify_list-cf-L23">23</span> <span class="line-number" id="file-example_canonify_list-cf-L24" rel="file-example_canonify_list-cf-L24">24</span> <span class="line-number" id="file-example_canonify_list-cf-L25" rel="file-example_canonify_list-cf-L25">25</span> <span class="line-number" id="file-example_canonify_list-cf-L26" rel="file-example_canonify_list-cf-L26">26</span> <span class="line-number" id="file-example_canonify_list-cf-L27" rel="file-example_canonify_list-cf-L27">27</span> <span class="line-number" id="file-example_canonify_list-cf-L28" rel="file-example_canonify_list-cf-L28">28</span> <span class="line-number" id="file-example_canonify_list-cf-L29" rel="file-example_canonify_list-cf-L29">29</span> <span class="line-number" id="file-example_canonify_list-cf-L30" rel="file-example_canonify_list-cf-L30">30</span> <span class="line-number" id="file-example_canonify_list-cf-L31" rel="file-example_canonify_list-cf-L31">31</span> <span class="line-number" id="file-example_canonify_list-cf-L32" rel="file-example_canonify_list-cf-L32">32</span> <span class="line-number" id="file-example_canonify_list-cf-L33" rel="file-example_canonify_list-cf-L33">33</span> <span class="line-number" id="file-example_canonify_list-cf-L34" rel="file-example_canonify_list-cf-L34">34</span> <span class="line-number" id="file-example_canonify_list-cf-L35" rel="file-example_canonify_list-cf-L35">35</span> <span class="line-number" id="file-example_canonify_list-cf-L36" rel="file-example_canonify_list-cf-L36">36</span> <span class="line-number" id="file-example_canonify_list-cf-L37" rel="file-example_canonify_list-cf-L37">37</span> <span class="line-number" id="file-example_canonify_list-cf-L38" rel="file-example_canonify_list-cf-L38">38</span> <span class="line-number" id="file-example_canonify_list-cf-L39" rel="file-example_canonify_list-cf-L39">39</span>
              </td>
              
              <td class="line-data">
                <pre class="line-pre"><div class="line" id="file-example_canonify_list-cf-LC1">
  body common control
</div>

<div class="line" id="file-example_canonify_list-cf-LC2">
  {
</div>

<div class="line" id="file-example_canonify_list-cf-LC3">
  bundlesequence =&gt; { "main" };
</div>

<div class="line" id="file-example_canonify_list-cf-LC4">
  inputs =&gt; { "cfengine_stdlib.cf", };
</div>

<div class="line" id="file-example_canonify_list-cf-LC5">
  }
</div>

<div class="line" id="file-example_canonify_list-cf-LC6">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC7">
  bundle agent main
</div>

<div class="line" id="file-example_canonify_list-cf-LC8">
  {
</div>

<div class="line" id="file-example_canonify_list-cf-LC9">
  vars:
</div>

<div class="line" id="file-example_canonify_list-cf-LC10">
  "apache_config[www.example.com][DocumentRoot]" string =&gt; "/var/www/www.example.com";
</div>

<div class="line" id="file-example_canonify_list-cf-LC11">
  "apache_config[www.example.com][ServerAdmin]" string =&gt; "webmaster@example2.com";
</div>

<div class="line" id="file-example_canonify_list-cf-LC12">
  "apache_config[www.example2.com][DocumentRoot]" string =&gt; "/var/www/www.example2.com";
</div>

<div class="line" id="file-example_canonify_list-cf-LC13">
  "apache_config[www.example2.com][ServerAdmin]" string =&gt; "webmaster@example3.com";
</div>

<div class="line" id="file-example_canonify_list-cf-LC14">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC15">
  methods:
</div>

<div class="line" id="file-example_canonify_list-cf-LC16">
  "Testing" usebundle =&gt; test("main.apache_config");
</div>

<div class="line" id="file-example_canonify_list-cf-LC17">
  
</div>

<div class="line" id="file-example_canonify_list-cf-LC18">
  }
</div>

<div class="line" id="file-example_canonify_list-cf-LC19">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC20">
  bundle agent test(config)
</div>

<div class="line" id="file-example_canonify_list-cf-LC21">
  {
</div>

<div class="line" id="file-example_canonify_list-cf-LC22">
  vars:
</div>

<div class="line" id="file-example_canonify_list-cf-LC23">
  # build a list from the first index on the config array
</div>

<div class="line" id="file-example_canonify_list-cf-LC24">
  "site_names" slist =&gt; getindices("$(config)");
</div>

<div class="line" id="file-example_canonify_list-cf-LC25">
  # Build a new array mapping the original index to a canonified version of itself
</div>

<div class="line" id="file-example_canonify_list-cf-LC26">
  "site_names_canonified_map[$(site_names)]" string =&gt; canonify("$(site_names)");
</div>

<div class="line" id="file-example_canonify_list-cf-LC27">
  # Build a list of just the canonified versions
</div>

<div class="line" id="file-example_canonify_list-cf-LC28">
  "site_names_canonified_list" slist =&gt; maplist("$(site_names_canonified_map[$(this)])", "site_names");
</div>

<div class="line" id="file-example_canonify_list-cf-LC29">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC30">
  # alternate way to build list of canonified values
</div>

<div class="line" id="file-example_canonify_list-cf-LC31">
  # due to a bug in the way getindices/getvalues works this needs to happen on the pass after the map array is generated
</div>

<div class="line" id="file-example_canonify_list-cf-LC32">
  "site_names_canonified_list2" slist =&gt; getvalues("site_names_canonified_map"), policy =&gt; "free";
</div>

<div class="line" id="file-example_canonify_list-cf-LC33">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC34">
  reports:
</div>

<div class="line" id="file-example_canonify_list-cf-LC35">
  cfengine::
</div>

<div class="line" id="file-example_canonify_list-cf-LC36">
  "canonified site: $(site_names_canonified_list)";
</div>

<div class="line" id="file-example_canonify_list-cf-LC37">
  "alternate canonified site: $(site_names_canonified_list2)";
</div>

<div class="line" id="file-example_canonify_list-cf-LC38">
  &nbsp;
</div>

<div class="line" id="file-example_canonify_list-cf-LC39">
  }
</div></pre>
              </td>
            </tr>
          </table>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/nickanderson/5271023/raw/b86b207ec0c8b89513a5882ce08330a97dedd513/example_canonify_list.cf" style="float:right">view raw</a> <a href="https://gist.github.com/nickanderson/5271023#file-example_canonify_list-cf" style="float:right; margin-right:10px; color:#666;">example_canonify_list.cf</a> <a href="https://gist.github.com/nickanderson/5271023">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
  </div>
</div>

&nbsp;

In lines 9-12 of the example policy we build an array with values that need to be canonified. We use getindices to get the list of the first index. You could just as easily start with a list of values that need canonified. John used the maplist function to construct a new array with the original index values and their canonified versions. Another way to do this is to use getvalues. Currently (as of CFEngine 3.4.4) getindices and getvalues are not able to get the index of a generated array on the same pass, so its something to be aware of if your using that approach. However Johns approach using maplist is able to work on the same pass because it does not rely on getting the index of the newly generated map array.

&nbsp;

 [1]: http://www.cmdln.org/images/wp-content/uploads/2013/03/Glass_pour_section_on_restaurant_wine_list.jpg
