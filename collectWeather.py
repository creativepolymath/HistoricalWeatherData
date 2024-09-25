# Simple Historic Weather Data Analytics
# Python with Kaggle API
# Data collected from:
# kaggle datasets download -d guillemservera/global-daily-climate-data

#setup python env
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

countries = pd.read_csv("./CSV/global-daily-climate-data/countries.csv")
cities = pd.read_csv("./CSV/global-daily-climate-data/cities.csv")


# Read Parquet Files (code from Kaggle:guillemservera)
daily_weather = pd.read_parquet("./CSV/global-daily-climate-data/daily_weather.parquet")


# Convert the date column to datetime
daily_weather['date'] = pd.to_datetime(daily_weather['date'])

# Filter data for the last 20 years
start_date = '2003-01-01'
end_date = '2023-09-05'
filtered_df = daily_weather[(daily_weather['date'] >= start_date) & (daily_weather['date'] <= end_date)]

filtered_df.to_csv('./output/weather_data.csv', index=False)