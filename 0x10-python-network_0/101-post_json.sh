#!/bin/bash
# sends JSON POST request to URL $! and displays response body
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
