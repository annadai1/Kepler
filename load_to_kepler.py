import pandas as pd
from keplergl import KeplerGl

# Define the path to the CSV file
file_path = '2013-data_copy.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Create a Kepler.gl map
map_1 = KeplerGl(height=600)

# Add the DataFrame to the Kepler.gl map
map_1.add_data(data=df, name="CSV Data")

# Save the map as an HTML file
map_1.save_to_html(file_name='kepler_map.html')

# Optionally, display the map (if running in an interactive environment)
# map_1
