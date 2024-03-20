import pandas as pd
import geopandas as gpd

############################## Merge LEHD with Shape file for Blocks ###############################
#         This file merges the LEHD jobs data with the US Census block shape file                  #
#         to create a new csv file that can be used for QGIS analysis                              #
#                                                                                                  #
#        The h_geocode column is made using the definition:                                        #
#        h_geocode = SSCCCTTTTTTBBBB                                                               #
#        where SS is the state FIPS code, CCD is the county FIPS code, TTTTTT is the tract code,   #
#        and BBBB is  the block code                                                               #
#                                                                                                  #
#         Author: John McCormick                                                                   #
#         Date: March 2024                                                                         #
#                                                                                                  #
####################################################################################################


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



