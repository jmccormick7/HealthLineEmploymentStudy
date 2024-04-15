clear 
set more off
cd "H:\ECON395"
capture log close
log using data_exploration.log, replace
import delimited "LEHD_data_NHGIS_controls_BlkGrp.csv"
//outlier !!!
drop if (total_jobs > 1)
//correlation/export
pwcorr total_jobs healthline pctwhite pctmale pctunder18 pct_hasdegree med_home_val total_pop, sig star(.1)
corrtex total_jobs healthline pctwhite pctmale pctunder18 pct_hasdegree med_home_val total_pop, file(corr.txt) replace
pwcorr total_jobs healthline pctwhite pctblack pctasian pcthispanic, sig star (0.01)
corrtex total_jobs healthline pctwhite pctblack pctasian pcthispanic, file(racecorr.txt) replace
//big correlation for visualization
corr total_jobs healthline pctwhite pctblack pctasian pcthispanic pctmale pctfemale pct_noged pct_hsdeg_orged pct_somecollege pct_associates pct_bachelors pct_masters pct_professional pct_doctorate pctunder18 pctover65 med_home_val total_pop
//the tttttests
ttest total_jobs, by(healthline)
//for parallel trends
gen hl_jobs = total_jobs if (healthline == 1)
gen no_hl_jobs = total_jobs if (healthline == 0)
bysort year: egen hl_jobs_yearly = mean(hl_jobs)
bysort year: egen no_hl_jobs_yearly = mean(no_hl_jobs)
//regression table (regrable)
gen healthline_x_pctblack = healthline * pctblack
gen healthline_x_pctnoged = healthline * pct_noged

//total jobs
quietly regress total_jobs healthline, r //ols
eststo m1, title("Ordinary Least Squares")
quietly regress total_jobs healthline pctblack pct_noged med_home_val total_pop, r //multivariate
eststo m2, title("Multivariate")
quietly regress total_jobs healthline pctblack pct_noged med_home_val total_pop healthline_x_pctblack, r //interaction 1
eststo m3, title("HealthLine x Pct Black Interaction")
quietly regress total_jobs healthline pctblack pct_noged med_home_val total_pop healthline_x_pctnoged, r //interaction 2
eststo m4, title("HealthLine x Pct No GED Interaction")

// Export the regression results to LaTeX using estout
esttab m1 m2 m3 m4, ///
    cells(b(star fmt(8)) se(par fmt(6))) /// 
    replace ///
    title("Regressions with \% Pop Employed") ///
    label ///
    nomtitles ///
    coeflabels(healthline "HealthLine" ///
               pctblack "\% Black" ///
               pct_noged "\% No GED" ///
               med_home_val "Med Home Val" ///
               total_pop "Total Pop" ///
               healthline_x_pctblack "HealthLine x \% Black" ///
               healthline_x_pctnoged "HealthLine x \% No GED") ///
    stats(N r2) ///
    collabels(none) ///
    noobs ///
    nonumber ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    booktabs ///
    ///
	

//healthcare
quietly regress health_care_social_assistance healthline, r //ols
eststo m1, title("Ordinary Least Squares")
quietly regress health_care_social_assistance healthline pctblack pct_noged med_home_val total_pop, r //multivariate
eststo m2, title("Multivariate")
quietly regress health_care_social_assistance healthline pctblack pct_noged med_home_val total_pop healthline_x_pctblack, r //interaction 1
eststo m3, title("HealthLine x Pct Black Interaction")
quietly regress health_care_social_assistance healthline pctblack pct_noged med_home_val total_pop healthline_x_pctnoged, r //interaction 2
eststo m4, title("HealthLine x Pct No GED Interaction")

// Export the regression results to LaTeX using estout
esttab m1 m2 m3 m4, ///
    cells(b(star fmt(8)) se(par fmt(6))) /// 
    replace ///
    title("Regressions with Health Care Social Assistance Job Share") ///
    label ///
    nomtitles ///
    coeflabels(healthline "HealthLine" ///
               pctblack "\% Black" ///
               pct_noged "\% No GED" ///
               med_home_val "Med Home Val" ///
               total_pop "Total Pop" ///
               healthline_x_pctblack "HealthLine x \% Black" ///
               healthline_x_pctnoged "HealthLine x \% No GED") ///
    stats(N r2) ///
    collabels(none) ///
    noobs ///
    nonumber ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    booktabs ///
    ///
	
//education
quietly regress educational_services healthline, r //ols
eststo m1, title("Ordinary Least Squares")
quietly regress educational_services healthline pctblack pct_noged med_home_val total_pop, r //multivariate
eststo m2, title("Multivariate")
quietly regress educational_services healthline pctblack pct_noged med_home_val total_pop healthline_x_pctblack, r //interaction 1
eststo m3, title("HealthLine x Pct Black Interaction")
quietly regress educational_services healthline pctblack pct_noged med_home_val total_pop healthline_x_pctnoged, r //interaction 2
eststo m4, title("HealthLine x Pct No GED Interaction")

// Export the regression results to LaTeX using estout
esttab m1 m2 m3 m4, ///
    cells(b(star fmt(8)) se(par fmt(6))) /// 
    replace ///
    title("Regressions with Educational Services Job Share") ///
    label ///
    nomtitles ///
    coeflabels(healthline "HealthLine" ///
               pctblack "\% Black" ///
               pct_noged "\% No GED" ///
               med_home_val "Med Home Val" ///
               total_pop "Total Pop" ///
               healthline_x_pctblack "HealthLine x \% Black" ///
               healthline_x_pctnoged "HealthLine x \% No GED") ///
    stats(N r2) ///
    collabels(none) ///
    noobs ///
    nonumber ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    booktabs ///
    ///
	
//prof
quietly regress professional_scientific_technica healthline, r //ols
eststo m1, title("Ordinary Least Squares")
quietly regress professional_scientific_technica healthline pctblack pct_noged med_home_val total_pop, r //multivariate
eststo m2, title("Multivariate")
quietly regress professional_scientific_technica healthline pctblack pct_noged med_home_val total_pop healthline_x_pctblack, r //interaction 1
eststo m3, title("HealthLine x Pct Black Interaction")
quietly regress professional_scientific_technica healthline pctblack pct_noged med_home_val total_pop healthline_x_pctnoged, r //interaction 2
eststo m4, title("HealthLine x Pct No GED Interaction")

// Export the regression results to LaTeX using estout
esttab m1 m2 m3 m4, ///
    cells(b(star fmt(8)) se(par fmt(6))) /// 
    replace ///
    title("Regressions with Prof/Sci/Tech Job Share") ///
    label ///
    nomtitles ///
    coeflabels(healthline "HealthLine" ///
               pctblack "\% Black" ///
               pct_noged "\% No GED" ///
               med_home_val "Med Home Val" ///
               total_pop "Total Pop" ///
               healthline_x_pctblack "HealthLine x \% Black" ///
               healthline_x_pctnoged "HealthLine x \% No GED") ///
    stats(N r2) ///
    collabels(none) ///
    noobs ///
    nonumber ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    booktabs ///
    ///
	
//food
quietly regress accommodation_food_services healthline, r //ols
eststo m1, title("Ordinary Least Squares")
quietly regress accommodation_food_services healthline pctblack pct_noged med_home_val total_pop, r //multivariate
eststo m2, title("Multivariate")
quietly regress accommodation_food_services healthline pctblack pct_noged med_home_val total_pop healthline_x_pctblack, r //interaction 1
eststo m3, title("HealthLine x Pct Black Interaction")
quietly regress accommodation_food_services healthline pctblack pct_noged med_home_val total_pop healthline_x_pctnoged, r //interaction 2
eststo m4, title("HealthLine x Pct No GED Interaction")

// Export the regression results to LaTeX using estout
esttab m1 m2 m3 m4, ///
    cells(b(star fmt(8)) se(par fmt(6))) /// 
    replace ///
    title("Regressions with Accommodation/Food Services Job Share") ///
    label ///
    nomtitles ///
    coeflabels(healthline "HealthLine" ///
               pctblack "\% Black" ///
               pct_noged "\% No GED" ///
               med_home_val "Med Home Val" ///
               total_pop "Total Pop" ///
               healthline_x_pctblack "HealthLine x \% Black" ///
               healthline_x_pctnoged "HealthLine x \% No GED") ///
    stats(N r2) ///
    collabels("Simple Regression" "Multivariate Regression" "\% Black Interaction" "\% No GED Interaction") ///
    noobs ///
    nonumber ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    booktabs ///
    ///
	

