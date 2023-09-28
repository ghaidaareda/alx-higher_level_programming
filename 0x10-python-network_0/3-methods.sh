#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument 
curl -s -X OPTIONS -i "$1" | grep "ALLOWS:"
