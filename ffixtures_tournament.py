"""
	Retrieves teams and fixtures of a multicountry league 
"""

from api.apifootball import APIFootball, Client, CustomEncoder
from datetime import datetime, date
import json
import os
import sys

"""
	Creates directories for a given team
"""
def create_home_away_directory(team_id, dirName):
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

"""
	Retrieves statistics from a match
"""
def saves_fixtures(match_id, home_team, away_team, dirName):
	# Directory where to save
	temp_home = dirName + '/' + home_team + '/home'
	temp_away = dirName + '/' + away_team + '/away'
	# Gets statistics from a match
	statistics, _ = af_cl.get_statistics(match_id)
	match = v
	match.stats_home = statistics[home_team]
	match.stats_away = statistics[away_team]
	season = str(match.season)
	# Save finish standings into a json  
	json_object = json.dumps(match, indent = 4, cls=CustomEncoder)
	# Saving into file
	file_home = temp_home + '/' + match_id + '_' + season + ".json"
	file_away = temp_away + '/' + match_id + '_' + season + ".json"
	with open(file_home, "w") as outfile: 
		outfile.write(json_object)
	with open(file_away, "w") as outfile: 
		outfile.write(json_object)

"""
	Retrieves standings of a team in a given season
"""
def saves_standings(team_id, season, dirName):
	# Retrieving stats from team with key
	home_stats, away_stats = af_cl.get_teams_stats(team_id, season=season)
	# Retrieving current standings from a league
	standings, _ = af_cl.get_standings(season=season)
	# Update team standings
	team = standings[team_id]
	team.stats_home = home_stats
	team.stats_away = away_stats
	# Save finish standings into a json  
	json_object = json.dumps(team, indent = 4, cls=CustomEncoder)
	# Games play
	week = home_stats.played + away_stats.played
	# Saving into file
	file = dirName + '/' + team_id + '/' + team_id + '_' + season + ".json"
	with open(file, "w") as outfile: 
		outfile.write(json_object)

if len(sys.argv) > 3:
	# Setting league and season from system arguments
	league = sys.argv[1]
	season = sys.argv[2]
	name = sys.argv[3]
	# Number of last maches h2h
	last = sys.argv[4]
	# Number of next matches to play
	nxt = sys.argv[5]
else:
    print("Wrong arguments were given, expected: --league --season --name --last --nxt")

dirName = os.getenv('DIR_NAME') + name

# Saving directory
dirName = dirName + '/' + league + '/' + season

# Retrieve key and host from terminal
api_key = os.getenv('AF_KEY')
api_host = os.getenv('AF_HOST')

cl = Client(api_key, api_host)
# Creates the client to the api with a country and season
af_cl = APIFootball(cl, season=season)

# Gets the future teams ids to play in the league
matches, _ = af_cl.get_fixtures(league, season, nxt=nxt)

for k, v in matches.items():
	match_id = str(k)
	home_team = str(v.team_home.id)
	away_team = str(v.team_away.id)
	# Creates folders for teams
	create_home_away_directory(home_team, dirName)
	create_home_away_directory(away_team, dirName)
	# Gets last N fixtures between these two teams
	historic_matches = af_cl.get_h2h(home_team, away_team, league, last=last)
	for k, v in historic_matches.items():
		match_id = str(k)
		home_team = str(v.team_home.id)
		away_team = str(v.team_away.id)
		saves_standings(home_team, v.season, dirName)
		saves_standings(away_team, v.season, dirName)
		saves_fixture(match_id, home_team, away_team, dirName)