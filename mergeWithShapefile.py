import pandas as pd
import geopandas as gpd

geo_frame = gpd.read_file("LEHD_data/U.S._Census_Blocks/Census_Blocks.shp")

data = pd.read_csv("LEHD_data/oh_rac_S000_JT00_2004_2013.csv")

data['h_geocode'] = data['h_geocode'].astype(str)
geo_frame.head()
geo_frame['STATE'] = geo_frame['STATE'].astype(str).str.zfill(2)  # State code is 2 digits
geo_frame['COUNTY'] = geo_frame['COUNTY'].astype(str).str.zfill(3)  # County codes are 3 digits
geo_frame['TRACT'] = geo_frame['TRACT'].astype(str).str.zfill(6)  # Tract codes are 6 digits
geo_frame['BLOCK'] = geo_frame['BLOCK'].astype(str).str.zfill(4)  # Block codes are 4 digits
geo_frame['h_geocode'] = (geo_frame['STATE']) + (geo_frame['COUNTY']) + (geo_frame['TRACT'])+ (geo_frame['BLOCK'])

mergedFrame = pd.merge(data, geo_frame, on = 'h_geocode', how='inner')
cuyahogaCounty = mergedFrame[mergedFrame['COUNTY'] == '035']

cuyahogaCounty.to_csv('LEHD_data/CuyahogaCountyRAC_SHP.csv', index=False)


