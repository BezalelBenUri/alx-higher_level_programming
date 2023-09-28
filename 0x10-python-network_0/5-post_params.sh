#!/bin/bash
# Script sends POST to URL
curl -sX POST -d "email=test@gmail.com.com&subject=I will always be here for PLD" "$1"
