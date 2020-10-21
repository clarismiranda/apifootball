# Useful library for API-football.

## Environmental Vars
export AF_HOST="api-football-beta.p.rapidapi.com"\
export AF_KEY=""\
export DIR_NAME="../PCA/"

## Files Structure
```bash
├── PCA
│   ├── DE
│   │   └── 78
│   │       ├── 2016
│   │       │   ├── 157
│   │       │   │   ├── 157_34.json
│   │       │   │   ├── away
│   │       │   │   │   ├── 16718_33.json
│   │       │   │   │   ├── 16734_31.json
│   │       │   │   │   ├── 16752_29.json
│   │       │   │   │   ├── 16773_27.json
│   │       │   │   │   ├── 16786_25.json
│   │       │   │   │   ├── 16809_23.json
│   │       │   │   │   ├── 16829_21.json
│   │       │   │   │   ├── 16835_20.json
│   │       │   │   │   ├── 16856_18.json
│   │       │   │   │   ├── 16866_17.json
│   │       │   │   │   ├── 16877_15.json
│   │       │   │   │   ├── 16902_13.json
│   │       │   │   │   ├── 16914_11.json
│   │       │   │   │   ├── 16933_9.json
│   │       │   │   │   ├── 16953_7.json
│   │       │   │   │   ├── 16973_5.json
│   │       │   │   │   └── 17001_2.json
│   │       │   │   └── home
│   │       │   │       ├── 16706_34.json
│   │       │   │       ├── 16726_32.json
│   │       │   │       ├── 16744_30.json
│   │       │   │       ├── 16761_28.json
│   │       │   │       ├── 16780_26.json
```

## Team Standings
This saves the current standings in a league, if the league is already over saves the last week.\
python fteam_stats.py --country --league --season --main
```bash
python fteam_stats.py DE 78 2016 true\
```
> Note: use true if it is the first time the standings are retrieved.

## Automate Team Standings
Here are several team standings commands of different leagues to be executed by one command.\
.\fteam_stats.sh --season --main
```bash
./fteam_stats.sh 2016 true
```
> Note: first mark the file as executable by running:
```bash 
chmod +x fteam_stats.sh
```

## Fixtures Stats
This saves all the fixtures of a league from a start date in format YY-MM-DD to an end date.\
python ffixtures_stats.py --country --league --season --start --end
```bash
python ffixtures_stats.py DE 78 2016 2016-08-26 2017-05-20
```
> Note: for knowing the start and end of the season use: \
python league.py --country --season

## Automate Fixtures Stats
Here are several fixtures statistics commands of different leagues to be executed by one command.\
.\ffixtures_stats.sh --season --end --start
```bash
./ffixtures_stats.sh 2016 2016-08-26 2017-05-20
```
> Note: first mark the file as executable by running:
```bash 
chmod +x ffixtures_stats.sh
```

## Next Fixtures
This ouputs a list of team's ids pairs, which are the teams' fixtures home and away teams in a given period of time.\
python ffixtures_future.py --country --league --season --start --end
```bash
python ffixtures_future.py DE 78 2016 2016-08-26 2016-08-30
```
