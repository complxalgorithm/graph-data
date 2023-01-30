# Name: graph_data.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# Description: Allows user to enter precipitation data for a specified number of months, and then gives
# the user the option to generate a bar graph, line graph, or scatter plot using the data.
# Requirements: Python3, Pandas, Plotly

# <-- TODO -- >
# 1. Generalize program so non-precipitation data can be graphed
# 2. Hide 0.5 intervals on y-axis
# 3. Prompt user whether they want to use inches or cms (or other units such as ft or m)
# 4. Ask user if the data is correct, and allow them to change the values of the months and precipitation
# 5. Give user option to customize axes labels
# 6. Give user option to display graph as .png, .jpeg, .svg, or .pdf
# 7. Give user option to save graph from command line into any directory as .png, .jpeg, .svg, or .pdf
# 8. Allow user to use data from .csv or .xls files
# 9. Allow user to use data that is stored in external databases (e.g. MySQL, PostgreSQL)
# 10. Allow the generation of multivariate graphs

# Import libraries
import pandas as pd                 # Pandas library - Used for graphing data
import plotly.express as px         # Plotly (Express) library - Used for graphing data
import time                         # Used to pause program for short intervals
#import os                          # Will be used to download graph to computer

# Display welcoming messages, then pause program for a second
print('Welcome to the Graph Data program!')
print('This program will allow you to enter data for a specified number of months.')
print('You will then have the option to generate a bar graph, line graph, or scatter plot with the data.')
time.sleep(1)

# main() function - manages flow of entire program
def main():
    # Initialize variables
    precip = {}          # Initialize dictionary to store data
    mon = 1              # Initialize variable used to run while loop - starts at 1 to signify 1st month
    total = 0            # Initialize total variable
    validate = False     # Initialize validation variable to use for validating numeric precipitation data
    
    # Get from user how many months of data they want to enter
    months = get_months()
    
    # Collect rainfall data
    precipitation = get_precipitation_data(precip, validate, months, mon)
    
    # Calculate total rainfall over specified period of time
    precip_sum = calc_total_precipitation(precipitation, total)
    
    # Calculate average monthly rainfall
    precip_avg = calc_avg_precipitation(precip_sum, months)
    
    # Pause program for 1/4 of a second
    time.sleep(0.25)
    
    # Output stats
    print(f'{precip_sum:.3f} inches of precipitation fell over the course of {months} months.')
    print(f'There was an average of {precip_avg:.3f} inches of precipitation per month.')
    
    # Pause program for 1 second
    time.sleep(1)
    
    # Ask user if they want to generate a graph using the data
    ifGraph = get_graph_status()
    
    # Create and output graph
    if (ifGraph == 'Y') or (ifGraph == 'y'):
        # Allow user to choose a line graph, bar graph, or scatter plot
        graphOption, ifTrendline = get_graph_choice()
        
        # Extract months and precipitation data from precipitation dictionary and separate into
        # individual lists
        months_list, precip_list = separate_data(precipitation)
        
        # Generate a graph, and open it in default browser
        generate_graph(months_list, precip_list, graphOption, ifTrendline)
        
        # Pause program for half a second
        time.sleep(0.5)
    
    # Print salutations
    print('Thank you for using the Graph Data program!')

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

# get_rainfall_data() function - collects data from user
def get_precipitation_data(precip, valid, ms, m):
    # Let user enter data for each month, store data in rainfall dict
    while m <= ms:
        # Enter data while validating that the data is numeric
        while valid == False:
            try:
                # Ask for month's data
                precip[m] = float(input(f"Enter rainfall in inches for month #" + str(m) + ": "))
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

# calc_total_precipitation() function - calculates total rainfall
def calc_total_precipitation(precip, tot):
    # Add up total of rainfall
    for key, val in precip.items():
        val = float(val)
        tot+= val
    
    # Return total to main() function
    return tot

# calc_avg_rainfall() function - calculates average monthly rainfall
def calc_avg_precipitation(total, ms):
    return (total / ms)

# get_graph_status() function - asks user whether they want to graph their data
def get_graph_status():
    # Ask user if they want to generate a graph
    inp = input("Would you like to generate a graph with your data? (Y or N): ")
    
    # Validate user's answer, and keep asking until input is valid
    while (inp != 'Y') and (inp != 'y') and (inp != 'N') and (inp != 'n'):
        print('ERROR: your input is not valid. Please answer with either Y or N.')
        inp = input("Would you like to generate a graph with your data? (Y or N): ")
    
    # Return valid answer to main() function
    return inp

# get_graph_choice() function - user chooses which graph they would like to generate
def get_graph_choice():
    # Ask user which graph they want
    choice = input('Would you like a bar graph (b), line graph (l), or scatter plot (s)? ')
    
    # Validate that user selected one of the options, and ask until they enter valid option
    while (choice.upper() != 'B') and (choice.upper() != 'L') and (choice.upper() != 'S'):
        print (f'ERROR: {choice} is not an option. Please try again.')
        choice = input('Would you like a bar graph (b), line graph (l), or scatter plot (s)? ') 
    
    # Return choice and ifTrendline values to main() function
    if choice.upper() == 'B':
        return 1, ''                       # Bar graph, no trendline
    elif choice.upper() == 'L':
        return 2, ''                       # Line graph, no trendline
    else:
        # Ask user if they want a trendline on their scatter plot
        trendline = input('Would you like to add a trendline to your scatterplot? (Y or N): ')
        
        # Return with trendline choice
        if trendline.upper() == 'Y':
            return 3, 'Y'                  # Scatter plot, with trendline option
        else:
            return 3, 'N'

# separate_data() function - splits months and precipitation data into 2 separate lists
# in order to use them as axes in the generated graph
def separate_data(data):
    # Initialize months and precipitation lists
    months = []
    precip = []
    
    # Add keys and values of dictionary to respective list
    for key, val in data.items():
        months.append(key)
        precip.append(val)
    
    # Return values of lists to main() function    
    return months, precip

# generate_graph() function - creates graph then displays it in default browser
def generate_graph(months, precip, graph, trend):
    # Create graph_title variable and set it to title
    graph_title = input('Enter a name for your graph: ')
    
    # Initialize variables used to validate and end below while loop
    correct = 'N'
    cont = False
    
    # Check to make sure user entered the correct title
    ifTitle = input(f'Is your input of - ' + graph_title + ' - correct? (Y or N): ')
    
    # Validate user gave valid answer, and prompt accordingly
    while cont == False:
        try:
            # Test that ifTitle is a valid answer
            (ifTitle.upper() == 'Y') or (ifTitle.upper() == 'N')
        except:
            # If ifTitle is not valid, tell user and let them answer again until it's valid
            print(f'ERROR: {ifTitle} is not a valid answer. Please try again.')
            ifTitle = input(f'Is your input of - ' + graph_title + ' - correct? (Y or N): ')
        else:
            if ifTitle.upper() == 'N':    # If original title is not correct
                # Ask user to enter the new name for the graph
                graph_title = input('Enter the new name for your graph: ')
            
            # End while loop
            cont = True
    
    # Print that the program is generating a graph
    print('Generating your graph....')
    
    # Create DataFrame object using months data and precipitation data
    df = pd.DataFrame(dict(Month=months, Precipitation=precip))
    
    # Generate graph based on value of opt
    if graph == 1:            # Bar graph
        # Create a bar graph
        fig = px.bar(df, x=df.Month, y=df.Precipitation, title=graph_title)
    elif graph == 2:          # Line graph
        # Create a line graph
        fig = px.line(df, x=df.Month, y=df.Precipitation, title=graph_title)
    else:                     # Scatter plot
        if trend == 'Y':
            # Create a scatter plot with red trendline
            fig = px.scatter(df, x=df.Month, y=df.Precipitation, title=graph_title, 
                            trendline='ols', trendline_color_override="red")
        else:
            # Create a scatter plot without trendline
            fig = px.scatter(df, x=df.Month, y=df.Precipitation, title=graph_title)
    
    # Set x-axis intervals to 1, and y-axis intervals to 0.5
    fig.update_xaxes(tick0=0, dtick=1, showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(tick0=0, dtick=0.5, showline=True, linewidth=1, linecolor='black')
    
    # Force graph's origin to start at (1, 0)
    # Set max x-axis range to last month
    # Set max y-axis range to one more than largest precipitation value (removing the decimal)
    fig.update_layout(
        xaxis_range=[0.5, (float(max(months)) + 0.5)],
        yaxis_range=[0, (int(max(precip)) + 1)]
    )
    
    # Open generated graph in new tab in default browser
    fig.show()
    
    # Pause program for half a second
    time.sleep(0.5)
    
    # Print that the graph was generated succesfully
    print('Your graph was created successfully!')
    
    # Return to main() function
    return

# Run main function
if __name__ == "__main__":
    main()