#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response

# -s = Silent mode. Don't show progress meter or error messages.
# -L = Follow redirects in URL
curl -sL "$1"
