#!/bin/bash
#script that Display header variable X-School-User-Id to 98
curl -s -X GET "$1" -L -b "X-School-User-Id: 98"
