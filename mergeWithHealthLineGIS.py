import pandas as pd

################################## Merge with HealthLine GIS Data ##################################
#         This script merged the full geographic jobs data with the manually computed              #
#         HealthLine access data. The HealthLine access data was computed manually using           #
#         QGIS software. The HealthLine access data was then merged with the full geographic       #
#         jobs data to create a new csv file.                                                      #
#                                                                                                  #
#         HealthLine access is defined below as any block group with more than 25% of its          #
#         block area being within 800m of the HealthLine.                                          #
#                                                                                                  #
#         Author: John McCormick                                                                   #
#         Date: March 4th, 2024                                                                    #
#                                                                                                  #
####################################################################################################


access = pd.read_csv("LEHD_data/HealthLineAccess.csv")
access.head()
access['STATE'] = access['STATE'].astype(str).str.zfill(2)  # State code is 2 digits
access['COUNTY'] = access['COUNTY'].astype(str).str.zfill(3)  # County codes are 3 digits
access['TRACT'] = access['TRACT'].astype(str).str.zfill(6)  # Tract codes are 6 digits
access['BLOCK'] = access['BLOCK'].astype(str).str.zfill(4)  # Block codes are 4 digits
access['h_geocode'] = (access['STATE']) + (access['COUNTY']) + (access['TRACT'])+ (access['BLOCK'])
access.head()
access['HealthLine'] = access['pctTransitAccess'] > 0.25
access['HealthLine'] = access['HealthLine'].astype(int)
access.head()


data = pd.read_csv("LEHD_data/CuyahogaCountyRAC_SHP.csv")
print(data.columns)
data.head()
data['year'].value_counts()
data['h_geocode'] = data['h_geocode'].astype(str)
merged = pd.merge(data, access, on = 'h_geocode', how = 'left')
merged.head()
merged['HealthLine'] = merged['HealthLine'].fillna(0)
merged['After'] = merged['year'] > 2008
merged['After'] = merged['After'].astype(int)
merged['HealthLine'].value_counts()
merged['After'].value_counts()
merged['healthline_x_after'] = merged['HealthLine'] * merged['After']
merged['healthline_x_after'].value_counts()
merged['BlockArea'] = merged['AREALAND']
merged['bufferArea'].fillna(0, inplace=True)

datadictionary = {
    'C000': 'total_jobs',
    'CA01': 'total_29_and_under',
    'CA02': 'total_30_54',
    'CA03': 'total_55_and_over',
    'CE01': 'total_under_1250per_month',
    'CE02': 'total_1250_3333per_month',
    'CE03': 'total_3334_and_up_per_month',
    'CNS01': 'agriculture_forestry_fishing_hunting',
    'CNS02': 'mining_quarrying_oil_gas_extraction',
    'CNS03': 'utilities',
    'CNS04': 'construction',
    'CNS05': 'manufacturing',
    'CNS06': 'wholesale_trade',
    'CNS07': 'retail_trade',
    'CNS08': 'transportation_warehousing',
    'CNS09': 'information',
    'CNS10': 'finance_insurance',
    'CNS11': 'real_estate_rental_leasing',
    'CNS12': 'professional_scientific_technical_services',
    'CNS13': 'management_of_companies_enterprises',
    'CNS14': 'admin_support_waste_mgmt_remediation_services',
    'CNS15': 'educational_services',
    'CNS16': 'health_care_social_assistance',
    'CNS17': 'arts_entertainment_recreation',
    'CNS18': 'accommodation_food_services',
    'CNS19': 'other_services_except_public_administration',
    'CNS20': 'public_administration',
    'CR01': 'race_white',
    'CR02': 'race_black',
    'CR03': 'race_american_indian_alaska_native',
    'CR04': 'race_asian',
    'CR05': 'race_native_hawaiian_other_pacific_islander',
    'CR07': 'race_two_or_more',
    'CT01': 'ethnicity_not_hispanic_latino',
    'CT02': 'ethnicity_hispanic_latino',
    'CD01': 'less_than_HS',
    'CD02': 'HS_GED',
    'CD03': 'Some_college_or_associates_degree',
    'CD04': 'Bachelors_or_higher',
    'CS01': 'sex_male',
    'CS02': 'sex_female'
}

for key, value in datadictionary.items():
    merged.rename(columns={key: value}, inplace=True)

merged.to_csv("LEHD_data/FinalJobData.csv", index=False)