clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"

// Correlation matrices
pwcorr total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance healthline, sig star(.05)


// Demographics on healthline
pwcorr healthline pctwhite pctblack pcthispanic pctmale, sig star(.05)
matrix demographicHealthline = r(C)

// Outcomes and demographics
pwcorr total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance pctwhite pctblack pcthispanic pctmale, sig star(.05)
matrix outcomeDemographics = r(C)

// Education
pwcorr healthline total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month accommodation_food_services health_care_social_assistance pct_hasdegree pct_noged, sig star(.05)
matrix education = r(C)

// Export to LaTeX
estout matrix(outcomeMatrix) using Outcomecorrelations.tex, replace unstack label starlevels(* 0.05 ** 0.01 *** 0.001)
estout matrix(demographicHealthline) using Demographiccorrelations.tex, replace unstack label starlevels(* 0.05 ** 0.01 *** 0.001)
estout matrix(outcomeDemographics) using OutcomeDemocorrelations.tex, replace unstack label starlevels(* 0.05 ** 0.01 *** 0.001)
estout matrix(education) using Educationcorrelations.tex, replace unstack label starlevels(* 0.05 ** 0.01 *** 0.001)




