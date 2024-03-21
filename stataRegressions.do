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

reg logJobs healthline after healthline_x_after pctwhite pct_hasdegree

reg logUnder1250 healthline after healthline_x_after pctwhite pct_hasdegree

reg log1250_3333 healthline after healthline_x_after pctwhite pct_hasdegree

reg logOver3333 healthline after healthline_x_after pctwhite pct_hasdegree

reg logHealth healthline after healthline_x_after pctwhite pct_hasdegree

reg logService healthline after healthline_x_after pctwhite pct_hasdegree


