library(devtools)
devtools::install_github("yiluyucheng/dnaMethyAge")
library(dnaMethyAge)

data("subGSE174422")
clock_name <- "HorvathS2013"
horvath_age <- methyAge(betas, clock = clock_name)
write.csv(horvath_age, "HorvathS2013_mAge_results.csv", row.names = FALSE)