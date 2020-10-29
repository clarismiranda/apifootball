#!/bin/bash

echo "Season: $1"
echo "From: $2"
echo "To: $3"

python ffixtures_stats.py GB 39 $1 $2 $3
python ffixtures_stats.py ES 140 $1 $2 $3
python ffixtures_stats.py DE 78 $1 $2 $3
python ffixtures_stats.py IT 135 $1 $2 $3
python ffixtures_stats.py FR 61 $1 $2 $3
python ffixtures_stats.py NL 88 $1 $2 $3
python ffixtures_stats.py PT 94 $1 $2 $3
python ffixtures_stats.py BE 144 $1 $2 $3