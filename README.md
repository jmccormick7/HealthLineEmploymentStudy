# Code and Data Repository for `The WealthLine—Examining the Effect of the HealthLine Bus Rapid Transit on Resident Employment`

***The WealthLine—Examining the Effect of the HealthLine Bus Rapid Transit on Resident Employment*** was presented as a working paper at the **Federal Reserve Bank of Cleveland** on April 19th, 2024 as part of the *Economic Scholars Program*. 

### Publishing Author

**John Cullen Nagura McCormick**
> Department of Computer and Data Sciences, Case Western Reserve University  
> Department of Economics, Case Western Reserve University

Senior Capstone partner:
**Dominic Barredo**
> Department of Economics, Case Western Reserve University

### All data processing is done in Python using the following libraries:
* `numpy`
* `pandas`
* `geopandas`

### Geographic definitions for the Healthline:  
Geographic definitions was gathered by hand. The HealthLine definition `LEHD_data/Healthline.kml` and/or `LEHD_data/Healthline.geojson` were manually made. 

HealthLine definition, and area data was then compiled using the open source GIS software `QGIS`

The log of actions to make the 800m buffer can be found in `QGIS_history.log`

### Difference-in-Differences and Triple DiD Regressions:  
Regressions can be found in `stataRegressions.do`

For this project I elected to use the Two-Way Fixed Effects Difference-in-Differences Model (TWFE) to control for differences between tracts and across years. Triple DiD was used to look at interactions of race, and education level with employment effects as a result of the implementation of the HealthLine BRT. 

`reghdfe` was the primary regression command (it allowed for more accurate $R^2$ reporting when running TWFE models.



