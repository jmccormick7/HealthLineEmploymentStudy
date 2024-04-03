clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"


g logJobs = log(total_jobs)
g logUnder1250 = log(total_under_1250per_month)
g log1250_3333 = log(total_1250_3333per_month)
g logOver3333 = log(total_3334_and_up_per_month)
g logHealth = log(health_care_social_assistance)
g logService = log(accommodation_food_services)

reg total_jobs healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 
 
reg health_care_social_assistance healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 

reg accommodation_food_services healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 

reg educational_services healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 

reg professional_scientific_technica healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 

reg information healthline after healthline_x_after pctwhite pctblack pct_hasdegree pct_noged med_home_val 
