---
title: New bundle to manage routes for RedHat/CentOS with CFEngine 3
author: Nick Anderson
type: post
date: 2012-02-19T04:55:27+00:00
url: /2012/02/18/new-bundle-to-manage-routes-for-redhatcentos-with-cfengine-3/
categories:
  - Posts
tags:
  - centos
  - CFEngine
  - example
  - redhat
  - routing
  - sysadmin

---
<img class="alignleft" src="http://farm4.staticflickr.com/3435/3388655598_42e5832466_m.jpg" alt="" width="240" height="160" />I re-factored rh\_add\_interface\_routes into a new bundle rh\_update_routes, you can find them in [my CFEngine library][1].

The biggest improvement is you no longer have to specify the interface you want the route on. Instead you specify a regular expression of the ip that would be on that interface and the specific interface is found.

Second major improvement is the direct use of ip route del/add to update currently running system instead of restarting all networking.

Also a small change in the declaration of the routes that is less repetitive and requires less typing.

Take care in crafting your ip regular expression especially if you are not using a standard A, B or C class network.

Now lets see how it could be used.

Consider that you have multiple interfaces on a host, one interface connects to a &#8220;management&#8221; network, another connects to an application network, and another connects to a database network. Your default route is for the application network because you need to talk to the rest of the world.

Now consider what other networks that your host might need to connect to for &#8220;management&#8221;. Maybe you have a network that your backup servers sit on, and maybe you have another network that is for vpn clients, and you want vpn clients to be able to ssh to this host on the management interface.

We don&#8217;t need to add any routes for the db network or for the application network but for these other two networks we have to add the routes on the host.

172.16.208.0/25 is the network your backup servers sit on. 192.168.5.0/24 is your vpn client access network. Your management network on the host we are considering is 192.168.35.0/24.

You could define a common bundle to define these variables.

<pre class="brush: plain; title: ; notranslate" title="">bundle common site {

vars:
ipv4_192_168_35::
"mgmt_ip_regex"
string  =&gt; "192\.168\.35\..*",
comment =&gt; "Regex to match the ip that is on the management network, we use this
to figure out which is the management interface";

"mgmt_routes[172.16.208.0/25]"
string  =&gt; "192.168.35.254",
comment =&gt; "Needed to talk to the backup servers over the management network";

"mgmt_routes[192.168.5.0/24]"
string  =&gt; "192.168.35.254",
comment =&gt; "Needed to talk to vpn clients on the vpn client network";

}

</pre>

This is how you would call the rh\_update\_routes bundle.

<pre class="brush: plain; title: ; notranslate" title="">bundle agent main{

methods:
"routing"       usebundle   =&gt; rh_update_routes("$(site.mgmt_ip_regex)", "site.mgmt_routes"),
comment =&gt; "Setup Management routes defined in bundle common site";

}

</pre>

Lets walk through the decision tree a little bit. In bundle common site mgmt\_ip\_regex and mgmt\_routes is only defined if the client matches the class ipv4\_192\_168\_35. We wouldn&#8217;t want to define the same routes for a host on the 192.168.5.0 network because the gateway would be wrong, so that&#8217;s why you need to be careful to restrict your variable definition based on classes.

The mgmt\_ip\_regex is needed to dynamically determine which interface these routes will apply to. And really we only need the interface for this so that we can update the proper file for persistent routes (in redhat|centos its /etc/sysconfig/network-scripts/route-interfacename).

Lets look at rh\_update\_routes to see what&#8217;s going on.

<pre class="brush: plain; title: ; notranslate" title="">bundle agent rh_update_routes(ipregex, routes) {
# Expects string, array
# Note: This bundle depricates rh_add_interface_routes. I see no good reason to continue using it.
#
# ipregex is a regular expression that matches the ip on the interface you want these routes added
#   hint: ipregex should match an ip that can communicate with the specified gateway
#         for example if your routing a network via 192.168.0.1 and the network is a /24 network
#         (255.255.255.0 netmask) then you should have an ip in the range 192.168.0.1-254 on the
#         host your trying to add this route on. So a regex of 192\.168\.0\.[0-9]++ would work.
# routes is an array keyed on the network you want to route to with the string value being the gateway to use.
#
# NOTE: Unfortunately the only way I could think of to automatically determine the interface a route
#       needs added for is to use regcmp to compare the ipregex to the array of addresses. It would be
#       better if there was some way to use the iprange function to determine which nic an ipaddress
#       is on, but that does not currently work, or I am thus far to dense to figure out how.
#       So right now I am stuck with using ugly ipaddress regular expressions which can be error prone
#       in construction especially when you start networks that dont fall into octet boundaries
#
#       This causes there to be a limitation of usage on this bundle, you MUST NOT MIX
#       routes that go on seperate interfaces in the same route configuration array. I believe
#       this limitation could be surpassed if we could use the iprange or similar function.
#
# vars:
#    "ipregex_mgmt" string =&gt; "192\.168\.0\.[0-9]++";
#    "management[CIDRNETWORK]"
#        string =&gt; "GATEWAY",
#        comment =&gt; "What do you need this for";
#
#    "management[10.119.156.0/26]"
#        string =&gt; "192.168.0.1",
#        comment =&gt; "Needed for talking to the special network used for backup servers";
#
# methods:
#    "any" usebundle =&gt; rh_add_routes("192\.168\.0\.[0-9]++", "context.management");
#
    vars:
        "nics"          slist =&gt; getindices("sys.ipv4");
        #"route_file"    string =&gt; "/etc/sysconfig/network-scripts/route-$(interface)";
        "route_index" slist =&gt; getindices("$(routes)");

    classes:
        "supported_os" or =&gt; { "centos_5", "redhat_5" };

        "$(nics)_matches_ipregex" expression    =&gt; regcmp("$(ipregex)", "$(sys.ipv4[$(nics)])"),
            comment =&gt; "Determine which network interface has an ip that we are adding routes for.
                        We need to know this so that we can insert the route in the proper
                        file for reboot persistence.";

    files:
        (centos_5|redhat_5)::
            "/etc/sysconfig/network-scripts/route-$(nics)"
                create      =&gt; "true",
                perms       =&gt; mog("644", "root", "root"),
                edit_line   =&gt; replace_or_add("$(route_index).*", "$(route_index) via $($(this.routes)[$(route_index)])"),
                classes     =&gt; if_repaired("persistent_route_updated_for_$(route_index)"),
                ifvarclass  =&gt; "$(nics)_matches_ipregex",
                comment     =&gt; "Replace any conflicting routes and ensure persistent across reboots";

    commands:
        # We only attempt to delete a route if we have modified the persistent route file
        "/sbin/ip route del $(route_index)"
            ifvarclass  =&gt; canonify("persistent_route_updated_for_$(route_index)"),
            classes     =&gt; "attempted_route_removal_for_$(route_index)",
            comment     =&gt; "Delete any possibly conflicting old route before adding the new one";

        # We only attempt to add a route if we have modified the persistent route file
        "/sbin/ip route add $(route_index) via $($(routes)[$(route_index)])"
            ifvarclass  =&gt; canonify("persistent_route_updated_for_$(route_index)"),
            classes     =&gt; "attempted_route_addition_for_$(route_index)",
            comment     =&gt; "Add the new route";

    reports:
        cfengine::
            "Persistent route updated for $(route_index) via $($(routes)[$(route_index)]) on dev $(nics)"
                ifvarclass =&gt; canonify("persistent_route_updated_for_$(route_index)");

        !supported_os::
            "Sorry I don't know how to work with this OS";

}
</pre>

First we get a list of the interfaces on the system using getindices on sys.ipv4. Then we get a list of networks to route for from the configuration array that we passed into the bundle. Next we use the ipregex that we passed into the bundle and we iterate over the network interfaces looking for a match. When a match is found it defines the class $(nics)\_matches\_ipregex where nics expands to the current iterated nic from the list we built earlier. Thanks to Diego for this pattern. [I found it][2] in [his upcoming book Learning CFEngine 3][3], if you haven&#8217;t you should go get a copy. The pre-release is available now, and even in its early stage I recommend it.

Now we get to some actual action. In the files section we edit the interface file for the current iterated value of $(nics) but only if we have a match on the regex &#8220;$(nics)\_matches\_ipregex&#8221; and we replace any routes for the same network  with the desired route entry or add it if one does not exist using the replace\_or\_add edit_line bundle from the standard library. If we made any repairs to the file we define the class `persistent_route_updated_for_$(route_index)` which is used to control when the commands promises are made.

In the commands section we first delete  any route for a matching network. This command may fail if there is no matching route but that&#8217;s ok. It&#8217;s far easier to implement delete add than to account for the current routing table to avoid the possible unnecessary delete and use replace in stead. (that being said I welcome patches)

Finally we just report if we have made any updates.

I think we are lacking in explained useful examples so I hope someone finds this useful. Any suggestions for improvements or additions are welcome.

UPDATE: 2.19.2012

I had an omission in the bundle, I forgot to restrict the files edit on the $(nics)\_matches\_ipregex class, It caused every interface to have the specified routes added so please use the updated bundle.

 [1]: https://github.com/nickanderson/nickanderson-cfengine-library/blob/master/lib_rh.cf
 [2]: http://cf-learn.info/code/ch04/edit_inittab_tso.cf.html
 [3]: http://cf-learn.info/