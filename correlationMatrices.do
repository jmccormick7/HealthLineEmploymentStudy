clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"

// Correlation matrices
corrtex total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance healthline after, file("outcomes.tex") replace sig digits(4)


// Demographics on healthline
corrtex healthline after pctwhite pctblack pcthispanic pctmale, file("demographics.tex") replace sig digits(4)

// Outcomes and demographics
corrtex total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance pctwhite pctblack pcthispanic pctmale, file("outcomeDemo.tex") replace sig digits(4)
 
// Education
corrtex healthline total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance pct_hasdegree pct_noged after, file("education.tex") replace sig digits(4)





