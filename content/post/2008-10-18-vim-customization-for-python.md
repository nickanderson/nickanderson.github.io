---
title: Vim customization for python
author: Nick Anderson
type: post
date: 2008-10-18T19:19:06+00:00
url: /2008/10/18/vim-customization-for-python/
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - python
  - python ide
  - vim

---
Python seems to keep growing on me. By no means am I a Python master, nor am I a vim guru but I do prefer to use vim over a gui editor. Sure there are some niceties with using a gui but getting comfortable using a tool that is almost always at your disposal has something to be said for it. Adding a few things to your vim environment will make writing python much more pleasurable.<!--more-->

First there is the [python indent plugin][1]. At the time of this writing the current version is 0.3. There is one annoying thing about it. When commenting with hashes it un-indents. Luckily <span class="author"><a href="http://henry.precheur.org/2008/4/18/Indenting%20Python%20with%20VIM.html">Henry Prêcheu pointed out</a> that its an easy one line fix.</span>

<pre class="brush: bash; title: ; notranslate" title="">setlocal indentkeys=!^F,o,O,&lt;:&gt;,0),0],0},=elif,=except
</pre>

should be changed to.

<pre class="brush: bash; title: ; notranslate" title="">setlocal indentkeys=!^F,o,O,&lt;:&gt;,0),0],0},=elif,=except,0#
</pre>

Here is the full updated version of the script. [Vim Python Indent 0.4_alpha1][2]

**Syntax Highlighting**

Download http://www.vim.org/scripts/script.php?script_id=790 at the time of this writing the current version is 2.6.3. and place it in your .vim /syntax/ directory (if its not there you should create it). This will add awesome highlighting to your python files. But we can make it better! We can add some simple error checking for things like missing colons. These are the additions that I have added which I found provided by [sontek aka John M. Anderson][3]. Don&#8217;t forget to add `syntax on` to your .vimrc.

<pre class="brush: bash; title: ; notranslate" title="">syn match pythonError "^\s*def\s\+\w\+(.*)\s*$" display
syn match pythonError "^\s*class\s\+\w\+(.*)\s*$" display
syn match pythonError "^\s*for\s.*[^:]$" display
syn match pythonError "^\s*except\s*$" display
syn match pythonError "^\s*finally\s*$" display
syn match pythonError "^\s*try\s*$" display
syn match pythonError "^\s*else\s*$" display
syn match pythonError "^\s*else\s*[^:].*" display
syn match pythonError "^\s*if\s.*[^\:]$" display
syn match pythonError "^\s*except\s.*[^\:]$" display
syn match pythonError "[;]$" display
syn keyword pythonError         do
</pre>

We can take that a step further with the following additions to your .vimrc.

<pre class="brush: bash; title: ; notranslate" title="">" Syntax checking entire file
" Usage: :make (check file)
" :clist (view list of errors)
" :cn, :cp (move around list of errors)
autocmd BufRead *.py set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
autocmd BufRead *.py set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
</pre>

This will allow you to check the syntax ofyour entire file by typing :make. you can the get a list of errors with :clist and move between the errors with :cn and :cp.

**Execute block of code**
  
Sometimes you want to check or execute a block of code. Drop the [python execute block vim script][4] into your .vim/ftplugin/ directory. With it you can visually select a block of code and execute it with Ctrl+h.

**Debugging**
  
So you are finding errors in your code and want to trace them? Drop this [python ipdb vim script][5] into your .vim/ftplugin/directory. You can set break points with F7 and clear them with shift-F7. If your not familiar with ipdb you should look it up.

While we&#8217;re at it lets add an easy way to run your current script.
  
<span style="text-decoration: line-through;">map <f8> :!python %<cr></span>
  
It was pointed out by [fboender][6] on [reddit][7] that there is a better way to do this.

Download the [bexec plugin][8] open it with vim using the full path to your vimball and then type :so % to source and install the vimball. Now setup some maps for it.

<pre class="brush: bash; title: ; notranslate" title="">nmap &lt;silent&gt; &lt;unique&gt; &lt;F8&gt; :call Bexec()&lt;cr&gt;
vmap &lt;silent&gt; &lt;unique&gt; &lt;F8&gt; :call BexecVisual()&lt;cr&gt;
map &lt;silent&gt; &lt;unique &lt;F9&gt; :call BexecCloseOut()&lt;cr&gt;</pre>

in your .vimrc will cause F8 to run the file you currently have open.

**Tabs**
  
Who doesn&#8217;t love tabs? You can have them in vim too ya know! Add these lines to your .vimrc

<pre class="brush: bash; title: ; notranslate" title="">map \t :tabnew&lt;cr&gt;
map \n :tabnext&lt;cr&gt;
map \p :tabprevious&lt;cr&gt;
map \c :tabclose&lt;cr&gt;
</pre>

With these additions you can open a new tab with \t move right with \n and move left with \p. To close the tab simply enter \c.

**Edit File Menu**
  
You can add a handy menu when opening files with :e. Its called the wildmenu. Add the following lines to your .vimrc. As a side note it will also give completion options for vim commands.

<pre class="brush: bash; title: ; notranslate" title="">set wildmenu
set wildignore+=*.pyc,*.zip,*.gz,*.bz,*.tar,*.jpg,*.png,*.gif,*.avi,*.wmv,*.ogg,*.mp3,*.mov
</pre>

**Code Snippets**
  
The vim snippy plugin provides textmate like code snippets. Its pretty darn cool. Installing is hard. Download the latest version from [here][9]. Be sure to download both snippy\_plugin.vba and snippy\_bundles.vba as the plugin and snippets are now seperated. Create a directory .vim/after/ftplugin and put both .vba files in there. I installed them by opening them with vim using the full path to the .vba files and then typing :source % to source the file. The vim ball script will install and you will be ready to go. Open a .py file and type def<tab>. You can tab through each <{}> and fill in the content to construct your function.

**Extra functional goodness like block comment**

Operating on blocks of code is handy. Being able to comment out an entire section with a few keystrokes saves much time. [This vim script][10] provides that functionality. I download it and save it to .vim/ftplugin/python_fn.vim.  Then you can visually select a block of code with ]v and comment it out with ]c and move its indentation level with ]< and ]> as well as a few other things.

**PEP8 Goodness**

Adding the following to .vim/ftplugin/python_pep8.vim will help you with tab space and other such worries with pep8.

<pre class="brush: bash; title: ; notranslate" title="">setlocal tabstop=4
setlocal softtabstop=4
setlocal shiftwidth=4
setlocal textwidth=79
setlocal smarttab
setlocal expandtab
setlocal smartindent
</pre>

**One last note**
  
Make sure indent and plugins are turned on in your .vimrc

<pre class="brush: bash; title: ; notranslate" title="">filetype plugin indent on
</pre>

 [1]: http://www.vim.org/scripts/script.php?script_id=974
 [2]: http://www.cmdln.org/wp-content/uploads/2008/10/python.vim
 [3]: http://blog.sontek.net
 [4]: http://www.cmdln.org/wp-content/uploads/2008/10/python_exec_block.vim
 [5]: http://www.cmdln.org/wp-content/uploads/2008/10/python_ipdb.vim
 [6]: http://www.reddit.com/user/fboender/
 [7]: http://www.reddit.com/r/Python/comments/785vt/vim_customization_for_python/
 [8]: http://www.vim.org/scripts/script.php?script_id=1788
 [9]: http://www.vim.org/scripts/script.php?script_id=1318
 [10]: http://www.vim.org/scripts/script.php?script_id=30