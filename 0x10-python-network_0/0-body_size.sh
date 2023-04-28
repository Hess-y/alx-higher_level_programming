#!/bin/bash
<<<<<<< HEAD
# Bash script that takes in URL,displays the size of the body of the response.
=======
# Bash script that takes in a URL,displays the size of the body of the response.
>>>>>>> 8b4f4bf50a36a443c6fd8b80a9d119734acb6677
curl - sI "$1" | grep - i Content-Length | awk '{print $2}'
