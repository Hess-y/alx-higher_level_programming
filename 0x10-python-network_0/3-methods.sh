#!/bin/bash
# Bash script that takes in URL & displays all HTTP methods server will accept.
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " - f 2-
