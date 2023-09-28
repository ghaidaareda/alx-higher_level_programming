#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument 
curl -s -X OPTIONS "$1" -L
