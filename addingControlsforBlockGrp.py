import pandas as pd
import numpy as np



############################# Merge with NHGIS ACS 5-year controls Data ############################
#         This script merged the full geographic jobs data with the manually computed              #
#         HealthLine access data and 5-year ACS demographic controls sourced from                  #
#         IPUMS NHGIS.                                                                             #
#                                                                                                  #
#         HealthLine access is defined below as any block group with more than 30% of its          #
#         block area being within 800m of the HealthLine.                                          #
#                                                                                                  #
#         All jobs data is normalized to the block group populations, and now is the percent of    #
#         the population that is employed in that category                                         #
#                                                                                                  #
#         Important Note: the percentages for job data, are not employment rate, it is percent     #
#         of the total population, NOT working population, that is employed in that category.      #
#                                                                                                  #
#         The final dataset is saved as a csv file.                                                #
#                                                                                                  #
#         Author: John McCormick                                                                   #
#         Date: March 20th, 2024                                                                   #
#                                                                                                  #
####################################################################################################



nhgis05_09 = pd.read_csv('nhgis_data/nhgis0003_ds195_20095_blck_grp.csv')
nhgis05_09['STATEA'] = nhgis05_09['STATEA'].astype(str).str.zfill(2)
nhgis05_09['COUNTYA'] = nhgis05_09['COUNTYA'].astype(str).str.zfill(3)
nhgis05_09['TRACTA'] = nhgis05_09['TRACTA'].astype(str).str.zfill(6)
nhgis05_09['BLKGRPA'] = nhgis05_09['BLKGRPA'].astype(str).str.zfill(1)

nhgis05_09['mergerRow']= nhgis05_09['STATEA'] + nhgis05_09['COUNTYA'] + nhgis05_09['TRACTA'] + nhgis05_09['BLKGRPA']



jobs = pd.read_csv('LEHD_data/FinalJobData.csv')

jobs['STATE_x'] = jobs['STATE_x'].astype(str).str.zfill(2)
jobs['COUNTY_x'] = jobs['COUNTY_x'].astype(str).str.zfill(3)
jobs['TRACT_x'] = jobs['TRACT_x'].astype(str).str.zfill(6)
jobs['BLKGRP_x'].value_counts()
jobs['BLKGRP_x'] = jobs['BLKGRP_x'].astype(str).str.zfill(1)
jobs['mergerRow'] = jobs['STATE_x'] + jobs['COUNTY_x'] + jobs['TRACT_x'] + jobs['BLKGRP_x']

jobs.drop(columns=['OBJECTID_x',
                    'AREALAND',
                    'AREAWATER',
                    'BASENAME',
                    'BLOCK_x',
                    'CENTLAT',
                    'CENTLON',
                    'FUNCSTAT',
                    'GEOID',
                    'INTPTLAT',
                    'INTPTLON',
                    'LSADC',
                    'LWBLKTYP',
                    'MTFCC',
                    'NAME',
                    'ObjID',
                    'SUFFIX',
                    'UR',
                    'HU100',
                    'POP100',
                    'SHAPE_Leng',
                    'SHAPE_Area',
                    'geometry',
                    'OBJECTID_y',
                    'BLKGRP_y',
                    'BLOCK_y',
                    'COUNTY_y',
                    'STATE_y',
                    'TRACT_y',
                    'Name',
                    'description',
                    'timestamp',
                    'begin',
                    'end',
                    'altitudeMode',
                    'tessellate',
                    'extrude',
                    'visibility',
                    'drawOrder',
                    'icon',
                    'h_geocode'], inplace=True)

nhgis05_09['pctWhite'] = nhgis05_09['RLAE002']
nhgis05_09['pctBlack'] = nhgis05_09['RLAE003']
nhgis05_09['pctAsian'] = nhgis05_09['RLAE005']
nhgis05_09['pctHispanic'] = nhgis05_09['RLJE003']


nhgis05_09['pctMale'] = nhgis05_09['RKYE002']
nhgis05_09['pctFemale'] = nhgis05_09['RKYE026']

nhgis05_09['pct_noGED'] = (nhgis05_09['RM8E003'] + nhgis05_09['RM8E004'] + nhgis05_09['RM8E005'] + nhgis05_09['RM8E006'] + nhgis05_09['RM8E007'] + nhgis05_09['RM8E008'] + nhgis05_09['RM8E009'] + nhgis05_09['RM8E010'] + nhgis05_09['RM8E020'] + nhgis05_09['RM8E021'] + nhgis05_09['RM8E022'] + nhgis05_09['RM8E023'] + nhgis05_09['RM8E024'] + nhgis05_09['RM8E025'] + nhgis05_09['RM8E026'] + nhgis05_09['RM8E027'])
nhgis05_09['pct_hsDeg_orGED'] = (nhgis05_09['RM8E011'] + nhgis05_09['RM8E028'])
nhgis05_09['pct_someCollege'] = (nhgis05_09['RM8E012'] + nhgis05_09['RM8E013'] + nhgis05_09['RM8E029'] + nhgis05_09['RM8E030'])
nhgis05_09['pct_associates'] = (nhgis05_09['RM8E014'] + nhgis05_09['RM8E031'])
nhgis05_09['pct_bachelors'] = (nhgis05_09['RM8E015'] + nhgis05_09['RM8E032'])
nhgis05_09['pct_masters'] = (nhgis05_09['RM8E016'] + nhgis05_09['RM8E033'])
nhgis05_09['pct_professional'] = (nhgis05_09['RM8E017'] + nhgis05_09['RM8E034'])
nhgis05_09['pct_doctorate'] = (nhgis05_09['RM8E018'] + nhgis05_09['RM8E035'])
nhgis05_09['total_pop'] = nhgis05_09['RK9E001']
nhgis05_09['med_home_val'] = nhgis05_09['RR7E001']

nhgis05_09 = nhgis05_09[nhgis05_09['total_pop'] > 0]


## conversions

blk2010_2020 = pd.read_csv('crosswalk/nhgis_bg2010_bg2020_39.csv')
"""bg2010ge:  Census Bureau standard GEOID identifier for the source 2010 block group

        bg2020gj, tr2020gj OR co2020gj:   NHGIS GISJOIN identifier for the 2020 target zone
        bg2020ge, tr2020ge OR co2020ge:   Census Bureau standard GEOID identifier for the 2020
	                                  target zone"""

blkConversion = blk2010_2020[['bg2010ge', 'bg2020ge','wt_pop']]
blkConversion['bg2010ge'] = blkConversion['bg2010ge'].astype(str).str.zfill(12)
blkConversion['bg2020ge'] = blkConversion['bg2020ge'].astype(str).str.zfill(12)
blkConversion.rename(
    columns = {
        'bg2020ge': 'GEOID_20',
        'bg2010ge': 'mergerRow',
        'wt_pop': '2020_wt_pop'
    },
    inplace = True
)

blk2000_2010 = pd.read_csv('crosswalk/nhgis_bgp2000_bg2010_39.csv')
"""- GISJOIN for 2000 block group parts (bgp2000gj): 26-character concatenation of: 0 123 4567 89012 34567 890123 4 5
        - "G"                       1 character
        - State NHGIS code:         3 digits (FIPS + "0")
        - County NHGIS code:        4 digits (FIPS + "0")
        - County subdivision code:  5 digits
        - Place/remainder code:     5 digits
        - Census tract code:        6 digits
        - Urban/rural code:         1 character ("U" for urban, "R" for rural)
        - Block group code:         1 digit
        """
blk2000_2010['STATE'] = blk2000_2010['bgp2000gj'].str[1:3]
blk2000_2010['STATE'].value_counts()
blk2000_2010['COUNTY'] = blk2000_2010['bgp2000gj'].str[4:7]
blk2000_2010['TRACT'] = blk2000_2010['bgp2000gj'].str[18:24]
blk2000_2010['BLKGRP'] = blk2000_2010['bgp2000gj'].str[25]
blk2000_2010['mergerRow'] = blk2000_2010['STATE'] + blk2000_2010['COUNTY'] + blk2000_2010['TRACT'] + blk2000_2010['BLKGRP']

"""
- 2010 block groups
        - GISJOIN (bg2010gj): 15-character concatenation of: 0 123 4567 890123 4
            - "G"                 1 character
            - State NHGIS code:   3 digits (FIPS + "0")
            - County NHGIS code:  4 digits (FIPS + "0")
            - Census tract code:  6 digits
            - Block group code:   1 digit
"""
blk2000_2010['2010Merger'] = blk2000_2010['bg2010ge'].astype(str).str.zfill(12)


convert2000To2010 = blk2000_2010[['mergerRow', '2010Merger', 'wt_pop']]

def weighted_average(df, weight_col, geocode_col, excl_cols=[]):
    """
    Function to calculate the weighted average of a dataframe by the geocode_col. This function deals with duplicates by using the weighted average of the duplicates based on the population weights

    :param df: pandas dataframe
    :param weight_col: str, name of the column that contains the weights
    :param geocode_col: str, name of the column that contains the geocode (e.g. tract, block group, etc.)
    :param excl_cols: list of str, columns to exclude from the weighted average calculation
    :return: pandas dataframe, weighted average of the input dataframe
    """
    exclude_cols = [geocode_col, weight_col]
    exclude_cols.extend(excl_cols)
    weighted_df = df.copy()
    for col in df.columns:
        if col not in exclude_cols:
            weighted_df[col] = df[col] * df[weight_col]
    weighted_df = weighted_df.groupby(geocode_col).sum().reset_index()
    return weighted_df

nhgis09_13 = pd.read_csv('nhgis_data/nhgis0003_ds201_20135_blck_grp.csv')

nhgis09_13['STATEA'] = nhgis09_13['STATEA'].astype(str).str.zfill(2)
nhgis09_13['COUNTYA'] = nhgis09_13['COUNTYA'].astype(str).str.zfill(3)
nhgis09_13['TRACTA'] = nhgis09_13['TRACTA'].astype(str).str.zfill(6)
nhgis09_13['BLKGRPA'].value_counts()
nhgis09_13['BLKGRPA'] = nhgis09_13['BLKGRPA'].astype(str).str.zfill(1)

nhgis09_13['mergerRow']= nhgis09_13['STATEA'] + nhgis09_13['COUNTYA'] + nhgis09_13['TRACTA'] + nhgis09_13['BLKGRPA']

nhgis09_13['pctWhite'] = nhgis09_13['UEQE002']
nhgis09_13['pctBlack'] = nhgis09_13['UEQE003']
nhgis09_13['pctAsian'] = nhgis09_13['UEQE005']
nhgis09_13['pctHispanic'] = nhgis09_13['UEZE003']

nhgis09_13['pctMale'] = nhgis09_13['UEEE002']
nhgis09_13['pctFemale'] = nhgis09_13['UEEE026']

nhgis09_13['pct_noGED'] = nhgis09_13['UGRE003'] + nhgis09_13['UGRE004'] + nhgis09_13['UGRE005'] + nhgis09_13['UGRE006'] + nhgis09_13['UGRE007'] + nhgis09_13['UGRE008'] + nhgis09_13['UGRE009'] + nhgis09_13['UGRE010'] + nhgis09_13['UGRE020'] + nhgis09_13['UGRE021'] + nhgis09_13['UGRE022'] + nhgis09_13['UGRE023'] + nhgis09_13['UGRE024'] + nhgis09_13['UGRE025'] + nhgis09_13['UGRE026'] + nhgis09_13['UGRE027']
nhgis09_13['pct_hsDeg_orGED'] = (nhgis09_13['UGRE011'] + nhgis09_13['UGRE028'])
nhgis09_13['pct_someCollege'] = (nhgis09_13['UGRE012'] + nhgis09_13['UGRE013'] + nhgis09_13['UGRE029'] + nhgis09_13['UGRE030'])
nhgis09_13['pct_associates'] = (nhgis09_13['UGRE014'] + nhgis09_13['UGRE031'])
nhgis09_13['pct_bachelors'] = (nhgis09_13['UGRE015'] + nhgis09_13['UGRE032'])
nhgis09_13['pct_masters'] = (nhgis09_13['UGRE016'] + nhgis09_13['UGRE033'])
nhgis09_13['pct_professional'] = (nhgis09_13['UGRE017'] + nhgis09_13['UGRE034'])
nhgis09_13['pct_doctorate'] = (nhgis09_13['UGRE018'] + nhgis09_13['UGRE035'])
nhgis09_13['total_pop'] = nhgis09_13['UEPE001']
nhgis09_13['med_home_val'] = nhgis09_13['UMME001']

nhgis09_13 = nhgis09_13[nhgis09_13['total_pop'] > 0]

jobs_05_08 = jobs[jobs['year'] < 2009]
jobs_05_08 = jobs_05_08[jobs_05_08['STATE_x'] == '39']
jobs_05_08 = jobs_05_08[jobs_05_08['COUNTY_x'] == '035']
jobs_09_13 = jobs[jobs['year'] > 2008]
jobs_09_13 = jobs_09_13[jobs_09_13['STATE_x'] == '39']
jobs_09_13 = jobs_09_13[jobs_09_13['COUNTY_x'] == '035']

nhgis05_09 = nhgis05_09[nhgis05_09['STATEA'] == '39']
nhgis09_13 = nhgis09_13[nhgis09_13['STATEA'] == '39']
nhgis05_09 = nhgis05_09[nhgis05_09['COUNTYA'] == '035']
nhgis09_13 = nhgis09_13[nhgis09_13['COUNTYA'] == '035']
nhgis05_09_final = nhgis05_09[['mergerRow', 'pctWhite', 'pctBlack', 'pctAsian', 'pctHispanic', 'pctMale', 'pctFemale', 'pct_noGED', 'pct_hsDeg_orGED', 'pct_someCollege', 'pct_associates', 'pct_bachelors', 'pct_masters', 'pct_professional', 'pct_doctorate', 'med_home_val','total_pop']]
nhgis09_13_final = nhgis09_13[['mergerRow', 'pctWhite', 'pctBlack', 'pctAsian', 'pctHispanic', 'pctMale', 'pctFemale', 'pct_noGED', 'pct_hsDeg_orGED', 'pct_someCollege', 'pct_associates', 'pct_bachelors', 'pct_masters', 'pct_professional', 'pct_doctorate', 'med_home_val', 'total_pop']]

nhgis05_09_final = nhgis05_09_final.dropna()
nhgis09_13_final = nhgis09_13_final.dropna()

print(nhgis05_09_final['total_pop'].value_counts())
print(nhgis09_13_final['total_pop'].value_counts())


nhgis05_09_final = pd.merge(nhgis05_09_final, convert2000To2010, on='mergerRow', how='inner')
nhgis05_09_final = nhgis05_09_final.dropna()

nhgis05_09_final = weighted_average(nhgis05_09_final, 'wt_pop', '2010Merger', ['mergerRow'])

nhgis05_09_final.drop(columns=['mergerRow', 'wt_pop'], inplace=True)
nhgis05_09_final.rename(columns={'2010Merger': 'mergerRow'}, inplace=True)


nhgis05_09_final = pd.merge(nhgis05_09_final, blkConversion, on='mergerRow', how='inner')
nhgis05_09_final = nhgis05_09_final.dropna()
nhgis05_09_final = weighted_average(nhgis05_09_final, '2020_wt_pop', 'GEOID_20', ['mergerRow'])
nhgis05_09_final.drop(columns=['mergerRow', '2020_wt_pop'], inplace=True)
nhgis05_09_final.rename(columns={'GEOID_20': 'mergerRow'}, inplace=True)

nhgis09_13_final = pd.merge(nhgis09_13_final, blkConversion, on='mergerRow', how='inner')
nhgis09_13_final = nhgis09_13_final.dropna()
nhgis09_13_final = weighted_average(nhgis09_13_final, '2020_wt_pop', 'GEOID_20', ['mergerRow'])
nhgis09_13_final.drop(columns=['mergerRow', '2020_wt_pop'], inplace=True)
nhgis09_13_final.rename(columns={'GEOID_20': 'mergerRow'}, inplace=True)

## adding has degree column
nhgis05_09_final['pct_hasDegree'] = nhgis05_09_final['pct_associates'] + nhgis05_09_final['pct_bachelors'] + nhgis05_09_final['pct_masters'] + nhgis05_09_final['pct_professional'] + nhgis05_09_final['pct_doctorate']
nhgis09_13_final['pct_hasDegree'] = nhgis09_13_final['pct_associates'] + nhgis09_13_final['pct_bachelors'] + nhgis09_13_final['pct_masters'] + nhgis09_13_final['pct_professional'] + nhgis09_13_final['pct_doctorate']
## Making all our pct columns into actual percent columns using the corrected total population column
pctCols = ['pctWhite', 'pctBlack', 'pctAsian', 'pctHispanic', 'pctMale', 'pctFemale', 'pct_noGED', 'pct_hsDeg_orGED', 'pct_someCollege', 'pct_associates', 'pct_bachelors', 'pct_masters', 'pct_professional', 'pct_doctorate','pct_hasDegree']

for col in pctCols:
    nhgis05_09_final[col] = nhgis05_09_final[col] / nhgis05_09_final['total_pop']
    nhgis09_13_final[col] = nhgis09_13_final[col] / nhgis09_13_final['total_pop']


def aggregate_with_default(df, groupby_cols, default_agg='sum', exceptions={}):
    numeric_cols = df.select_dtypes(include='number').columns
    agg_dict = {col: default_agg if col in numeric_cols else 'first' for col in df.columns if col not in groupby_cols}
    agg_dict.update(exceptions)
    return df.groupby(groupby_cols).agg(agg_dict).reset_index()

jobs_05_08 = aggregate_with_default(jobs_05_08, ['mergerRow', 'year'], exceptions={'HealthLine': 'mean', 'After': 'mean', 'healthline_x_after': 'mean'})
print(jobs_05_08['STATE_x'].value_counts())
jobs_09_13 = aggregate_with_default(jobs_09_13, ['mergerRow', 'year'], exceptions={'HealthLine': 'mean', 'After': 'mean', 'healthline_x_after': 'mean'})


jobs_05_08['accessArea'] = jobs_05_08['bufferArea'] / jobs_05_08['BlockArea']
jobs_09_13['accessArea'] = jobs_09_13['bufferArea'] / jobs_09_13['BlockArea']
jobs_05_08['HealthLine'] = np.where(jobs_05_08['accessArea'] > 0.3, 1, 0)
jobs_09_13['HealthLine'] = np.where(jobs_09_13['accessArea'] > 0.3, 1, 0)
jobs_09_13['After'] = 1
jobs_09_13['healthline_x_after'] = jobs_09_13['HealthLine'] * jobs_09_13['After']


gis_04 = nhgis05_09_final.copy()
gis_04['year'] = 2004
gis_05 = nhgis05_09_final.copy()
gis_05['year'] = 2005
gis_06 = nhgis05_09_final.copy()
gis_06['year'] = 2006
gis_07 = nhgis05_09_final.copy()
gis_07['year'] = 2007
gis_08 = nhgis05_09_final.copy()
gis_08['year'] = 2008
gis_09 = nhgis09_13_final.copy()
gis_09['year'] = 2009
gis_10 = nhgis09_13_final.copy()
gis_10['year'] = 2010
gis_11 = nhgis09_13_final.copy()
gis_11['year'] = 2011
gis_12 = nhgis09_13_final.copy()
gis_12['year'] = 2012
gis_13 = nhgis09_13_final.copy()
gis_13['year'] = 2013

nhgis_05_09_final = pd.concat([gis_04,gis_05,gis_06,gis_07,gis_08],axis=0)
nhgis_09_13_final = pd.concat([gis_09,gis_10,gis_11,gis_12,gis_13],axis=0)
nhgis_05_09_final['merge_year'] = nhgis_05_09_final['mergerRow'] + nhgis_05_09_final['year'].astype(str)
nhgis_09_13_final['merge_year'] = nhgis_09_13_final['mergerRow'] + nhgis_09_13_final['year'].astype(str)
nhgis_05_09_final.drop(columns=['year'],inplace=True)
nhgis_09_13_final.drop(columns=['year'],inplace=True)
jobs_05_08['merge_year'] = jobs_05_08['mergerRow'] + jobs_05_08['year'].astype(str)
jobs_09_13['merge_year'] = jobs_09_13['mergerRow'] + jobs_09_13['year'].astype(str)



final_05_08 = pd.merge(jobs_05_08, nhgis_05_09_final, on=['merge_year'], how='inner')

final_09_13 = pd.merge(jobs_09_13, nhgis_09_13_final, on=['merge_year'], how='inner')





final = pd.concat([final_05_08, final_09_13],axis=0)
final['total_pop'] = round(final['total_pop'])
final = final[final['total_pop'] > 0]
## normalize job data to percentage of total jobs
jobRows = ['total_29_and_under',
            'total_30_54',
            'total_55_and_over',
            'total_under_1250per_month',
            'total_1250_3333per_month',
            'total_3334_and_up_per_month',
            'agriculture_forestry_fishing_hunting',
            'mining_quarrying_oil_gas_extraction',
            'utilities',
            'construction',
            'manufacturing',
            'wholesale_trade',
            'retail_trade',
            'transportation_warehousing',
            'information',
            'finance_insurance',
            'real_estate_rental_leasing',
            'professional_scientific_technical_services',
            'management_of_companies_enterprises',
            'admin_support_waste_mgmt_remediation_services',
            'educational_services',
            'health_care_social_assistance',
            'arts_entertainment_recreation',
            'accommodation_food_services',
            'other_services_except_public_administration',
            'public_administration',
            'race_white',
            'race_black',
            'race_american_indian_alaska_native',
            'race_asian',
            'race_native_hawaiian_other_pacific_islander',
            'race_two_or_more',
            'ethnicity_not_hispanic_latino',
            'ethnicity_hispanic_latino',
            'less_than_HS',
            'HS_GED',
            'Some_college_or_associates_degree',
            'Bachelors_or_higher',
            'sex_male',
            'sex_female']


for row in jobRows:
    final[row] = final[row] / final['total_jobs']

final['total_jobs'] = final['total_jobs'] / final['total_pop']

final = final[final['total_jobs'] < 1]

final.to_csv('LEHD_data_NHGIS_controls_BlkGrp.csv')
