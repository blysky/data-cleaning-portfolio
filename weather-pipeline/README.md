# Weather pipeline

I wanted to practise connecting Python to a database, so I wrote a small script
that fetches hourly temperatures for Toronto from the Open-Meteo API, averages them
by day with pandas, and saves the result to PostgreSQL.

The script reads the database password from an environment variable instead of
the file, so it needs that set before it runs.

The database runs in Docker. Getting Docker to start was the hardest part, because
WSL and virtualization had to be turned on first. The steps below are the ones that
worked for me.

Running it

Start a PostgreSQL container on port 5433, so it doesn't clash with the telecom
database on 5432:

```
docker run -d --name pg-weather -e POSTGRES_PASSWORD=postgres -p 5433:5432 postgres:16
docker exec pg-weather psql -U postgres -c "CREATE DATABASE weather_practice;"
```

Then, in the same PowerShell window:

```
$env:DB_PASSWORD="postgres"
pip install requests pandas sqlalchemy psycopg2-binary
python fetch_weather.py
```

The script prints the daily averages and saves them to a table called
`daily_temperature`. To check the table:

```
docker exec pg-weather psql -U postgres -d weather_practice -c "SELECT * FROM daily_temperature;"
```

You should see seven rows, one per day. The numbers change from run to run because
the forecast updates.

What is next

I'd like to run this on a schedule so it collects a new forecast every day, probably
with Airflow. For now it only runs when I start it by hand.