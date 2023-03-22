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
    print('This program will allow you to enter data for a specified number of temporal units.')
    print('You will then have the option to generate a bar graph, line graph, or scatter plot with the data.')
    print('\n')             # Blank line so program output looks less clunky
    time.sleep(1.5)
    
    # Initialize variables
    data_dict = {}          # Initialize dictionary to store data
    validate = False        # Initialize validation variable to use for validating numeric precipitation data
    time_units = ['hour', 'day', 'week', 'month', 'year']
    
    # Get from user how temporal units and how many of that unit they have data for
    time_type, time_num = data.temporal(time_units)
    
    # Collect data
    dat = data.d(data_dict, validate, time_type, time_num)
    
    # Calculate total precipitation over specified period of time
    data_sum = stats.total(dat)
    
    # Calculate average monthly precipitation
    data_avg = stats.avg(data_sum, time_num)
    
    # Pause program for 1/4 of a second
    time.sleep(0.25)
    
    # Output stats
    print(f'{data_sum:.3f} inches of precipitation fell over the course of {time_num} {time_type}s.')
    print(f'There was an average of {data_avg:.3f} inches of precipitation per {time_type}.')
    print('\n')        # Blank line so program output looks less clunky
    
    # Pause program for 1 second
    time.sleep(1)
    
    # Ask user if they want to generate a graph using the data
    ifGraph = graph.status()
    
    # Create and output graph
    if ifGraph.upper() == 'Y':
        # Allow user to choose a line graph, bar graph, or scatter plot
        graphOption, ifTrendline = graph.choice()
        
        # Extract months and precipitation data from precipitation dictionary and separate into
        # individual lists
        time_list, data_list = data.separate(dat)
        
        # Generate a graph, and open it in default browser
        graph.generate(time_list, data_list, graphOption, ifTrendline, time_type)
    
    # Pause program for half a second
    time.sleep(0.5)
    
    # Print salutations
    print('Thank you for using the Graph Data program!')