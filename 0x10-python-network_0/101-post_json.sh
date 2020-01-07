#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
curl -sH "Content-Type: application/json" --request POST --data @"$2" "$1"
