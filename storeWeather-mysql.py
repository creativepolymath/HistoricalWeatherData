#not functional at this time. sorting out the database/table connection

import mysql.connector
import pandas as pd

# Load the dataset
rain_df = pd.read_csv('./output/rain_data.csv')
snow_df = pd.read_csv('./output/snow_data.csv')
wind_df = pd.read_csv('./output/wind_data.csv')

# Create separate DataFrames for rain, snow, and wind, including temperature information
rain_df = rain_df[['station_id', 'city_name', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'precipitation_mm']]
snow_df = snow_df[['station_id', 'city_name', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'snow_depth_mm']]
wind_df = wind_df[['station_id', 'city_name', 'date', 'avg_temp_c', 'min_temp_c', 'max_temp_c', 'avg_wind_dir_deg', 'avg_wind_speed_kmh', 'peak_wind_gust_kmh']]

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # replace with your MySQL username
    password='',  # replace with your MySQL password
    database='climate_data'  # replace with your database name
)

cursor = conn.cursor()

# Create tables for rain, snow, and wind data
cursor.execute("""
CREATE TABLE IF NOT EXISTS rain_data (
    station_id VARCHAR(255),
    city_name VARCHAR(255),
    date DATE,
    avg_temp_c FLOAT,
    min_temp_c FLOAT,
    max_temp_c FLOAT,
    precipitation_mm FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS snow_data (
    station_id VARCHAR(255),
    city_name VARCHAR(255),
    date DATE,
    avg_temp_c FLOAT,
    min_temp_c FLOAT,
    max_temp_c FLOAT,
    snow_depth_mm FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS wind_data (
    station_id VARCHAR(255),
    city_name VARCHAR(255),
    date DATE,
    avg_temp_c FLOAT,
    min_temp_c FLOAT,
    max_temp_c FLOAT,
    avg_wind_dir_deg FLOAT,
    avg_wind_speed_kmh FLOAT,
    peak_wind_gust_kmh FLOAT
)
""")

# Function to insert data into a table
def insert_data(table_name, data_frame):
    for _, row in data_frame.iterrows():
        cursor.execute(f"""
        INSERT INTO {table_name} (station_id, city_name, date, avg_temp_c, min_temp_c, max_temp_c, {', '.join(row.index[6:])})
        VALUES (%s, %s, %s, %s, %s, %s, {', '.join(['%s'] * (len(row) - 6))})
        """, tuple(row))

# Insert data into the tables
insert_data('rain_data', rain_df)
insert_data('snow_data', snow_df)
insert_data('wind_data', wind_df)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data has been successfully written to the MySQL database.")
