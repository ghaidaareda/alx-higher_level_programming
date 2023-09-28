#!/bin/bash
#script that Display only body of a 200 status code response
curl -X GET -w "%{stderr} {\"status\": \"%{http_code}\", \"body\":\"%{stdout}\"}" -s -o /dev/null "$1"
