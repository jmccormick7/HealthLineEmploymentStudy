cd "/Users/johnmccormick/githubFolder/econCapstone"

clear
log using zillow2.log
import delimited "cleanedZillowData.csv"

// Simple regression
reg pct_sold_below_list mean_days_pending, r
eststo simple_reg 

// Multivariate regression
reg pct_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, r
eststo multi_reg

// Fixed Effects 
gen year_state = year*state
xtset year_state
xtreg pct_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, fe
eststo fixed_effects

// interactionTerms
gen days_pending_x_zhvi = zhvi * mean_days_pending
xtreg pct_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast days_pending_x_zhvi, fe
eststo interactionTerm

// colinearity 
// colinear variables are zhvi and median_sale_price
xtreg pct_sold_below_list mean_days_pending median_list_price median_sale_price invt_for_sale sales_count_nowcast, fe
eststo colin_zhvi

xtreg pct_sold_below_list mean_days_pending zhvi median_list_price invt_for_sale sales_count_nowcast, fe
eststo colin_sale

// Log Transformations
gen log_est_num_sold_below_list = log(est_num_sold_below_list) 
reg log_est_num_sold_below_list mean_days_pending zhvi median_list_price median_sale_price invt_for_sale sales_count_nowcast, r
eststo log_linear

gen log_days_pending = log(mean_days_pending)
gen log_zhvi = log(zhvi)
gen log_median_list = log(median_list_price)
gen log_median_sale = log(median_sale_price)
gen log_invt = log(invt_for_sale)
gen log_sales_count = log(sales_count_nowcast)

reg log_est_num_sold_below_list log_days_pending log_zhvi log_median_list log_median_sale log_invt log_sales_count, r
eststo log_log

esttab simple_reg multi_reg fixed_effects interactionTerm colin_zhvi colin_sale log_linear log_log using Zillow2.tex, se r2  replace

clear
import delimited "mergedZillowData.csv"

gen log_days_pending = log(mean_days_pending)
gen log_zhvi = log(zhvi)
gen log_median_list = log(median_list_price)
gen log_median_sale = log(median_sale_price)
gen log_invt = log(invt_for_sale)
gen log_sales_count = log(sales_count_nowcast)

reg pct_sold_below_list mean_days_pending sunny_hours, r
eststo sunny1

reg pct_sold_below_list log_days_pending sunny_hours log_zhvi log_median_list log_median_sale log_invt log_sales_count, r 
eststo sunny2

esttab sunny1 sunny2 using sunnyZillow.tex, se r2   replace
