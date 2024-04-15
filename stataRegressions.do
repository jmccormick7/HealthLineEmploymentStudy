clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"

// cleveland is 38 percent white 
g minority = pctwhite < 0.20

// Cleveland has 82 percent HS grad so 18% is standard dropout rate 
g uneducated = pct_noged > .22

// overall mean is 0.23
g educated = pct_hasdegree > 0.3


// interaction terms for minority
g healthline_x_minority = healthline * minority
g after_x_minority = after * minority 
g after_x_minority_healthline = after * minority * healthline

// interaction terms for uneducated 
g uneducated_x_healthline = uneducated * healthline
g after_x_uneducated = uneducated * after
g after_x_uneducated_healthline = after * uneducated * healthline


// interaction terms for educated 
g educated_x_healthline = educated * healthline
g after_x_educated = after * educated 
g after_x_educated_healthline = after * educated * healthline


// fixed effects terms 
// mergerrow_x is the Geocode down to block group 
xtset mergerrow_x year

// Total Jobs

reg total_jobs healthline after healthline_x_after pctblack pct_hasdegree pct_noged med_home_val , r
eststo jobsDiD

reghdfe total_jobs healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, absorb(mergerrow_x year) vce(robust)
eststo jobsfeDiD

reghdfe total_jobs healthline_x_after minority educated uneducated healthline_x_minority after_x_minority after_x_minority_healthline, absorb(mergerrow_x year) vce(robust)
eststo minorityInteractionJobs

reghdfe total_jobs healthline_x_after minority educated uneducated uneducated_x_healthline after_x_uneducated after_x_uneducated_healthline, absorb(mergerrow_x year) vce(robust)
eststo uneducatedInteractionJobs

reghdfe total_jobs healthline_x_after minority educated uneducated educated_x_healthline after_x_educated after_x_educated_healthline, absorb(mergerrow_x year) vce(robust)
eststo educatedInteractionJobs

esttab jobsDiD jobsfeDiD using totalJobsDiD.tex, se r2 replace

esttab minorityInteractionJobs uneducatedInteractionJobs educatedInteractionJobs using jobsDDD.tex, se r2 replace

esttab jobsDiD jobsfeDiD minorityInteractionJobs uneducatedInteractionJobs educatedInteractionJobs using totalJobs.tex, se r2 replace


// healthcare 


reg health_care_social_assistance healthline after healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, r 
eststo healthDiD

reghdfe health_care_social_assistance healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, absorb(mergerrow_x year) vce(robust)
eststo healthfeDiD

reghdfe health_care_social_assistance healthline_x_after minority educated uneducated healthline_x_minority after_x_minority after_x_minority_healthline, absorb(mergerrow_x year) vce(robust)
eststo minorityInteractionHealth

reghdfe health_care_social_assistance healthline_x_after minority educated uneducated uneducated_x_healthline after_x_uneducated after_x_uneducated_healthline, absorb(mergerrow_x year) vce(robust)
eststo uneducatedInteractionhealth

reghdfe health_care_social_assistance healthline_x_after minority educated uneducated educated_x_healthline after_x_educated after_x_educated_healthline, absorb(mergerrow_x year) vce(robust)
eststo educatedInteractionHealth

esttab healthDiD healthfeDiD using HealthDiD.tex, se r2 replace

esttab minorityInteractionHealth uneducatedInteractionhealth educatedInteractionHealth using HealthDDD.tex, se r2 replace

esttab healthDiD healthfeDiD minorityInteractionHealth uneducatedInteractionhealth educatedInteractionHealth using Health.tex, se r2 replace


//food services 

reg accommodation_food_services healthline after healthline_x_after pctblack pct_hasdegree pct_noged med_home_val , r
eststo foodDiD

reghdfe accommodation_food_services healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, absorb(mergerrow_x year) vce(robust)
eststo foodfeDiD

reghdfe accommodation_food_services healthline_x_after minority educated uneducated healthline_x_minority after_x_minority after_x_minority_healthline, absorb(mergerrow_x year) vce(robust)
eststo minorityinteractionsfood

reghdfe accommodation_food_services healthline_x_after minority educated uneducated uneducated_x_healthline after_x_uneducated after_x_uneducated_healthline, absorb(mergerrow_x year) vce(robust)
eststo uneducatedinteractionsfood

reghdfe accommodation_food_services healthline_x_after minority educated uneducated educated_x_healthline after_x_educated after_x_educated_healthline, absorb(mergerrow_x year) vce(robust)
eststo educatedInteractionFood

esttab foodDiD foodfeDiD using FoodDiD.tex, se r2 replace

esttab minorityinteractionsfood uneducatedinteractionsfood educatedInteractionFood using FoodDDD.tex, se r2 replace


esttab foodDiD foodfeDiD minorityinteractionsfood uneducatedinteractionsfood educatedInteractionFood using food.tex, se r2 replace

//educational services 

reg educational_services healthline after healthline_x_after pctblack pct_hasdegree pct_noged med_home_val , r
eststo educationDiD

reghdfe educational_services healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, absorb(mergerrow_x year) vce(robust)
eststo educationfeDiD

reghdfe educational_services healthline_x_after minority educated uneducated healthline_x_minority after_x_minority after_x_minority_healthline, absorb(mergerrow_x year) vce(robust) 
eststo minorityInteractionEduc

reghdfe educational_services healthline_x_after minority educated uneducated uneducated_x_healthline after_x_uneducated after_x_uneducated_healthline, absorb(mergerrow_x year) vce(robust)
eststo uneducatedInteractionEduc

reghdfe educational_services healthline_x_after minority educated uneducated educated_x_healthline after_x_educated after_x_educated_healthline, absorb(mergerrow_x year) vce(robust)
eststo educatedInteractionEduc

esttab educationDiD educationfeDiD using educationDiD.tex, se r2 replace

esttab minorityInteractionEduc uneducatedInteractionEduc educatedInteractionEduc using educationDDD.tex, se r2 replace

esttab educationDiD educationfeDiD minorityInteractionEduc uneducatedInteractionEduc educatedInteractionEduc using education.tex, se r2 replace

// science and tech 
reg professional_scientific_technica healthline after healthline_x_after pctblack pct_hasdegree pct_noged med_home_val , r
eststo scienceDiD

reghdfe professional_scientific_technica healthline_x_after pctblack pct_hasdegree pct_noged med_home_val, absorb(mergerrow_x year) vce(robust)
eststo sciencefeDiD

reghdfe professional_scientific_technica healthline_x_after minority educated uneducated healthline_x_minority after_x_minority after_x_minority_healthline, absorb(mergerrow_x year) vce(robust)
eststo minorityInteractionSci

reghdfe professional_scientific_technica healthline_x_after minority educated uneducated uneducated_x_healthline after_x_uneducated after_x_uneducated_healthline, absorb(mergerrow_x year) vce(robust)
eststo uneducatedinteractionSci

reghdfe professional_scientific_technica healthline_x_after minority educated uneducated educated_x_healthline after_x_educated after_x_educated_healthline, absorb(mergerrow_x year) vce(robust)
eststo educatedInteractionSci

esttab scienceDiD sciencefeDiD using scienceDiD.tex, se r2 replace

esttab minorityInteractionSci uneducatedinteractionSci educatedInteractionSci using scienceDDD.tex, se r2 replace

esttab scienceDiD sciencefeDiD minorityInteractionSci uneducatedinteractionSci educatedInteractionSci using science.tex, se r2 replace


esttab jobsfeDiD healthfeDiD foodfeDiD educationfeDiD sciencefeDiD using allDiD.tex, se r2 replace



