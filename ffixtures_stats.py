"""
	Retrieves all fixtures stats and saves them into folder
"""

from api.apifootball import APIFootball, Client, CustomEncoder
from datetime import datetime, date
import json
import os
import sys

if len(sys.argv) > 3:
	# Setting league and season from system arguments
	country = sys.argv[1]
	league = sys.argv[2]
	season = sys.argv[3]
	start = sys.argv[4]
	end = sys.argv[5]
else:
    print("Wrong arguments were given, expected: --country --league --season --start --end")

dirName = os.getenv('DIR_NAME') + country
# Teams file
teams_json = dirName + '/teams.json'

# Saving directory
dirName = dirName + '/' + league + '/' + season

# Retrieve key and host from terminal
api_key = os.getenv('AF_KEY')
api_host = os.getenv('AF_HOST')

cl = Client(api_key, api_host)
# Creates the client to the api with a country and season
af_cl = APIFootball(cl, country, season)

# Retrieving all matches in the league
matches, _ = af_cl.get_fixtures(league, frm=start, to=end)

# Future matches dictionary
dct_future = {}
dct_teams = None

# Check if both teams belong to principal league
with open(teams_json) as json_file:
		dct_teams = json.load(json_file)

for k, v in matches.items():
	match_id = str(k)
	week = str(v.week)
	week = ''.join(filter(str.isdigit, week))
	home_team = str(v.team_home.id)
	away_team = str(v.team_away.id)
	if home_team in dct_teams and away_team in dct_teams:
		# Directory where to save
		temp_home = dirName + '/' + home_team + '/home'
		temp_away = dirName + '/' + away_team + '/away'
		# Gets statistics from a match
		statistics, _ = af_cl.get_statistics(match_id)
		match = v
		try:
			match.stats_home = statistics[home_team]
			match.stats_away = statistics[away_team]
		except:
			# Dictionary for saving future matches
			dct_future[match_id] = {
				"home_id" : home_team,
				"away_id" : away_team
			}
		# Save finish standings into a json  
		json_object = json.dumps(match, indent = 4, cls=CustomEncoder)
		# Saving into file
		file_home = temp_home + '/' + match_id + "_" + week + ".json"
		file_away = temp_away + '/' + match_id + "_" + week + ".json"
		with open(file_home, "w") as outfile: 
			outfile.write(json_object)
		with open(file_away, "w") as outfile: 
			outfile.write(json_object)

# Path for saving future games
file_future = dirName + '/'+ "next.json"
# Writting future games into a file
with open(file_future) as outfile:
	outfile.write(dct_future)