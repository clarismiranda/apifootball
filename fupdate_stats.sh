#!/bin/bash
# Using path /Applications/MCC/Thesis/apifootball
# Updates stats

echo "Season: $1"
echo "From: $2"
echo "To: $3"

# Gets team standings
./fteam_stats.sh $1 true

# Gets fixtures
./ffixtures_stats.sh $1 $2 $3

# Move to directory
cd ../PCA/ES_V

# Creates stats and fixtures datasets
./maps_stats.sh $1 1