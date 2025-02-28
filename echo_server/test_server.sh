#!/bin/bash
curl -X POST 'http://0.0.0.0:8200/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "echo-model",
    "messages": [
      {
        "role": "user",
        "content": "Hello, World!"
      }
    ]
}'