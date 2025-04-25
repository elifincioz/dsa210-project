import pandas as pd

# Read data
accidents = pd.read_csv("data/accidents_istanbul.csv")
weather = pd.read_csv("data/weather_istanbul.csv")

# Drop duplicates
accidents.drop_duplicates(inplace=True)

# Handle missing weather data with time-based interpolation
weather['temperature'] = weather['temperature'].interpolate(method='time')
weather['precipitation'] = weather['precipitation'].interpolate(method='time')

# Convert date columns to datetime
accidents['date'] = pd.to_datetime(accidents['date'])
weather['date'] = pd.to_datetime(weather['date'])

# Merge datasets
merged = pd.merge(accidents, weather, on='date', how='inner')
merged.to_csv("merged_data.csv", index=False)
