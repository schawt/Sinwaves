#!/usr/bin/env python
import cgitb
cgitb.enable()

#cgi common gateway interface

print 'Content-Type: image/png'
#print 'Content-Type: text/html'
print
#print '<h1>Hello!</h1>'
print file(r"/home/aa/ugrad/sjwilson/public_html/firefox.png", "rb").read()

