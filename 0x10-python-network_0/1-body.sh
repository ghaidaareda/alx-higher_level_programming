#!/bin/bash
#script that Display only body of a 200 status code response
curl -s -X GET "$1" -w "%http_code" | grep -q 200 && curl -s
