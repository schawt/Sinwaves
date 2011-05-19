#!/usr/bin/env python

"""
Used these for reference
http://lost-theory.org/python/dynamicimg.html
http://matplotlib.sourceforge.net/faq/howto_faq.html#matplotlib-in-a-web-application-server
"""

import sys

import cgi
import cgitb
cgitb.enable()

import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import numpy as np

import cStringIO

def main():
    form = cgi.FieldStorage()
    if 'frequency' in form:
        plotAGG(float(form['frequency'].value))
    else:
        print 'Content-type: text/html'
        print 
        print '<html><body>Test %s </body></html>' % "None"

def plotAGG(freq):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(-np.pi, np.pi, 201)
    ax.plot(x, np.sin(x*freq))
    ax.set_title('Sine Wave')
    ax.set_xlabel('Angle [rad]')
    ax.set_ylabel('sin(x)')
    #fig.savefig('test.png')
    #trying
    f = cStringIO.StringIO()
    fig.savefig(f, format='png')
    print 'Content-type: image/png'
    print
    f.seek(0)
    print f.read()

#tests
"""
import unittest

class Test1(unittest.TestCase):
    def test1(self):
        print "write tests here"
"""

if len(sys.argv) > 1 and sys.argv[1] == "--test":
    print
    # If we invoke with --test then we add a verbose and                       
    # pass the remaining arguments to unittest                                 
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[2:]
    unittest.main()
else:
    main ()


