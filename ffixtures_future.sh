#!/bin/bash

echo "Season: $1"
echo "From: $2"
echo "To: $3"

python ffixtures_future.py GB 39 $1 $2 $3
python ffixtures_future.py ES 140 $1 $2 $3
python ffixtures_future.py DE 78 $1 $2 $3
python ffixtures_future.py IT 135 $1 $2 $3
python ffixtures_future.py FR 61 $1 $2 $3
python ffixtures_future.py NL 88 $1 $2 $3
python ffixtures_future.py PT 94 $1 $2 $3
python ffixtures_future.py BE 144 $1 $2 $3