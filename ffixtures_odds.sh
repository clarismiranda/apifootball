#!/bin/bash

echo "Season: $1"
echo "Date: $2"

python ffixtures_odds.py 39 $1 7 $2
python ffixtures_odds.py 140 $1 8 $2
python ffixtures_odds.py 78 $1 6 $2
python ffixtures_odds.py 135 $1 6 $2
python ffixtures_odds.py 61 $1 9 $2
python ffixtures_odds.py 88 $1 7 $2
python ffixtures_odds.py 94 $1 6 $2
python ffixtures_odds.py 144 $1 11 $2