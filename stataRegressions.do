clear 
set more off
cd "/Users/johnmccormick/githubFolder/econCapstone/LEHD_data"

import delimited "FinalJobData.csv"

reg total_jobs healthline after healthline_x_after
