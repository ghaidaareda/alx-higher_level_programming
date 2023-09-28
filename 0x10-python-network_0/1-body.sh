#!/bin/bash
#script that Display only body of a 200 status code response
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

curl -s -X GET "$1" -o /dev/null -w "%{http_code}":wq
 | grep -q 200 && curl -s "$1"
