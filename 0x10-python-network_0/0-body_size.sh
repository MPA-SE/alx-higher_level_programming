#!/bin/bash
# ends request to that URL displays size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
