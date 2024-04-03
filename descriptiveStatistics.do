clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone"

import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"


dtable total_jobs total_under_1250per_month total_1250_3333per_month total_3334_and_up_per_month health_care_social_assistance accommodation_food_services race_black, by(healthline, tests nototals) column(by(hide, fvlabel) ) nosample continuous(, statistics(mean sd)) nformat(%5.4g) export(jobsDesc.tex, as(tex) replace)


dtable pctwhite pctblack pctasian pcthispanic pctmale pctfemale pctunder18 pctover65, by(healthline, tests nototals) column(by(hide, fvlabel)) nosample continuous(,statistics(mean sd)) nformat(%5.4g) export(demoDesc.tex, as(tex) replace)


dtable pct_noged pct_hsdeg_orged pct_somecollege pct_associates pct_bachelors pct_masters pct_professional pct_doctorate, by(healthline, tests nototals) column(by(hide, fvlabel)) nosample continuous(, statistics(mean sd)) nformat(%5.4g) export(educDesc.tex, as(tex) replace)
