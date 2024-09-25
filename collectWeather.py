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

# Aggregate data by avg/month
daily_weather['year_month'] = daily_weather['date'].dt.to_period('M')
monthly_data = daily_weather.groupby('year_month').agg({
    'avg_temp_c': 'mean',
    'min_temp_c': 'mean',
    'max_temp_c': 'mean',
    'precipitation_mm': 'sum',  # Total precipitation per month
    'avg_wind_speed_kmh': 'mean',  # Average wind speed per month
    'peak_wind_gust_kmh': 'max'  # Maximum wind gust per month
}).reset_index()

# Aggregate data by year
daily_weather['year'] = daily_weather['date'].dt.year
yearly_data = daily_weather.groupby('year').agg({
    'avg_temp_c': 'mean',
    'min_temp_c': 'mean',
    'max_temp_c': 'mean',
    'precipitation_mm': 'sum',  # Total precipitation per year
    'avg_wind_speed_kmh': 'mean',  # Average wind speed per year
    'peak_wind_gust_kmh': 'max'  # Maximum wind gust per year
}).reset_index()

# Convert year_month back to datetime for better handling in Tableau
monthly_data['year_month'] = monthly_data['year_month'].dt.to_timestamp()

# Write the yearly data to a CSV file
yearly_data.to_csv('./output/yearly_data.csv', index=False)

# Write the monthly data to a CSV file
monthly_data.to_csv('./output/monthly_data.csv', index=False)