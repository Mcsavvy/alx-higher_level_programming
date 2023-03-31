#!/bin/bash
curl -b "email=test@gmail.com&subject=I will always be here for PLD" -sX POST "$1"
