# Lab notes for the Future News Fund analysis

## Loading the data

* We use the data that we have downloaded for our analysis in the project mapping innovation in Scotland.

* Note that this has a discontinuty after 2015 due to changes in the sampling frame to include PAYE units

* We will focus on a small number of 4-digit SIC codes capturing Journalism and TV and Radio Broadcasting

## Analysis

* we have written some functions to analyse the evolution of employment in various sectors related to journalism as well as benchmarks, their geography, and their links with other potentially relevant variables. This shows...
  * Levels of employment in newspaper publishing have declined strongly in recent years
  * Meanwhile, employment in web portals and broadcasting has grown
  * The media sector is becoming more geographically concentrated - a smaller number of locations account for more activity
  * Locations with lower levels of media activity (eg less than 20 people working in journalism) tend to have older and less educated populations, a stronger propensity to have voted leave in the European referendum, lower levels of economic activity and slightly higher suicide rates. This **definitely doens't imply causality** as it might well be that poorer locations have lower demand for media etc. This would be an interesting area for further research.
  
**TODO**
* Review the LAD matches and definitions of variables. In particular, it seems that some LAD names have changed in recent years.
* Some of the health outcome data is quite old (2015) - we should try to find more up to date measures of health outcomes.
* We need to incorporate more variables related to educational outcomes, criminality and corruption in the data.