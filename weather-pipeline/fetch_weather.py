import requests
import pandas as pd
from sqlalchemy import create_engine, text

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 43.65, "longitude": -79.38, "hourly": "temperature_2m"}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    hourly = data["hourly"]
    df = pd.DataFrame({
        "time": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
    })
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = df["time"].dt.date
    daily_avg = df.groupby("date")["temperature_c"].mean().round(1)
    print(daily_avg)

    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5433/weather_practice")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connected:", result.scalar())

    daily_avg.to_frame().to_sql("daily_temperature", engine, if_exists="replace")
    print("Saved to daily_temperature")

except requests.exceptions.Timeout:
    print("The website took too long to reply. Try again later.")