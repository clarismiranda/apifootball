"""
	Retrieves all team stats and saves them into folder
"""

from api.apifootball import APIFootball, Client, CustomEncoder
import json
import os
import sys

if len(sys.argv) > 3:
	# Setting country, league and season from system arguments
	# Main is a boolean to represent this league as principal
    country = sys.argv[1]
    league = sys.argv[2]
    season = sys.argv[3]
    main = sys.argv[4]
else:
    print("Wrong arguments were given, expected: --country --league --season --main")

dirName = os.getenv('DIR_NAME') + country 

# Saving directory
dirName = dirName + '/' + league + '/' + season

# Teams file
teams_json = dirName + '/teams.json'

# Teams dictionary
dct_teams = None

# Retrieve key and host from terminal
api_key = os.getenv('AF_KEY')
api_host = os.getenv('AF_HOST')

cl = Client(api_key, api_host)
# Creates the client to the api with a country and season
af_cl = APIFootball(cl, country, season)

if main == 'true':
	# Retrieving all teams in the league
	dct_teams, _ = af_cl.get_teams(league)
	# Save the teams when the league is principal
	teams_object = json.dumps(dct_teams, indent = 4, cls=CustomEncoder)
	with open(teams_json, "w") as outfile: 
		outfile.write(teams_object)
elif main == 'false':
	with open(teams_json) as json_file:
		dct_teams = json.load(json_file) 

# When is not a main league, just create the folders 
for k, v in dct_teams.items():
	team_id = str(k)
	# Creates directory if it doesn't exist
	temp = dirName + '/' + team_id
	try:
		# Create target Directory
		os.mkdir(temp)
		print("Directory " , temp ,  " Created ") 
		# Create home team target Directory
		try:
			temp_home = temp + '/home'
			os.mkdir(temp_home)
			print("Directory " , temp_home ,  " Created ") 
		except FileExistsError:
			print("Directory " , temp_home ,  " already exists")
		# Create away team target Directory
		try:
			temp_away = temp + '/away'
			os.mkdir(temp_away)
			print("Directory " , temp_away ,  " Created ") 
		except FileExistsError:
			print("Directory " , temp_away ,  " already exists")
	except FileExistsError:
		print("Directory " , temp ,  " already exists")

	# Saves current standings if the league is principal
	if main == 'true':
		# Retrieving stats from team with key
		home_stats, away_stats = af_cl.get_teams_stats(team=team_id, league=league, season=season)
		# Retrieving current standings from a league
		standings, _ = af_cl.get_standings(league)
		# Update team standings
		team = standings[team_id]
		team.stats_home = home_stats
		team.stats_away = away_stats
		# Save finish standings into a json  
		json_object = json.dumps(team, indent = 4, cls=CustomEncoder)
		# Games play
		week = home_stats.played + away_stats.played
		# Saving into file
		file = temp + '/' + team_id + '_' + str(week) + ".json"
		with open(file, "w") as outfile: 
			outfile.write(json_object)
		temp = dirName
