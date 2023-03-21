# Name: stats.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Includes stats related functions: total() and avg()

# total() function - calculates total precipitation
def total(precip, tot):
    # Add up total of precipitation
    for key, val in precip.items():
        val = float(val)
        tot+= val
    
    # Return total to main() function
    return tot

# avg() function - calculates average monthly precipitation
def avg(total, ms):
    return (total / ms)