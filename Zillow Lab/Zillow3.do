cd "/Users/johnmccormick/Desktop/econCapstone"

clear

import delimited "cleanedZillowData_SeattleDummy.csv"

// Multivariate regression
reg pct_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, r
eststo multi_reg

// Fixed Effects 
gen year_state = year*state
xtset year_state
xtreg pct_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, fe
eststo fixed_effects

// IV -- median_sale_to_list_ratio
// Step 1: First Stage Regression
reg mean_days_pending median_sale_to_list_ratio zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, robust
eststo first_stage

// Step 2: Perform F-test on the instrument in the first stage
test median_sale_to_list_ratio


ivregress 2sls pct_sold_below_list (mean_days_pending = median_sale_to_list_ratio) zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, r
eststo IV


// diff in diff
gen after = year > 2019
gen seattle_after = seattle * after

reg pct_sold_below_list seattle after seattle_after zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast if seattle == 1 | sanfran == 1, r
eststo diff_diff


esttab multi_reg fixed_effects IV diff_diff using zillow3.tex, se r2   replace
