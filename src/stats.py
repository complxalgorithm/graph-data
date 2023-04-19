# Name: stats.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Includes stats related functions: total() and avg()

# total() function - calculates total precipitation
def total(data):
    # Initialize tot variable to add sum to
    tot = 0
    
    # Add up total of all data
    for key, val in data.items():
        val = float(val)
        tot += val
    
    # Return total to m() function
    return tot

# avg() function - calculates average
def avg(total, time):
    return (total / time)