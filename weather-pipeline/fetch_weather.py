import os

import pandas as pd
import requests
from sqlalchemy import create_engine, text

DB_PASSWORD = os.environ.get("DB_PASSWORD")
if not DB_PASSWORD:
    raise SystemExit("Set the DB_PASSWORD environment variable first.")

DB_URL = f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5433/weather_practice"

API_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {"latitude": 43.65, "longitude": -79.38, "hourly": "temperature_2m"}


def fetch_hourly_temperatures():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    hourly = response.json()["hourly"]
    return pd.DataFrame({
        "time": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
    })


def daily_averages(df):
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = df["time"].dt.date
    return df.groupby("date")["temperature_c"].mean().round(1)


def save_to_db(daily_avg, engine):
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    daily_avg.to_frame().to_sql("daily_temperature", engine, if_exists="replace")


def main():
    try:
        df = fetch_hourly_temperatures()
    except requests.exceptions.Timeout:
        print("The website took too long to reply. Try again later.")
        return

    daily_avg = daily_averages(df)
    print(daily_avg)

    engine = create_engine(DB_URL)
    save_to_db(daily_avg, engine)
    print("Saved to daily_temperature")


if __name__ == "__main__":
    main()