cd "/Users/johnmccormick/githubFolder/econCapstone"

clear
import delimited "final.xlsx - dataset.csv"


reg pct_sold_below_list mean_days_pending, r



reg pct_sold_below_list mean_days_pending median_list_price, r


reg pct_sold_below_list zhvi, r

generate sale_minus_list = median_sale_price - median_list_price
generate sale_vs_zhvi = median_sale_price - zhvi
generate list_vs_zhvi = median_list_price - zhvi

estpost ttest median_sale_price==median_list_price
est store a

estpost ttest median_sale_price==zhvi
est store b

estpost ttest median_list_price==zhvi
est store c

esttab a b c using Zillow_1_ttests.tex, replace ///
mtitles ("\textbf{Paired T-test of median sale price and median list price}" "\textbf{Paired T-test of median sale price and Zillow home value index}" "\textbf{Paired T-test of median list price and Zillow home value index}") ///

