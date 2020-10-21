#!/bin/bash

echo "Season: $1"
echo "First time created: $2"

python fteam_stats.py GB 39 $1 $2
python fteam_stats.py ES 140 $1 $2
python fteam_stats.py DE 78 $1 $2
python fteam_stats.py IT 135 $1 $2