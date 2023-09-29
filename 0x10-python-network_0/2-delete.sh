#!/bin/bash
#sends a DELETE request to the URL passed as the first argument and displays the body of the response

# -s = Silent mode. Don't show progress meter or error messages.
# X = specifies the request method - DELETE
curl -sX DELETE "$1"
