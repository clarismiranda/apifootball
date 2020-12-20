"""
	Retrieves all odds and saves them into folder
"""
from api.apifootball import APIFootball, Client, CustomEncoder
from datetime import datetime, date
import json
import os
import sys

if len(sys.argv) > 4:
	# Setting league and season from system arguments
	league = sys.argv[1]
	season = sys.argv[2]
	week = sys.argv[3]
	date = sys.argv[4]
else:
    print("Wrong arguments were given, expected: --league --season --week --date")

# Retrieve key and host from terminal
api_key = os.getenv('AF_KEY')
api_host = os.getenv('AF_HOST')

dirName = os.getenv('DIR_NAME') + 'Odds'

# Saving directory
dirName = dirName + '/' + league + '/' + season

cl = Client(api_key, api_host)
# Creates the client to the api with a country and season
af_cl = APIFootball(cl)

# Identifies a date of the odd
if date is not 'None':
	date = date
else:
	date = None

# Retrieving all odds in the league
odds, _ = af_cl.get_odds(league, season, date=date)

for k, v in odds.items():
	match_id = str(k)
	# Save finish odds into a json  
	json_object = json.dumps(v, indent = 4, cls=CustomEncoder)
	# Adding week
	json_object = json.loads(json_object)
	json_object['week']= week
	json_object = json.dumps(json_object, indent = 4)
	# Saving into file
	file = dirName + '/' + match_id + '_' + week + ".json"
	with open(file, "w") as outfile: 
		outfile.write(json_object)