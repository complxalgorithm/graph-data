# Name: data.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Includes data related functions: months(), d(), and separate()

import time  # Used to pause program for short intervals

# temporal() function - user signals what temporal units and the number they have data for
def temporal(t):
    # Show user temporal unit options
    print('The available temporal units are: ')
    time.sleep(0.5)        # Pause program for 1/2 of a second
    for i in t:
        print(i)
        time.sleep(0.5)    # Pause program for 1/2 of a second
    print('\n')            # Blank line so program output looks less clunky 
    
    # Ask user what temporal units they would like to use
    unit = input('Which temporal unit would you like to use? ')
    
    # Validate that temporal unit input is valid
    while unit not in t:
        print(f'ERROR: {unit} is not an option.')
        time.sleep(0.25)        # Pause program for 1/4 of a second
        unit = input('Which temporal unit would you like to use? ')
    
    # Ask user how many of that temporal unit for which they want to enter data
    num = input(f"How many {unit}s do you have data for? ")
    
    # Validate months input is an int
    while not(num.isdigit()):
        print('ERROR: that is not an integer.')
        time.sleep(0.25)    # Pause program for 1/4 of a second
        num = input(f"How many {unit}s do you have data for? ")
    
    # Convert validation input to int
    num = int(num)
    
    # Return valid input to m() function
    return unit, num

# d() function - collects data from user
def d(data, valid, typ, amt):
    # Initialize first input to 1 to interate until the last temporal unit
    n = 1
    
    # Let user enter data for each month, store data in precipitation dict
    while n <= amt:
        # Enter data while validating that the data is numeric
        while valid == False:
            try:
                # Ask for month's data
                data[n] = float(input(f"Enter precipitation in inches for {typ} #" + str(n) + ": "))
            except ValueError:
                print(f'ERROR: your input is not numeric. Please try again')
                time.sleep(0.25)    # Pause program for 1/4 of a second
            else:
                valid = True
        
        # Reset validation variable to False
        valid = False
        
        # Go to next month
        n+=1
    
    # Return data dict to m() function
    return data

# separate() function - splits months and precipitation data into 2 separate lists
# in order to use them as axes in the generated graph
def separate(data):
    # Initialize months and precipitation lists
    times = []
    dat = []
    
    # Add keys and values of dictionary to respective list
    for key, val in data.items():
        times.append(key)
        dat.append(val)
    
    # Return values of lists to m() function    
    return times, dat