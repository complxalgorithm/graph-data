# Name: stats.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Includes stats related functions: total() and avg()

# total() function - calculates total precipitation
def total(precip):
    # Initialize tot variable to add sum to
    tot = 0
    
    # Add up total of precipitation
    for key, val in precip.items():
        val = float(val)
        tot += val
    
    # Return total to m() function
    return tot

# avg() function - calculates average monthly precipitation
def avg(total, time):
    return (total / time)