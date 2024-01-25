#!/bin/bash
# takes in a URL and displays all HTTP methods the server accepts
curl -sI "$1" | sed -n '/Allow: /s/Allow: //p'
