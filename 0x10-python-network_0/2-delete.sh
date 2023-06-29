#!/bin/bash
# sends DELETE request to $1 URL and displays response body
curl -s "$1" -X DELETE
