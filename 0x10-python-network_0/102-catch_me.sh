#!/bin/bash
# Catch me
curl -sL "43e2c31a6dc8.32fbd0b4.alx-cod.online:5000/catch_me" | sed '$a\You got me!' | grep -o 'You got me!'
