[Gsheet link](https://docs.google.com/spreadsheets/d/15UbmcRcw81TQvNrwvA7CpOxIqPkj93mX06xoC2js0r8/edit#gid=515309321)

## Pre-requisite
-  Assume postgres is installed if not, run:
```bash
brew install postgres
brew services start postgresql
```

## Setup Postgres Database
- RUN `export DATABASE_PATH=$(pwd)/amber/data/test_data.csv`
- RUN `make setup-database`

## Get output data
- Setup venv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- Run `python main.py` and output file will be in `/data/processed/dataset.csv`

## Cleaning in data before adding into `/data`
- Removed last column on csv
- Changed date format to `yyyy/mm/dd` except for `frmp` as it contains null to be ingested by postgres

### pre-commit
- This repo uses pre-commit to run pre-commit checks

#### Installation
- Run
```bash
brew install pre-commit
pre-commit install
```

## TODO
- Connecting to remote database
