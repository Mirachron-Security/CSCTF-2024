#!/bin/bash

# Start Tor in the background
service tor start

# Start nginx in the foreground
nginx -g 'daemon off;'
