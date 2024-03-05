import xml.etree.ElementTree as ET
import shapefile
from pyproj import Proj, transform

# Define the input KML file and the output shapefile
kml_file = 'LEHD_data/Healthline.kml'
shapefile_name = 'LEHD_data/HealthLine.shp'

# Parse the KML file
tree = ET.parse(kml_file)
root = tree.getroot()

# Define the shapefile
w = shapefile.Writer(shapefile_name, shapeType=shapefile.POLYLINE)
w.field('name', 'C')

# Define the coordinate systems
in_proj = Proj(init='epsg:4326')  # WGS84
out_proj = Proj(init='epsg:3857')  # Web Mercator

# Iterate through Placemark elements and extract coordinates
for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
    name = placemark.find('{http://www.opengis.net/kml/2.2}name').text
    line_string = placemark.find('.//{http://www.opengis.net/kml/2.2}LineString')
    if line_string is not None:
        coords_text = line_string.find('{http://www.opengis.net/kml/2.2}coordinates').text
        coords = [tuple(map(float, c.split(','))) for c in coords_text.strip().split()]
        transformed_coords = [transform(in_proj, out_proj, lon, lat) for lon, lat in coords]
        w.line([transformed_coords])
        w.record(name)

# Save the shapefile
w.close()
