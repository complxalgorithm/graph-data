# Name: main.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Controls the flow of the entire program

# Import modules
import data         # To collect precipitation data with using number of months
import stats        # For precipitation total and average
import graph        # To see if user wants to graph the data or not
import time         # Used to pause program for short intervals

# m() function - executes program
def m():
    # Display welcoming messages, then pause program for a second
    print('Welcome to the Graph Data program!')
    print('This program will allow you to enter data for a specified number of months.')
    print('You will then have the option to generate a bar graph, line graph, or scatter plot with the data.')
    time.sleep(1)
    
    # Initialize variables
    precip = {}          # Initialize dictionary to store data
    mon = 1              # Initialize variable used to run while loop - starts at 1 to signify 1st month
    total = 0            # Initialize total variable
    validate = False     # Initialize validation variable to use for validating numeric precipitation data
    
    # Get from user how many months of data they want to enter
    months = data.months()
    
    # Collect precipitation data
    precipitation = data.d(precip, validate, months, mon)
    
    # Calculate total precipitation over specified period of time
    precip_sum = stats.total(precipitation, total)
    
    # Calculate average monthly precipitation
    precip_avg = stats.avg(precip_sum, months)
    
    # Pause program for 1/4 of a second
    time.sleep(0.25)
    
    # Output stats
    print(f'{precip_sum:.3f} inches of precipitation fell over the course of {months} months.')
    print(f'There was an average of {precip_avg:.3f} inches of precipitation per month.')
    
    # Pause program for 1 second
    time.sleep(1)
    
    # Ask user if they want to generate a graph using the data
    ifGraph = graph.status()
    
    # Create and output graph
    if (ifGraph == 'Y') or (ifGraph == 'y'):
        # Allow user to choose a line graph, bar graph, or scatter plot
        graphOption, ifTrendline = graph.choice()
        
        # Extract months and precipitation data from precipitation dictionary and separate into
        # individual lists
        months_list, precip_list = data.separate(precipitation)
        
        # Generate a graph, and open it in default browser
        graph.generate(months_list, precip_list, graphOption, ifTrendline)
    
    # Pause program for half a second
    time.sleep(0.5)
    
    # Print salutations
    print('Thank you for using the Graph Data program!')