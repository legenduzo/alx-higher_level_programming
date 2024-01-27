#!/bin/bash
# Catch me
curl -vLX PUT -H "Origin:School" -d "user_id=98" "43e2c31a6dc8.32fbd0b4.alx-cod.online:5000/catch_me" | grep -o 'You got me!'
