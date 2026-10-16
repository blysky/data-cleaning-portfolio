# Weather Pipeline

A small Python pipeline that fetches hourly temperatures for Toronto from the
[Open-Meteo API](https://open-meteo.com/), averages them by day with pandas,
and saves the result to PostgreSQL.

## Steps
1. Fetch 7 days of hourly temperatures (JSON)
2. Convert to a pandas DataFrame
3. Group by day and average
4. Save to a PostgreSQL table, `daily_temperature`

## Requirements
- Python 3.x
- Docker Desktop
- `pip install requests pandas sqlalchemy psycopg2-binary`

## Setup

Start a PostgreSQL container:

```
docker run -d --name pg-weather -e POSTGRES_PASSWORD=<your-password> -p 5433:5432 postgres:16
docker exec pg-weather psql -U postgres -c "CREATE DATABASE weather_practice;"
```

Set the password for your terminal session:

```
$env:DB_PASSWORD="<your-password>"
```

## Run

```
python fetch_weather.py
```

Check the result:

```
docker exec pg-weather psql -U postgres -d weather_practice -c "SELECT * FROM daily_temperature;"
```