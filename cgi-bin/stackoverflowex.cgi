#!/usr/bin/env python

import cgitb; cgitb.enable()
import cgi
import os

""" from
http://stackoverflow.com/questions/5150591/is-it-possible-to-use-python-ajax-cgi-together
"""

print "Content-Type: text/html\n"

input_data   = cgi.FieldStorage()
print "hello"
