# Simple Historic Weather Data Analytics Gui
# https://creativepolymath.github.io/

# Python with Kaggle API
# pip install kaggle
# needed libraries:
# pip install tk pyarrow fastparquet
# Data collected from:
# kaggle datasets download -d guillemservera/global-daily-climate-data

# FIRST RUN 'python collectWeather.py'
# This makes the data less memory intensive
# and I'm learning so it's the only way
# I could make it work, for now.

# setup Python environment
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import pandas as pd
import os
import traceback

"""
    Main function to initialize and run the Historical Weather Data GUI application.
    This function performs the following steps:
    1. Loads the necessary data.
    2. Runs diagnostics on the loaded data.
    3. Creates the main GUI window with input fields and buttons.
    4. Starts the GUI event loop.
    """

def main():
    global root, city_entry, start_date_entry, end_date_entry, daily_weather, cities

    try:
        # Load data
        if not load_data():
            print("Failed to load data. Exiting.")
            return

        # Run diagnostics to view data types and column info
        #diagnose_data()

        # Create the main window
        root = tk.Tk()
        root.title("Historical Weather Data GUI")

        # Create and pack the widgets
        ttk.Label(root, text="City:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        # Handle mixed data types in city names
        city_names = cities['city_name'].astype(str)
        city_names = city_names[city_names != 'nan'].unique()  # Remove 'nan' strings
        city_names = sorted(city_names)
        
        city_entry = ttk.Combobox(root, values=city_names)
        city_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        start_date_entry = ttk.Entry(root)
        start_date_entry.grid(row=1, column=1, padx=5, pady=5)
        start_date_entry.insert(0, "2003-01-01")  # Default start date

        ttk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        end_date_entry = ttk.Entry(root)
        end_date_entry.grid(row=2, column=1, padx=5, pady=5)
        end_date_entry.insert(0, "2023-09-05")  # Default end date

        generate_button = ttk.Button(root, text="Generate CSV", command=generate_csv)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Start the GUI event loop
        root.mainloop()

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Traceback:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()