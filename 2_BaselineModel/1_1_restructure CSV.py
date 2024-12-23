import os
import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2, degrees

# Constants
EARTH_RADIUS_NM = 3440.065  # Nautical miles

# Functions to calculate distance and bearing
def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points in nautical miles."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return EARTH_RADIUS_NM * c

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Calculate the initial bearing between two points."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    x = sin(dlon) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)
    initial_bearing = atan2(x, y)
    return (degrees(initial_bearing) + 360) % 360

# Process files
input_folder = "path/to/your/folder"
output_folder = "path/to/output/folder"
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
            
            # Calculate speed and direction
            distance = haversine(lat1, lon1, lat2, lon2)
            dirs.append(calculate_bearing(lat1, lon1, lat2, lon2))
            spds.append(distance / time_diff if time_diff > 0 else 0)
        
        # Append NaN for the first row
        df['DIR'] = [np.nan] + dirs
        df['SPD'] = [np.nan] + spds

        # Save the processed file
        output_path = os.path.join(output_folder, file)
        df.to_csv(output_path, index=False)

print("Processing complete. Files saved to:", output_folder)
