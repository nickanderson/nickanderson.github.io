---
title: Setup encfs on dropbox for boxcryptor with CFEngine
author: Nick Anderson
type: post
date: 2012-02-27T20:19:39+00:00
url: /2012/02/27/setup-encfs-on-dropbox-for-boxcryptor-with-cfengine/
categories:
  - Posts
tags:
  - boxcryptor
  - CFEngine
  - dropbox
  - encfs
  - sysadmin
  - ubuntu

---
[<img class="alignleft size-thumbnail wp-image-982" title="Selection_001" src="http://www.cmdln.org/images/wp-content/uploads/2012/02/Selection_001-150x150.png" alt="" width="150" height="150" />][1]Here is an easy way to configure <a href="http://www.arg0.net/encfs" target="_blank">encfs</a> with <a href="http://db.tt/REX1m3Zv" target="_blank">dropbox</a> that is compatible with boxcryptor. <a href="http://www.boxcryptor.com/" target="_blank">Boxcryptor</a> makes [Windows][2], [Mac][3] [Android][4], and [IOS][5] applications to assist you in accessing data that you have stored in encfs. They do require that you create your encfs with some <a href="https://boxcryptorsupport.uservoice.com/knowledgebase/articles/35105-can-boxcryptor-mount-encrypted-volumes-created-wit" target="_blank">specific options</a>: Cipher algorithm: AES, Plaintext or Stream encrypted filenames, No filename initialization vector chaining, No per-file initialization vectors, No external IV chaining, No block MAC headers, No per-block random bytes.

I thought it would be fun to write a <a href="http://cfengine.com/" target="_blank">CFEngine</a> policy to set it up so here it is. Just install CFEngine 3, configure your settings in the policy file and kick it off with cf-agent -KIf ~/.cfagent/inputs/boxcryptor\_dropbox\_encfs. (You will need the standard library, and the policy is classed for ubuntu, but it should be easy enough to add support for another distro).

<div class="gistem">
  <div id="gist-1926615" class="gist">
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
  &nbsp;&nbsp;&nbsp;&nbsp;bundlesequence  =&gt; {
</div>

<div class='line' id='LC4'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"main",
</div>

<div class='line' id='LC5'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};
</div>

<div class='line' id='LC6'>
  <br />
</div>

<div class='line' id='LC7'>
  &nbsp;&nbsp;&nbsp;&nbsp;inputs          =&gt; {
</div>

<div class='line' id='LC8'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"cfengine_stdlib.cf",
</div>

<div class='line' id='LC9'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};
</div>

<div class='line' id='LC10'>
  }
</div>

<div class='line' id='LC11'>
  <br />
</div>

<div class='line' id='LC12'>
  bundle agent main {
</div>

<div class='line' id='LC13'>
  # Setup encfs on one of your dropbox folders for use with boxcryptor
</div>

<div class='line' id='LC14'>
  &nbsp;&nbsp;&nbsp;&nbsp;vars:
</div>

<div class='line' id='LC15'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"settings[user]"      string =&gt; "user";
</div>

<div class='line' id='LC16'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"settings[group]"     string =&gt; "group";
</div>

<div class='line' id='LC17'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"settings[encfs]"     string =&gt; "/home/user/Dropbox/encfs";
</div>

<div class='line' id='LC18'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"settings[mount]"     string =&gt; "/home/user/Documents/Safe";
</div>

<div class='line' id='LC19'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"settings[password]"  string =&gt; "supersecret";
</div>

<div class='line' id='LC20'>
  <br />
</div>

<div class='line' id='LC21'>
  &nbsp;&nbsp;&nbsp;&nbsp;methods:
</div>

<div class='line' id='LC22'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"required_software" 
</div>

<div class='line' id='LC23'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usebundle   =&gt; install_boxcryptor,
</div>

<div class='line' id='LC24'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action      =&gt; if_elapsed("360"),
</div>

<div class='line' id='LC25'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "Install software to work with boxcryptor, but only
</div>

<div class='line' id='LC26'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;verify and try once every 6 hours";
</div>

<div class='line' id='LC27'>
  <br />
</div>

<div class='line' id='LC28'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encfs" 
</div>

<div class='line' id='LC29'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usebundle =&gt; encfs_init_boxcryptor("main.settings"),
</div>

<div class='line' id='LC30'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment   =&gt; "If no encfs is found, initalize one compatible with boxcryptor";
</div>

<div class='line' id='LC31'>
  <br />
</div>

<div class='line' id='LC32'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encfs" 
</div>

<div class='line' id='LC33'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usebundle =&gt; encfs_mounted("main.settings"),
</div>

<div class='line' id='LC34'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Ensure the encfs is mounted somewhere we can write to it";
</div>

<div class='line' id='LC35'>
  }
</div>

<div class='line' id='LC36'>
  <br />
</div>

<div class='line' id='LC37'>
  bundle agent install_boxcryptor{
</div>

<div class='line' id='LC38'>
  # This is just a meta to make sure the deps for boxcryptor are all installed
</div>

<div class='line' id='LC39'>
  <br />
</div>

<div class='line' id='LC40'>
  &nbsp;&nbsp;&nbsp;&nbsp;packages:
</div>

<div class='line' id='LC41'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC42'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"python-pexpect"
</div>

<div class='line' id='LC43'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_policy  =&gt; "add",
</div>

<div class='line' id='LC44'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_method  =&gt; apt,
</div>

<div class='line' id='LC45'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment         =&gt; "python-expect is needed for the custom 
</div>

<div class='line' id='LC46'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scripts to initalize and mount encfs";
</div>

<div class='line' id='LC47'>
  <br />
</div>

<div class='line' id='LC48'>
  &nbsp;&nbsp;&nbsp;&nbsp;methods:
</div>

<div class='line' id='LC49'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# would be nice to find a dropbox fuse implimentation that works so we
</div>

<div class='line' id='LC50'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# dont have to rely on the nautilus dropbox plugin and thus be able to 
</div>

<div class='line' id='LC51'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# this on a headless machine
</div>

<div class='line' id='LC52'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#"dropbox"    usebundle =&gt; install_dropfuse;
</div>

<div class='line' id='LC53'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dropbox" 
</div>

<div class='line' id='LC54'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usebundle =&gt; install_dropbox;
</div>

<div class='line' id='LC55'>
  <br />
</div>

<div class='line' id='LC56'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encryption" 
</div>

<div class='line' id='LC57'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usebundle =&gt; install_encfs;
</div>

<div class='line' id='LC58'>
  }
</div>

<div class='line' id='LC59'>
  <br />
</div>

<div class='line' id='LC60'>
  bundle agent encfs_init_boxcryptor(config){
</div>

<div class='line' id='LC61'>
  <br />
</div>

<div class='line' id='LC62'>
  &nbsp;vars:
</div>

<div class='line' id='LC63'>
  &nbsp;&nbsp;&nbsp;&nbsp;"temp_script"
</div>

<div class='line' id='LC64'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string =&gt; "/tmp/init_boxcryptor_encfs.py";
</div>

<div class='line' id='LC65'>
  <br />
</div>

<div class='line' id='LC66'>
  &nbsp;&nbsp;&nbsp;&nbsp;"init_boxcryptor_encfs_template" 
</div>

<div class='line' id='LC67'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "boxcryptor only supports a subset of encfs options, 
</div>

<div class='line' id='LC68'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this script initalizes an encfs filesystem with those 
</div>

<div class='line' id='LC69'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;options. Its an interactive process so we needed expect.",
</div>

<div class='line' id='LC70'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string =&gt; "#!/usr/bin/env python
</div>

<div class='line' id='LC71'>
  # encoding: utf-8
</div>

<div class='line' id='LC72'>
  <br />
</div>

<div class='line' id='LC73'>
  import pexpect
</div>

<div class='line' id='LC74'>
  import sys
</div>

<div class='line' id='LC75'>
  <br />
</div>

<div class='line' id='LC76'>
  child = pexpect.spawn(&#39;encfs $($(config)[encfs]) $($(config)[mount])&#39;)
</div>

<div class='line' id='LC77'>
  child.logfile = sys.stdout
</div>

<div class='line' id='LC78'>
  child.expect(&#39;&gt;&#39;)
</div>

<div class='line' id='LC79'>
  child.sendline(&#39;x&#39;)
</div>

<div class='line' id='LC80'>
  child.expect(&#39;The following cipher algorithms are available&#39;)
</div>

<div class='line' id='LC81'>
  child.sendline(&#39;1&#39;)
</div>

<div class='line' id='LC82'>
  child.expect(&#39;Selected key size&#39;)
</div>

<div class='line' id='LC83'>
  child.sendline(&#39;256&#39;)
</div>

<div class='line' id='LC84'>
  child.expect(&#39;filesystem block size&#39;)
</div>

<div class='line' id='LC85'>
  child.sendline(&#39;1024&#39;)
</div>

<div class='line' id='LC86'>
  child.expect(&#39;The following filename encoding algorithms are available&#39;)
</div>

<div class='line' id='LC87'>
  child.sendline(&#39;3&#39;)
</div>

<div class='line' id='LC88'>
  child.expect(&#39;Enable filename initialization vector chaining&#39;)
</div>

<div class='line' id='LC89'>
  child.sendline(&#39;n&#39;)
</div>

<div class='line' id='LC90'>
  child.expect(&#39;Enable per-file initialization vectors&#39;)
</div>

<div class='line' id='LC91'>
  child.sendline(&#39;n&#39;)
</div>

<div class='line' id='LC92'>
  child.expect(&#39;Enable block authentication code headers&#39;)
</div>

<div class='line' id='LC93'>
  child.sendline(&#39;n&#39;)
</div>

<div class='line' id='LC94'>
  child.expect(&#39;Add random bytes to each block header&#39;)
</div>

<div class='line' id='LC95'>
  child.sendline(&#39;0&#39;)
</div>

<div class='line' id='LC96'>
  child.expect(&#39;Enable file-hole pass-through&#39;)
</div>

<div class='line' id='LC97'>
  child.sendline(&#39;y&#39;)
</div>

<div class='line' id='LC98'>
  child.expect(&#39;New Encfs Password&#39;)
</div>

<div class='line' id='LC99'>
  child.sendline(&#39;$($(config)[password])&#39;)
</div>

<div class='line' id='LC100'>
  child.expect(&#39;Verify Encfs Password&#39;)
</div>

<div class='line' id='LC101'>
  child.sendline(&#39;$($(config)[password])&#39;)
</div>

<div class='line' id='LC102'>
  child.expect(pexpect.EOF, timeout=None)
</div>

<div class='line' id='LC103'>
  child.close()
</div>

<div class='line' id='LC104'>
  sys.exit(child.exitstatus)";
</div>

<div class='line' id='LC105'>
  <br />
</div>

<div class='line' id='LC106'>
  &nbsp;&nbsp;&nbsp;&nbsp;classes:
</div>

<div class='line' id='LC107'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encfs_exists" 
</div>

<div class='line' id='LC108'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression  =&gt; fileexists("$($(config)[encfs])/.encfs6.xml"),
</div>

<div class='line' id='LC109'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "Determine if there is an existing encfs";
</div>

<div class='line' id='LC110'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"mount_exists"  
</div>

<div class='line' id='LC111'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression  =&gt; isdir("$($(config)[mount])"),
</div>

<div class='line' id='LC112'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "Make sure there is a place to mount the encfs";
</div>

<div class='line' id='LC113'>
  &nbsp;
</div>

<div class='line' id='LC114'>
  &nbsp;files:
</div>

<div class='line' id='LC115'>
  &nbsp;&nbsp;&nbsp;!encfs_exists::
</div>

<div class='line' id='LC116'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$($(config)[mount])/."
</div>

<div class='line' id='LC117'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;create =&gt; "true",
</div>

<div class='line' id='LC118'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perms =&gt; mog("700", "$($(config)[user])", "$($(config)[group])"),
</div>

<div class='line' id='LC119'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Make sure that there is a place to mount the encfs";
</div>

<div class='line' id='LC120'>
  <br />
</div>

<div class='line' id='LC121'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)"
</div>

<div class='line' id='LC122'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;create =&gt; "true",
</div>

<div class='line' id='LC123'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perms =&gt; mog("700", "$($(config)[user])", "$($(config)[group])"),
</div>

<div class='line' id='LC124'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit_line =&gt; append_if_no_line("$(init_boxcryptor_encfs_template)"),
</div>

<div class='line' id='LC125'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit_defaults =&gt; empty,
</div>

<div class='line' id='LC126'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes =&gt; if_repaired("script_installed"),
</div>

<div class='line' id='LC127'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "If no encfs filesystem is found place the initalization script
</div>

<div class='line' id='LC128'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;so we can execute it.";
</div>

<div class='line' id='LC129'>
  <br />
</div>

<div class='line' id='LC130'>
  &nbsp;&nbsp;&nbsp;&nbsp;encfs_exists::
</div>

<div class='line' id='LC131'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)"
</div>

<div class='line' id='LC132'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delete =&gt; tidy,
</div>

<div class='line' id='LC133'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes =&gt; if_repaired("performed_cleanup"),
</div>

<div class='line' id='LC134'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Delete the temporary initalization script if an encfs already exists";
</div>

<div class='line' id='LC135'>
  <br />
</div>

<div class='line' id='LC136'>
  &nbsp;&nbsp;&nbsp;&nbsp;commands:
</div>

<div class='line' id='LC137'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!(encfs_exists|initalized_boxcryptor_encfs)::
</div>

<div class='line' id='LC138'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)",
</div>

<div class='line' id='LC139'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contain =&gt; setuidgid_silent("$($(config)[user])", "$($(config)[group])"),
</div>

<div class='line' id='LC140'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes =&gt; "initalized_boxcryptor_encfs",
</div>

<div class='line' id='LC141'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "If no encfs is detected and we havent yet successfully initalized
</div>

<div class='line' id='LC142'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;one fire the expect script to do so.";
</div>

<div class='line' id='LC143'>
  <br />
</div>

<div class='line' id='LC144'>
  &nbsp;&nbsp;&nbsp;&nbsp;reports:
</div>

<div class='line' id='LC145'>
  <br />
</div>

<div class='line' id='LC146'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script_installed::
</div>

<div class='line' id='LC147'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_initalize: I installed a script to do my work";
</div>

<div class='line' id='LC148'>
  <br />
</div>

<div class='line' id='LC149'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initalized_boxcryptor_encfs::
</div>

<div class='line' id='LC150'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_initalize: I couldn&#39;t find an existing encfs at $($(config)[encfs]) so I initalized one";
</div>

<div class='line' id='LC151'>
  <br />
</div>

<div class='line' id='LC152'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;performed_cleanup::
</div>

<div class='line' id='LC153'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_initalize: I cleaned up after myself";
</div>

<div class='line' id='LC154'>
  <br />
</div>

<div class='line' id='LC155'>
  <br />
</div>

<div class='line' id='LC156'>
  }
</div>

<div class='line' id='LC157'>
  <br />
</div>

<div class='line' id='LC158'>
  bundle agent encfs_mounted(config){
</div>

<div class='line' id='LC159'>
  &nbsp;&nbsp;&nbsp;&nbsp;vars:
</div>

<div class='line' id='LC160'>
  &nbsp;&nbsp;&nbsp;&nbsp;"temp_script"
</div>

<div class='line' id='LC161'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Mounting an encfs filesystem requires a password, this script uses expect so we can supply one interactively",
</div>

<div class='line' id='LC162'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string =&gt; "/tmp/mount_encfs.py";
</div>

<div class='line' id='LC163'>
  <br />
</div>

<div class='line' id='LC164'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"mount_encfs_tpl" string =&gt; "#!/usr/bin/env python
</div>

<div class='line' id='LC165'>
  # encoding: utf-8
</div>

<div class='line' id='LC166'>
  <br />
</div>

<div class='line' id='LC167'>
  import pexpect
</div>

<div class='line' id='LC168'>
  import sys
</div>

<div class='line' id='LC169'>
  <br />
</div>

<div class='line' id='LC170'>
  child = pexpect.spawn(&#39;/usr/bin/encfs $($(config)[encfs]) $($(config)[mount])&#39;)
</div>

<div class='line' id='LC171'>
  <br />
</div>

<div class='line' id='LC172'>
  child.logfile = sys.stdout
</div>

<div class='line' id='LC173'>
  child.expect(&#39;EncFS Password&#39;)
</div>

<div class='line' id='LC174'>
  child.sendline(&#39;$($(config)[password])&#39;)
</div>

<div class='line' id='LC175'>
  child.expect(pexpect.EOF, timeout=None)
</div>

<div class='line' id='LC176'>
  child.close()
</div>

<div class='line' id='LC177'>
  sys.exit(child.exitstatus)";
</div>

<div class='line' id='LC178'>
  <br />
</div>

<div class='line' id='LC179'>
  &nbsp;&nbsp;&nbsp;&nbsp;classes:
</div>

<div class='line' id='LC180'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encfs_mounted" 
</div>

<div class='line' id='LC181'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression  =&gt; returnszero("/bin/grep --silent -P ^encfs\s$($(config)[mount]) /etc/mtab", "noshell"),
</div>

<div class='line' id='LC182'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "Determine if the encfs filesystem is currently mounted or not"; 
</div>

<div class='line' id='LC183'>
  <br />
</div>

<div class='line' id='LC184'>
  &nbsp;&nbsp;&nbsp;&nbsp;files:
</div>

<div class='line' id='LC185'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!encfs_mounted::
</div>

<div class='line' id='LC186'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)"
</div>

<div class='line' id='LC187'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;create          =&gt; "true",
</div>

<div class='line' id='LC188'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perms           =&gt; mog("700", "$($(config)[user])", "$($(config)[group])"),
</div>

<div class='line' id='LC189'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit_line       =&gt; append_if_no_line("$(mount_encfs_tpl)"),
</div>

<div class='line' id='LC190'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit_defaults   =&gt; empty,
</div>

<div class='line' id='LC191'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes         =&gt; if_repaired("placed_script"),
</div>

<div class='line' id='LC192'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment         =&gt; "If we dont detect that our desired encfs filesystem is mounted
</div>

<div class='line' id='LC193'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop the expect script in place. We use the expect script
</div>

<div class='line' id='LC194'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;because we need to provide a password";
</div>

<div class='line' id='LC195'>
  <br />
</div>

<div class='line' id='LC196'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encfs_mounted::
</div>

<div class='line' id='LC197'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)"
</div>

<div class='line' id='LC198'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delete  =&gt; tidy,
</div>

<div class='line' id='LC199'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes =&gt; if_repaired("performed_cleanup"),
</div>

<div class='line' id='LC200'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "If the encfs filesystem is mounted we have no need for the mount script to be in place, delete it";
</div>

<div class='line' id='LC201'>
  <br />
</div>

<div class='line' id='LC202'>
  &nbsp;&nbsp;&nbsp;&nbsp;commands:
</div>

<div class='line' id='LC203'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!encfs_mounted::
</div>

<div class='line' id='LC204'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(temp_script)",
</div>

<div class='line' id='LC205'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contain =&gt; setuidgid_silent("$($(config)[user])", "$($(config)[group])"),
</div>

<div class='line' id='LC206'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes =&gt; if_else("repaired_mount", "failed_repair_mount"),
</div>

<div class='line' id='LC207'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "If the enfcs filesystem is not mounted execute our mount script";
</div>

<div class='line' id='LC208'>
  <br />
</div>

<div class='line' id='LC209'>
  &nbsp;&nbsp;&nbsp;&nbsp;reports:
</div>

<div class='line' id='LC210'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;placed_script::
</div>

<div class='line' id='LC211'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_mounted: I installed a script";
</div>

<div class='line' id='LC212'>
  <br />
</div>

<div class='line' id='LC213'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repaired_mount::
</div>

<div class='line' id='LC214'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_mounted: $($(config)[encfs]) was not mounted on $($(config)[mount]), but we fixed it";
</div>

<div class='line' id='LC215'>
  <br />
</div>

<div class='line' id='LC216'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;performed_cleanup::
</div>

<div class='line' id='LC217'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_mounted: I cleaned up aftermyself";
</div>

<div class='line' id='LC218'>
  <br />
</div>

<div class='line' id='LC219'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!encfs_mounted.failed_repair_mount::
</div>

<div class='line' id='LC220'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_mounted: I dunno what happened, but I couldnt mount the encfs volume check your settings!";
</div>

<div class='line' id='LC221'>
  <br />
</div>

<div class='line' id='LC222'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!repaired_mount.encfs_mounted::
</div>

<div class='line' id='LC223'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boxcryptor_mounted: Everything was as expected";
</div>

<div class='line' id='LC224'>
  &nbsp;
</div>

<div class='line' id='LC225'>
  }
</div>

<div class='line' id='LC226'>
  <br />
</div>

<div class='line' id='LC227'>
  <br />
</div>

<div class='line' id='LC228'>
  <br />
</div>

<div class='line' id='LC229'>
  <br />
</div>

<div class='line' id='LC230'>
  bundle agent install_dropbox{
</div>

<div class='line' id='LC231'>
  &nbsp;&nbsp;&nbsp;&nbsp;vars:
</div>

<div class='line' id='LC232'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC233'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"packages"  slist =&gt; { "nautilus-dropbox" };
</div>

<div class='line' id='LC234'>
  <br />
</div>

<div class='line' id='LC235'>
  &nbsp;&nbsp;&nbsp;&nbsp;packages:
</div>

<div class='line' id='LC236'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC237'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(packages)"
</div>

<div class='line' id='LC238'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_policy  =&gt; "add",
</div>

<div class='line' id='LC239'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_method  =&gt; apt,
</div>

<div class='line' id='LC240'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment         =&gt; "Install dropbox packages with apt";
</div>

<div class='line' id='LC241'>
  <br />
</div>

<div class='line' id='LC242'>
  }
</div>

<div class='line' id='LC243'>
  <br />
</div>

<div class='line' id='LC244'>
  bundle agent install_encfs {
</div>

<div class='line' id='LC245'>
  # Install encfs
</div>

<div class='line' id='LC246'>
  &nbsp;&nbsp;&nbsp;&nbsp;vars:
</div>

<div class='line' id='LC247'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC248'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"packages" slist =&gt; { "encfs", "fuse-utils" };
</div>

<div class='line' id='LC249'>
  &nbsp;
</div>

<div class='line' id='LC250'>
  &nbsp;&nbsp;&nbsp;&nbsp;packages:
</div>

<div class='line' id='LC251'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC252'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(packages)"
</div>

<div class='line' id='LC253'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_policy  =&gt; "add",
</div>

<div class='line' id='LC254'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_method  =&gt; apt,
</div>

<div class='line' id='LC255'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment         =&gt; "Install encfs with apt";
</div>

<div class='line' id='LC256'>
  &nbsp;&nbsp;&nbsp;&nbsp;
</div>

<div class='line' id='LC257'>
  }
</div>

<div class='line' id='LC258'>
  <br />
</div>

<div class='line' id='LC259'>
  ###########################################################################
</div>

<div class='line' id='LC260'>
  #                               body parts                                #
</div>

<div class='line' id='LC261'>
  ###########################################################################
</div>

<div class='line' id='LC262'>
  <br />
</div>

<div class='line' id='LC263'>
  body contain setuidgid_silent(x,y){
</div>

<div class='line' id='LC264'>
  &nbsp;&nbsp;&nbsp;&nbsp;exec_owner =&gt; "$(x)";
</div>

<div class='line' id='LC265'>
  &nbsp;&nbsp;&nbsp;&nbsp;exec_group =&gt; "$(y)";
</div>

<div class='line' id='LC266'>
  &nbsp;&nbsp;&nbsp;&nbsp;no_output =&gt; "true";
</div>

<div class='line' id='LC267'>
  }
</div>

<div class='line' id='LC268'>
  <br />
</div>

<div class='line' id='LC269'>
  <br />
</div>

<div class='line' id='LC270'>
  <br />
</div>

<div class='line' id='LC271'>
  ###########################################################################
</div>

<div class='line' id='LC272'>
  #                            Not really useful                            #
</div>

<div class='line' id='LC273'>
  ###########################################################################
</div>

<div class='line' id='LC274'>
  # I couldnt get dropfuse to work, nor did I try very hard
</div>

<div class='line' id='LC275'>
  bundle agent install_dropfuse{
</div>

<div class='line' id='LC276'>
  &nbsp;&nbsp;&nbsp;&nbsp;vars:
</div>

<div class='line' id='LC277'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dropfuse_src" 
</div>

<div class='line' id='LC278'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string =&gt; "https://raw.github.com/arekzb/dropfuse/master/dropfuse.py",
</div>

<div class='line' id='LC279'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Location to get dropfuse binary from since its not packaged";
</div>

<div class='line' id='LC280'>
  <br />
</div>

<div class='line' id='LC281'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dropfuse_bin"
</div>

<div class='line' id='LC282'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string  =&gt; "/usr/local/bin/dropfuse.py",
</div>

<div class='line' id='LC283'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Location to install the dropfuse library";
</div>

<div class='line' id='LC284'>
  &nbsp;&nbsp;&nbsp;&nbsp;
</div>

<div class='line' id='LC285'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC286'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# TODO: find out if fuse-utils is really required for this
</div>

<div class='line' id='LC287'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"packages" 
</div>

<div class='line' id='LC288'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;slist   =&gt; { "fuse-utils", "python-fuse" },
</div>

<div class='line' id='LC289'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Packages required";
</div>

<div class='line' id='LC290'>
  <br />
</div>

<div class='line' id='LC291'>
  &nbsp;&nbsp;&nbsp;&nbsp;files:
</div>

<div class='line' id='LC292'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(dropfuse_bin)"
</div>

<div class='line' id='LC293'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perms       =&gt; mog("755", "root", "root"),
</div>

<div class='line' id='LC294'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ifvarclass  =&gt; "dropfuse_installed",
</div>

<div class='line' id='LC295'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "If dropfuse is installed ensure that 
</div>

<div class='line' id='LC296'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it is executable";
</div>

<div class='line' id='LC297'>
  &nbsp;&nbsp;&nbsp;&nbsp;packages:
</div>

<div class='line' id='LC298'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ubuntu::
</div>

<div class='line' id='LC299'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"$(packages)"
</div>

<div class='line' id='LC300'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_policy =&gt; "add",
</div>

<div class='line' id='LC301'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_method =&gt; apt, 
</div>

<div class='line' id='LC302'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment        =&gt; "Install the selected package with apt if
</div>

<div class='line' id='LC303'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;its not installed";
</div>

<div class='line' id='LC304'>
  &nbsp;&nbsp;&nbsp;&nbsp;classes:
</div>

<div class='line' id='LC305'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dropfuse_installed" 
</div>

<div class='line' id='LC306'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression  =&gt; fileexists("$(dropfuse_bin)"),
</div>

<div class='line' id='LC307'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment     =&gt; "Determine if the dropfuse binary is installed";
</div>

<div class='line' id='LC308'>
  <br />
</div>

<div class='line' id='LC309'>
  &nbsp;&nbsp;&nbsp;&nbsp;commands:
</div>

<div class='line' id='LC310'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!dropfuse_installed::
</div>

<div class='line' id='LC311'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"/usr/bin/wget $(dropfuse_src) -O $(dropfuse_bin)",
</div>

<div class='line' id='LC312'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment =&gt; "Install the dropfuse binary, its not currently 
</div>

<div class='line' id='LC313'>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;packaged so just get it from the authors github account";
</div>

<div class='line' id='LC314'>
  <br />
</div>

<div class='line' id='LC315'>
  }
</div>

<div class='line' id='LC316'>
  <br />
</div>

<div class='line' id='LC317'>
  <br />
</div>

<div class='line' id='LC318'>
  <br />
</div></pre>
        </div>
      </div>
      
      <div class="gist-meta">
        <a href="https://gist.github.com/raw/1926615/944c7cce07e27a0ea69a5af92d04d92b9a038024/boxcryptor_dropbox_encfs.cf" style="float:right;">view raw</a> <a href="https://gist.github.com/1926615#file_boxcryptor_dropbox_encfs.cf" style="float:right;margin-right:10px;color:#666">boxcryptor_dropbox_encfs.cf</a> <a href="https://gist.github.com/1926615">This Gist</a> is brought to you using <a href="http://en.bainternet.info/2011/simple-gist-embed"><small>Simple Gist Embed</small></a>.
      </div>
    </div>
  </div>
</div>

&nbsp;

edit: February 27, 2012 at 2:52 pm

Thanks @highdraw for pointing out the mac installer.

 [1]: http://www.cmdln.org/images/wp-content/uploads/2012/02/Selection_001.png
 [2]: http://www.boxcryptor.com/download/#platform_win_dl
 [3]: http://blog.boxcryptor.com/encfs-174-installer-for-mac-os-x-available
 [4]: https://market.android.com/details?id=com.boxcryptor.android
 [5]: http://itunes.apple.com/us/app/boxcryptor/id484546808