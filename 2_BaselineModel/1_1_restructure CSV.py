import os
import pandas as pd
import numpy as np
from math import radians, degrees, sin, cos, sqrt, atan2

# Constants
EARTH_RADIUS_NM = 3440.065  # Nautical miles

# Loxodrome distance and bearing calculations
def loxodrome_distance(lat1, lon1, lat2, lon2):
    """Calculate the loxodrome distance between two points in nautical miles."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    mean_lat = (lat1 + lat2) / 2
    distance = sqrt(dlat**2 + (dlon * cos(mean_lat))**2) * EARTH_RADIUS_NM
    return distance

def loxodrome_bearing(lat1, lon1, lat2, lon2):
    """Calculate the loxodrome bearing between two points in degrees."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    mean_lat = (lat1 + lat2) / 2
    bearing = atan2(dlon, dlat * cos(mean_lat))
    return (degrees(bearing) + 360) % 360

# Process files
input_folder = "time_sets_standardized"  # Replace with the path to your input folder
output_folder = "time_sets_postomov"  # Replace with the path to your output folder
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(input_folder, file)
        df = pd.read_csv(file_path)

        # Ensure data is sorted by timestamp
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df = df.sort_values('Timestamp')

        # Calculate DIR and SPD
        dirs = []
        spds = []
        for i in range(1, len(df)):
            lat1, lon1 = df.iloc[i - 1]['Latitude'], df.iloc[i - 1]['Longitude']
            lat2, lon2 = df.iloc[i]['Latitude'], df.iloc[i]['Longitude']
            time_diff = (df.iloc[i]['Timestamp'] - df.iloc[i - 1]['Timestamp']).total_seconds() / 3600  # in hours
            
            # Calculate speed and direction using loxodrome calculations
            distance = loxodrome_distance(lat1, lon1, lat2, lon2)
            dirs.append(loxodrome_bearing(lat1, lon1, lat2, lon2))
            spds.append(distance / time_diff if time_diff > 0 else 0)
        
        # Append NaN for the first row
        df['DIR'] = [np.nan] + dirs
        df['SPD'] = [np.nan] + spds

        # Save the processed file
        output_path = os.path.join(output_folder, file)
        df.to_csv(output_path, index=False)

print("Processing complete. Files saved to:", output_folder)
