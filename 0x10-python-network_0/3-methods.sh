#!/bin/bash
# curl to display all HTTP methods server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
