# Useful library for API-football.

## Environmental Vars
export AF_HOST="api-football-beta.p.rapidapi.com"\
export AF_KEY=""\
export DIR_NAME="../PCA/"

## Team Standings
python fteam_stats.py --country --league --season --main\
python fteam_stats.py MX 262 2020 true

## Fixtures Stats
python ffixtures_stats.py --country --league --season --start --end\
python ffixtures_stats.py MX 262 2020 2020-08-14 2020-08-18

## Next Fixtures
python ffixtures_stats.py --country --league --season --start --end\
python ffixtures_future.py MX 262 2020 2020-08-21 2020-08-25
