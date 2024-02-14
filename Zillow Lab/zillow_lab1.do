cd "/Users/johnmccormick/githubFolder/econCapstone"

clear
import delimited "final.xlsx - dataset.csv"


reg pct_sold_below_list mean_days_pending, r



reg pct_sold_below_list mean_days_pending median_list_price, r


reg pct_sold_below_list zhvi, r

generate sale_minus_list = median_sale_price - median_list_price
generate sale_vs_zhvi = median_sale_price - zhvi
generate list_vs_zhvi = median_list_price - zhvi

ttest median_sale_price==median_list_price
ttest median_sale_price==zhvi
ttest median_list_price==zhvi

estpost correlate pct_sold_below_list mean_days_pending sales_count_nowcast zhvi invt_for_sale median_list_price median_sale_price
est store a

by region_name, sort: tabstat pct_sold_below_list mean_days_pending sales_count_nowcast zhvi invt_for_sale median_list_price median_sale_price, statistics(mean)


// estpost tabstat pct_sold_below_list mean_days_pending sales_count_nowcast zhvi invt_for_sale median_list_price median_sale_price
est store b


esttab a b  using Zillow_1_ttests.tex, replace 
