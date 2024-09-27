# Simple Historic Weather Data Analytics
# Python with Kaggle API
# pip install kaggle
# needed libraries:
# pip install pyarrow fastparquet
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

# Filter data for the last 5 years
start_date = '2003-01-01'
end_date = '2023-09-05'
filtered_df = daily_weather[(daily_weather['date'] >= start_date) & (daily_weather['date'] <= end_date)]

# Create separate DataFrames for rain, snow, and wind, including temperature information
rain_df = filtered_df[['station_id', 'city_name', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'precipitation_mm']]
snow_df = filtered_df[['station_id', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'snow_depth_mm']]
wind_df = filtered_df[['station_id', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'avg_wind_dir_deg', 'avg_wind_speed_kmh', 'peak_wind_gust_kmh']]

# Save each DataFrame to a separate CSV file
rain_df.to_csv('./output/rain_data.csv', index=False)
snow_df.to_csv('./output/snow_data.csv', index=False)
wind_df.to_csv('./output/wind_data.csv', index=False)

print("CSV files for rain, snow, and wind data (with temperature and wind direction) have been created successfully.")

#filtered_df.to_csv('./output/weather_data.csv', index=False)