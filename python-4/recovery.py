import numpy as np

nines = 99.999999999
secs_per_year = 365*24*60*60
downtime_in_s=secs_per_year-(nines * secs_per_year)/100
print("downtime (mins yr^-1)",downtime_in_s)
print("Expect this to be a loss event every", 1/downtime_in_s, "years")