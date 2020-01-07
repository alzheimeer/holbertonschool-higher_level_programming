#!/bin/bash
# displays the size of the content in a header of the response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
