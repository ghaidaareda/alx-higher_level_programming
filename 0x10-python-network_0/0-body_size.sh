#!/bin/bash
#script that takes in a URL, sends a request to it & displays the response size in bytes
echo "$(curl -sS "$url"| wc -c)"
