
cd "/Users/johnmccormick/githubFolder/econCapstone"

clear
import delimited "final.xlsx - dataset.csv"


reg pct_sold_below_list mean_days_pending, r
eststo reg1



reg pct_sold_below_list mean_days_pending median_list_price median_sale_price invt_for_sale zhvi sales_count_nowcast, r
eststo reg2


reg pct_sold_below_list zhvi, r
outreg2 using test.tex, ctitle("Model 3") append


//esttab reg1 reg2 reg3 using table1.tex

