#!/bin/bash
# sends GET request to URL and displays response body
curl -sfL "$1" -X GET
