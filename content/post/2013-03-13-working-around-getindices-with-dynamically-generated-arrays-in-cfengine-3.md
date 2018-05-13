---
title: Working around getindices with dynamically generated arrays in CFEngine 3
author: Nick Anderson
type: post
date: 2013-03-13T17:44:58+00:00
url: /2013/03/13/working-around-getindices-with-dynamically-generated-arrays-in-cfengine-3/
categories:
  - Posts
tags:
  - CFEngine
  - tips

---
There is a <a href="https://cfengine.com/dev/issues/2088" target="_blank">known bug</a> where <a href="https://cfengine.com/manuals/cf3-Reference#Function-getindices" target="_blank">getindices</a> is unable to get the index <img class="alignright size-medium wp-image-1150" alt="Workaround" src="http://www.cmdln.org/wp-content/uploads/2013/03/work-around-300x223.jpg" width="300" height="223" srcset="http://www.cmdln.org/wp-content/uploads/2013/03/work-around-300x223.jpg 300w, http://www.cmdln.org/wp-content/uploads/2013/03/work-around.jpg 550w" sizes="(max-width: 300px) 100vw, 300px" />of a dynamically generated array until the next pass. This comes up from time to time so I thought I would post an example using a pattern shared on the <a href="http://groups.google.com/group/help-cfengine?hl=en" target="_blank">CFEngine help mailing list</a>. The policy below shows 3 working examples. They are mostly similar, example0 shows the simplest workaround, example1 and example2 in addition show ways to suppress the &#8220;Duplicate selection of value for variable&#8221; messages.

<div class="gistem">
  <div id="gist5154392" class="gist">
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="file-data">
          <table cellpadding="0" cellspacing="0" class="lines highlight">
            <tr>
              <td class="line-numbers">
                <span class="line-number" id="file-output-txt-L1" rel="file-output-txt-L1">1</span> <span class="line-number" id="file-output-txt-L2" rel="file-output-txt-L2">2</span> <span class="line-number" id="file-output-txt-L3" rel="file-output-txt-L3">3</span> <span class="line-number" id="file-output-txt-L4" rel="file-output-txt-L4">4</span> <span class="line-number" id="file-output-txt-L5" rel="file-output-txt-L5">5</span> <span class="line-number" id="file-output-txt-L6" rel="file-output-txt-L6">6</span> <span class="line-number" id="file-output-txt-L7" rel="file-output-txt-L7">7</span> <span class="line-number" id="file-output-txt-L8" rel="file-output-txt-L8">8</span> <span class="line-number" id="file-output-txt-L9" rel="file-output-txt-L9">9</span> <span class="line-number" id="file-output-txt-L10" rel="file-output-txt-L10">10</span> <span class="line-number" id="file-output-txt-L11" rel="file-output-txt-L11">11</span> <span class="line-number" id="file-output-txt-L12" rel="file-output-txt-L12">12</span> <span class="line-number" id="file-output-txt-L13" rel="file-output-txt-L13">13</span> <span class="line-number" id="file-output-txt-L14" rel="file-output-txt-L14">14</span>
              </td>
              
              <td class="line-data">
                <pre class="line-pre"><div class="line" id="file-output-txt-LC1">
  cf-agent -KIf ./test_getindices_dynamic_array.cf
</div>

<div class="line" id="file-output-txt-LC2">
  !! Duplicate selection of value for variable "idx" in scope example0
</div>

<div class="line" id="file-output-txt-LC3">
  !! Rule from ./test_getindices_dynamic_array.cf at/before line 28
</div>

<div class="line" id="file-output-txt-LC4">
  !! Duplicate selection of value for variable "idx" in scope example0
</div>

<div class="line" id="file-output-txt-LC5">
  !! Rule from ./test_getindices_dynamic_array.cf at/before line 28
</div>

<div class="line" id="file-output-txt-LC6">
  R: example0 item1
</div>

<div class="line" id="file-output-txt-LC7">
  R: example0 item2
</div>

<div class="line" id="file-output-txt-LC8">
  R: example0 item3
</div>

<div class="line" id="file-output-txt-LC9">
  R: example1 item1
</div>

<div class="line" id="file-output-txt-LC10">
  R: example1 item2
</div>

<div class="line" id="file-output-txt-LC11">
  R: example1 item3
</div>

<div class="line" id="file-output-txt-LC12">
  R: example2 item1
</div>

<div class="line" id="file-output-txt-LC13">
  R: example2 item2
</div>

<div class="line" id="file-output-txt-LC14">
  R: example2 item3
</div></pre>
              </td>
            </tr>
          </table>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/nickanderson/5154392/raw/0173ced1600e7bb221dafb5661ff516f14e6929b/output.txt" style="float:right">view raw</a> <a href="https://gist.github.com/nickanderson/5154392#file-output-txt" style="float:right; margin-right:10px; color:#666;">output.txt</a> <a href="https://gist.github.com/nickanderson/5154392">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
    
    <div class="gist-file">
      <div class="gist-data gist-syntax">
        <div class="file-data">
          <table cellpadding="0" cellspacing="0" class="lines highlight">
            <tr>
              <td class="line-numbers">
                <span class="line-number" id="file-test_getindices_dynamic_array-cf-L1" rel="file-test_getindices_dynamic_array-cf-L1">1</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L2" rel="file-test_getindices_dynamic_array-cf-L2">2</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L3" rel="file-test_getindices_dynamic_array-cf-L3">3</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L4" rel="file-test_getindices_dynamic_array-cf-L4">4</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L5" rel="file-test_getindices_dynamic_array-cf-L5">5</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L6" rel="file-test_getindices_dynamic_array-cf-L6">6</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L7" rel="file-test_getindices_dynamic_array-cf-L7">7</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L8" rel="file-test_getindices_dynamic_array-cf-L8">8</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L9" rel="file-test_getindices_dynamic_array-cf-L9">9</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L10" rel="file-test_getindices_dynamic_array-cf-L10">10</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L11" rel="file-test_getindices_dynamic_array-cf-L11">11</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L12" rel="file-test_getindices_dynamic_array-cf-L12">12</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L13" rel="file-test_getindices_dynamic_array-cf-L13">13</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L14" rel="file-test_getindices_dynamic_array-cf-L14">14</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L15" rel="file-test_getindices_dynamic_array-cf-L15">15</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L16" rel="file-test_getindices_dynamic_array-cf-L16">16</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L17" rel="file-test_getindices_dynamic_array-cf-L17">17</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L18" rel="file-test_getindices_dynamic_array-cf-L18">18</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L19" rel="file-test_getindices_dynamic_array-cf-L19">19</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L20" rel="file-test_getindices_dynamic_array-cf-L20">20</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L21" rel="file-test_getindices_dynamic_array-cf-L21">21</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L22" rel="file-test_getindices_dynamic_array-cf-L22">22</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L23" rel="file-test_getindices_dynamic_array-cf-L23">23</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L24" rel="file-test_getindices_dynamic_array-cf-L24">24</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L25" rel="file-test_getindices_dynamic_array-cf-L25">25</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L26" rel="file-test_getindices_dynamic_array-cf-L26">26</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L27" rel="file-test_getindices_dynamic_array-cf-L27">27</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L28" rel="file-test_getindices_dynamic_array-cf-L28">28</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L29" rel="file-test_getindices_dynamic_array-cf-L29">29</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L30" rel="file-test_getindices_dynamic_array-cf-L30">30</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L31" rel="file-test_getindices_dynamic_array-cf-L31">31</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L32" rel="file-test_getindices_dynamic_array-cf-L32">32</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L33" rel="file-test_getindices_dynamic_array-cf-L33">33</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L34" rel="file-test_getindices_dynamic_array-cf-L34">34</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L35" rel="file-test_getindices_dynamic_array-cf-L35">35</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L36" rel="file-test_getindices_dynamic_array-cf-L36">36</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L37" rel="file-test_getindices_dynamic_array-cf-L37">37</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L38" rel="file-test_getindices_dynamic_array-cf-L38">38</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L39" rel="file-test_getindices_dynamic_array-cf-L39">39</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L40" rel="file-test_getindices_dynamic_array-cf-L40">40</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L41" rel="file-test_getindices_dynamic_array-cf-L41">41</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L42" rel="file-test_getindices_dynamic_array-cf-L42">42</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L43" rel="file-test_getindices_dynamic_array-cf-L43">43</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L44" rel="file-test_getindices_dynamic_array-cf-L44">44</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L45" rel="file-test_getindices_dynamic_array-cf-L45">45</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L46" rel="file-test_getindices_dynamic_array-cf-L46">46</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L47" rel="file-test_getindices_dynamic_array-cf-L47">47</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L48" rel="file-test_getindices_dynamic_array-cf-L48">48</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L49" rel="file-test_getindices_dynamic_array-cf-L49">49</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L50" rel="file-test_getindices_dynamic_array-cf-L50">50</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L51" rel="file-test_getindices_dynamic_array-cf-L51">51</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L52" rel="file-test_getindices_dynamic_array-cf-L52">52</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L53" rel="file-test_getindices_dynamic_array-cf-L53">53</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L54" rel="file-test_getindices_dynamic_array-cf-L54">54</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L55" rel="file-test_getindices_dynamic_array-cf-L55">55</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L56" rel="file-test_getindices_dynamic_array-cf-L56">56</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L57" rel="file-test_getindices_dynamic_array-cf-L57">57</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L58" rel="file-test_getindices_dynamic_array-cf-L58">58</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L59" rel="file-test_getindices_dynamic_array-cf-L59">59</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L60" rel="file-test_getindices_dynamic_array-cf-L60">60</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L61" rel="file-test_getindices_dynamic_array-cf-L61">61</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L62" rel="file-test_getindices_dynamic_array-cf-L62">62</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L63" rel="file-test_getindices_dynamic_array-cf-L63">63</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L64" rel="file-test_getindices_dynamic_array-cf-L64">64</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L65" rel="file-test_getindices_dynamic_array-cf-L65">65</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L66" rel="file-test_getindices_dynamic_array-cf-L66">66</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L67" rel="file-test_getindices_dynamic_array-cf-L67">67</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L68" rel="file-test_getindices_dynamic_array-cf-L68">68</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L69" rel="file-test_getindices_dynamic_array-cf-L69">69</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L70" rel="file-test_getindices_dynamic_array-cf-L70">70</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L71" rel="file-test_getindices_dynamic_array-cf-L71">71</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L72" rel="file-test_getindices_dynamic_array-cf-L72">72</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L73" rel="file-test_getindices_dynamic_array-cf-L73">73</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L74" rel="file-test_getindices_dynamic_array-cf-L74">74</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L75" rel="file-test_getindices_dynamic_array-cf-L75">75</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L76" rel="file-test_getindices_dynamic_array-cf-L76">76</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L77" rel="file-test_getindices_dynamic_array-cf-L77">77</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L78" rel="file-test_getindices_dynamic_array-cf-L78">78</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L79" rel="file-test_getindices_dynamic_array-cf-L79">79</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L80" rel="file-test_getindices_dynamic_array-cf-L80">80</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L81" rel="file-test_getindices_dynamic_array-cf-L81">81</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L82" rel="file-test_getindices_dynamic_array-cf-L82">82</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L83" rel="file-test_getindices_dynamic_array-cf-L83">83</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L84" rel="file-test_getindices_dynamic_array-cf-L84">84</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L85" rel="file-test_getindices_dynamic_array-cf-L85">85</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L86" rel="file-test_getindices_dynamic_array-cf-L86">86</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L87" rel="file-test_getindices_dynamic_array-cf-L87">87</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L88" rel="file-test_getindices_dynamic_array-cf-L88">88</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L89" rel="file-test_getindices_dynamic_array-cf-L89">89</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L90" rel="file-test_getindices_dynamic_array-cf-L90">90</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L91" rel="file-test_getindices_dynamic_array-cf-L91">91</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L92" rel="file-test_getindices_dynamic_array-cf-L92">92</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L93" rel="file-test_getindices_dynamic_array-cf-L93">93</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L94" rel="file-test_getindices_dynamic_array-cf-L94">94</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L95" rel="file-test_getindices_dynamic_array-cf-L95">95</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L96" rel="file-test_getindices_dynamic_array-cf-L96">96</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L97" rel="file-test_getindices_dynamic_array-cf-L97">97</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L98" rel="file-test_getindices_dynamic_array-cf-L98">98</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L99" rel="file-test_getindices_dynamic_array-cf-L99">99</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L100" rel="file-test_getindices_dynamic_array-cf-L100">100</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L101" rel="file-test_getindices_dynamic_array-cf-L101">101</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L102" rel="file-test_getindices_dynamic_array-cf-L102">102</span> <span class="line-number" id="file-test_getindices_dynamic_array-cf-L103" rel="file-test_getindices_dynamic_array-cf-L103">103</span>
              </td>
              
              <td class="line-data">
                <pre class="line-pre"><div class="line" id="file-test_getindices_dynamic_array-cf-LC1">
  body common control
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC2">
  {
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC3">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC4">
  bundlesequence =&gt; {
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC5">
  "example0",
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC6">
  "example1",
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC7">
  "example2",
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC8">
  };
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC9">
  }
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC10">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC11">
  bundle agent example0
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC12">
  # This pattern was shared on the CFEngine help mailing list by cyril
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC13">
  # Thanks!
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC14">
  {
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC15">
  vars:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC16">
  "list" slist =&gt; { "1", "2", "3" };
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC17">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC18">
  # Autogenerate an array instead of typing it out
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC19">
  # "array[item1]" string =&gt; "value1";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC20">
  # "array[item2]" string =&gt; "value2";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC21">
  # "array[item3]" string =&gt; "value3";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC22">
  "array[item$(list)]" string =&gt; "value$(list)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC23">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC24">
  !idx_defined::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC25">
  "idx"
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC26">
  slist =&gt; { getindices("array") },
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC27">
  handle =&gt; "$(this.bundle)_get_array_index";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC28">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC29">
  classes:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC30">
  "idx_defined" expression =&gt; isvariable("idx");
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC31">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC32">
  reports:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC33">
  cfengine::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC34">
  # should report 3 times itemx where x is a list value
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC35">
  "$(this.bundle) $(idx)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC36">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC37">
  }
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC38">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC39">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC40">
  bundle agent example1
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC41">
  # This pattern was shared on the CFEngine help mailing list by cyril
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC42">
  # Thanks!
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC43">
  {
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC44">
  vars:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC45">
  "list" slist =&gt; { "1", "2", "3" };
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC46">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC47">
  # Autogenerate an array instead of typing it out
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC48">
  # "array[item1]" string =&gt; "value1";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC49">
  # "array[item2]" string =&gt; "value2";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC50">
  # "array[item3]" string =&gt; "value3";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC51">
  "array[item$(list)]" string =&gt; "value$(list)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC52">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC53">
  list_defined.!idx_defined::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC54">
  "idx"
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC55">
  slist =&gt; { getindices("array") },
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC56">
  handle =&gt; "$(this.bundle)_get_array_index";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC57">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC58">
  classes:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC59">
  "list_defined"
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC60">
  expression =&gt; isvariable("list"),
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC61">
  comment    =&gt; "This is one way to work around &#39;Duplicate selection of
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC62">
  value for variable&#39; messages. Your forcing get_array_index
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC63">
  to not be evaluated until the next pass";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC64">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC65">
  "idx_defined" expression =&gt; isvariable("idx");
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC66">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC67">
  reports:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC68">
  cfengine::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC69">
  # should report 3 times itemx where x is a list value
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC70">
  "$(this.bundle) $(idx)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC71">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC72">
  }
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC73">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC74">
  bundle agent example2
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC75">
  # This pattern was shared on the CFEngine help mailing list by cyril
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC76">
  # Thanks!
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC77">
  {
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC78">
  vars:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC79">
  "list" slist =&gt; { "1", "2", "3" };
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC80">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC81">
  # Autogenerate an array instead of typing it out
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC82">
  # "array[item1]" string =&gt; "value1";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC83">
  # "array[item2]" string =&gt; "value2";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC84">
  # "array[item3]" string =&gt; "value3";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC85">
  "array[item$(list)]" string =&gt; "value$(list)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC86">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC87">
  !idx_defined::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC88">
  "idx"
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC89">
  slist   =&gt; { getindices("array") },
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC90">
  policy  =&gt; "free",
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC91">
  handle  =&gt; "$(this.bundle)_get_array_index",
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC92">
  comment =&gt; "Setting policy free is another way to suppress &#39;Duplicate
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC93">
  selection of value for variable&#39; messages.";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC94">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC95">
  classes:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC96">
  "idx_defined" expression =&gt; isvariable("idx");
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC97">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC98">
  reports:
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC99">
  cfengine::
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC100">
  # should report 3 times itemx where x is a list value
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC101">
  "$(this.bundle) $(idx)";
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC102">
  &nbsp;
</div>

<div class="line" id="file-test_getindices_dynamic_array-cf-LC103">
  }
</div></pre>
              </td>
            </tr>
          </table>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/nickanderson/5154392/raw/d1b746f381b08a8e466820e0152676ab1fbf585a/test_getindices_dynamic_array.cf" style="float:right">view raw</a> <a href="https://gist.github.com/nickanderson/5154392#file-test_getindices_dynamic_array-cf" style="float:right; margin-right:10px; color:#666;">test_getindices_dynamic_array.cf</a> <a href="https://gist.github.com/nickanderson/5154392">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
  </div>
</div>

&nbsp;

&nbsp;