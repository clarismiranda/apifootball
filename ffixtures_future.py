"""
	Retrieves future fixtures' teams
"""

from api.apifootball import APIFootball, Client
from datetime import datetime, date
import json
import os
import sys

if len(sys.argv) > 5:
	# Setting country, league and season from system arguments
    country = sys.argv[1]
    league = sys.argv[2]
    season = sys.argv[3]
    start = sys.argv[4]
    end = sys.argv[5]
else:
    print("Wrong arguments were given, expected: --country --league --season --start --end")

# Retrieve key and host from terminal
api_key = os.getenv('AF_KEY')
api_host = os.getenv('AF_HOST')

# Where to save
dirName = '../PCA/' + country + '/' + league + '/'

cl = Client(api_key, api_host)
# Creates the client to the api with a country and season
af_cl = APIFootball(cl, country, season)
# Getting today's date
today = str(date.today())
# Retrieving all matches in the league
matches, _ = af_cl.get_fixtures(league, frm=start, to=end)

# Output array of pair of teams in future matches
future_teams = []
future_matches = {}
f_matches = []
for k, v in matches.items():
	match_id = str(k)
	home_team = int(v.team_home.id)
	away_team = int(v.team_away.id)
	future_teams.append([home_team, away_team])
	f_matches.append(int(match_id))
	future_matches[match_id] = [home_team, away_team]

print("Future teams %s:" % (country))
print(future_teams)
print(f_matches)