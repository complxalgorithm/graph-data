import time  # Used to pause program for short intervals

# get_months() function - user inputs how many months of data they have
def get_months():
    # Ask user how many months for which they want to enter data
    num = input(f"How many months do you have data for? ")
    
    # Validate months input is an int
    while not(num.isdigit()):
        print(f'ERROR: that is not an integer.')
        time.sleep(0.25)    # Pause program for 1/4 of a second
        num = input(f"How many months do you have data for? ")
    
    # Convert validation input to int
    num = int(num)
    
    # Return valid input to main() function
    return num

# get_data() function - collects data from user
def get_data(precip, valid, ms, m):
    # Let user enter data for each month, store data in precipitation dict
    while m <= ms:
        # Enter data while validating that the data is numeric
        while valid == False:
            try:
                # Ask for month's data
                precip[m] = float(input(f"Enter precipitation in inches for month #" + str(m) + ": "))
            except ValueError:
                print(f'ERROR: your input is not numeric. Please try again')
                time.sleep(0.25)    # Pause program for 1/4 of a second
            else:
                valid = True
        
        # Reset validation variable to False
        valid = False
        
        # Go to next month
        m+=1
    
    # Return data dict to main() function
    return precip

# separate() function - splits months and precipitation data into 2 separate lists
# in order to use them as axes in the generated graph
def separate(data):
    # Initialize months and precipitation lists
    months = []
    precip = []
    
    # Add keys and values of dictionary to respective list
    for key, val in data.items():
        months.append(key)
        precip.append(val)
    
    # Return values of lists to main() function    
    return months, precip