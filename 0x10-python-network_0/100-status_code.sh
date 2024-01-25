#!/bin/bash
# Returns status code
curl -sw '%{http_code}' -o /dev/null "$1"
