# Weather pipeline

I wanted to practise connecting Python to a database, so I wrote a small script
that fetches hourly temperatures for Toronto from the Open-Meteo API, averages them
by day with pandas, and saves the result to PostgreSQL.

The script reads the database password from an environment variable instead of
the file, so it needs that set before it runs.

The database runs in Docker. Getting Docker to start was the hardest part, because
WSL and virtualization had to be turned on first. The steps below are the ones that
worked for me.

# Running it

This uses the PostgreSQL container from the telecom project, which listens on port 5433: