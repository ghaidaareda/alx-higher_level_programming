#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument 
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
