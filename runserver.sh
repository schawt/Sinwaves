#!/bin/bash
echo "http://loopback:8000/"
python -c "import CGIHTTPServer;CGIHTTPServer.test()"
