# total_precipitation() function - calculates total precipitation
def total_precipitation(precip, tot):
    # Add up total of precipitation
    for key, val in precip.items():
        val = float(val)
        tot+= val
    
    # Return total to main() function
    return tot

# avg_precipitation() function - calculates average monthly precipitation
def avg_precipitation(total, ms):
    return (total / ms)