#!/bin/bash
url="$1"
curl -sI $url | grep -i Content-length |awk '{print $2}'
