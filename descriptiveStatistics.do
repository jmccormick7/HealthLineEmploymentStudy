clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"

estpost sum total_jobs total_under_1250per_month total_1250_3333per_month  total_3334_and_up_per_month health_care_social_assistance accommodation_food_services if healthline == 1
eststo jobsHealthLine

estpost sum total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month health_care_social_assistance accommodation_food_services if healthline == 0
eststo jobsControl

esttab jobsHealthLine jobsControl using jobsDesc.tex, replace cells("mean(fmt(4)) sd(fmt(4))") label nonumber noobs alignment(S) booktabs




estpost sum pctwhite pctblack pctasian pcthispanic pctmale pctfemale if healthline == 1
eststo demoHealthLine

estpost sum pctwhite pctblack pctasian pcthispanic pctmale pctfemale if healthline == 0
eststo demoControl

esttab demoHealthLine demoControl using demoDesc.tex, replace cells("mean(fmt(4)) sd(fmt(4))") label nonumber noobs alignment(S) booktabs


estpost sum pct_noged pct_hsdeg_orged pct_somecollege pct_associates pct_bachelors pct_masters pct_professional pct_doctorate if healthline ==1 
eststo educHealthLine

estpost sum pct_noged pct_hsdeg_orged pct_somecollege pct_associates pct_bachelors pct_masters pct_professional pct_doctorate if healthline ==0 
eststo educControl

esttab educHealthLine educControl using educDesc.tex, replace cells("mean(fmt(4)) sd(fmt(4))") label nonumber noobs alignment(S) booktabs
