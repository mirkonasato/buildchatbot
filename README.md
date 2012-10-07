buildchatbot
============

Python script to monitor Jenkins builds and notify a Skype chat.

Requirements
------------

* Python 2.7
* [Skype4Py](http://pypi.python.org/pypi/Skype4Py/)
* The Skype desktop app, running as the same user as this script
* HTTP access to the Jenkins server

Unlike the Jenkins
[Skype Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Skype+Plugin)
this script does not need to run on the same machine as Jenkins.

Configuration
-------------

Edit the top of the script setting your Jenkins URL and Skype chat name.

The chat name is the internal name used by Skype. To find it out run the
provided helper script that will display FriendlyName and Name of your
recent chats:

    python listrecentchats.py
    "Our project chat" -> "#myname/$abc123"
    "Some other chat" -> "#friendname/$xyz789"

License
-------

Released under the BSD 2-clause license; see LICENSE.txt.

