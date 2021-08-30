import folium
from folium.plugins import MiniMap
import pandas as pd
import webbrowser
import pathlib

# Creates the map using Folium
weather_radar_stations = folium.Map(location=[48, -102], zoom_start=4)
minimap = MiniMap()
minimap.add_to(weather_radar_stations)

# Provides toggleable option to enable the NWS nexrad cgi overlay from iastate.edu
folium.raster_layers.WmsTileLayer(
    url="http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi",
    name="NWS NEXRAD",
    fmt="image/png",
    layers="nexrad-n0r-900913",
    transparent=True,
    overlay=True,
    control=True,
    show=False
).add_to(weather_radar_stations)

folium.LayerControl().add_to(weather_radar_stations)

# Adds radar station markers for each location
weather_radars = pd.read_csv('assets/Weather_Radar_Stations.csv')
for i, row in weather_radars.iterrows():
    coords = [row[1], row[0]]
    site_name = row[4]
    radar_type = row[5]
    folium.Marker(coords, popup=radar_type, tooltip=site_name).add_to(weather_radar_stations)
    print(coords)

# Saves and open the map
weather_radar_stations.save(outfile='weather-radar-stations.html')
file_path = pathlib.Path('weather-radar-stations.html').absolute()
url = 'file://' + str(file_path)
webbrowser.open(url, new=2)  # open in new tab

exit()
