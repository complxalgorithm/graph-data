# Name: graph.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Includes graphing related functions: status(), choice(), and generate()

# Import graphing libraries
import pandas as pd                 # Pandas library - Used for graphing data
import plotly.express as px         # Plotly (Express) library - Used for graphing data
#import kaleido                     # Will be used to download graph as png or other file

# status() function - asks user whether they want to graph their data
def status():
    # Ask user if they want to generate a graph
    inp = input("Would you like to generate a graph with your data? (Y or N): ")
    
    # Validate user's answer, and keep asking until input is valid
    while (inp.upper() != 'Y') and (inp.upper() != 'N'):
        print('ERROR: your input is not valid. Please answer with either Y or N.')
        inp = input("Would you like to generate a graph with your data? (Y or N): ")
    
    # Return valid answer to main() function
    return inp

# choice() function - user chooses which graph they would like to generate
def choice():
    # Ask user which graph they want
    choice = input('Would you like a bar graph (b), line graph (l), or scatter plot (s)? ')
    
    # Validate that user selected one of the options, and ask until they enter valid option
    while (choice.upper() != 'B') and (choice.upper() != 'L') and (choice.upper() != 'S'):
        print (f'ERROR: {choice} is not an option. Please try again.')
        choice = input('Would you like a bar graph (b), line graph (l), or scatter plot (s)? ') 
    
    # Return choice and ifTrendline values to m() function
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

# generate() function - creates graph then displays it in default browser
def generate(times, data, graph, trend, typ):
    # Initialize origin_zero variable to use in determining where to start graph origin
    origin_zero = True
    
    # Capitalize time type for use as x-axis label
    typ = typ.capitalize()
    
    # Create graph_title variable and set it to title
    graph_title = input('Enter a name for your graph: ')
    
    # Initialize variables used to validate and end below while loop
    correct = 'N'
    cont = False
    
    # Check to make sure user entered the correct title
    ifTitle = input(f'Is your input of : {graph_title} : correct? (Y or N): ')
    
    # Validate user gave valid answer, and prompt accordingly
    while cont == False:
        try:
            # Test that ifTitle is a valid answer
            (ifTitle.upper() == 'Y') or (ifTitle.upper() == 'N')
        except:
            # If ifTitle is not valid, tell user and let them answer again until it's valid
            print(f'ERROR: {ifTitle} is not a valid answer. Please try again.')
            ifTitle = input(f'Is your input of : {graph_title} : correct? (Y or N): ')
        else:
            if ifTitle.upper() == 'N':    # If original title is not correct
                # Ask user to enter the new name for the graph
                graph_title = input('Enter the new name for your graph: ')
            
            # End while loop
            cont = True
    
    # Update user that the graph is being generated
    print('Generating your graph....')
    
    # Create DataFrame object using months data and precipitation data
    df = pd.DataFrame(dict(typ=times, Precipitation=data))
    
    # Generate graph based on value of graphOption
    if graph == 1:            # Bar graph
        # Create a bar graph
        fig = px.bar(df, x=df.typ, y=df.Precipitation, title=graph_title)
    elif graph == 2:          # Line graph
        # Create a line graph
        fig = px.line(df, x=df.typ, y=df.Precipitation, title=graph_title)
    else:                     # Scatter plot
        if trend == 'Y':
            # Create a scatter plot with red trendline
            fig = px.scatter(df, x=df.typ, y=df.Precipitation, title=graph_title, 
                            trendline='ols', trendline_color_override="red")
        else:
            # Create a scatter plot without trendline
            fig = px.scatter(df, x=df.typ, y=df.Precipitation, title=graph_title)
    
    # Set x-axis intervals to 1, and y-axis intervals to 0.5
    fig.update_xaxes(tick0=0, dtick=1, showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(tick0=0, dtick=0.5, showline=True, linewidth=1, linecolor='black')
    
    # Determine origin of the graph
    if min(data) < 2:
        # Force graph's origin to start at (1, 0) if the lowest data entry is less than 2.5
        # Set max x-axis range to last month
        # Set max y-axis range to one more than largest precipitation value (removing the decimal)
        fig.update_layout(
            xaxis_range=[0.5, (float(max(times)) + 0.5)],
            yaxis_range=[0, (int(max(data)) + 1)]
        )
    else:
        # Otherwise, set y-axis start point to lowest data entry value minus the decimal
        fig.update_layout(
            xaxis_range=[0.5, (float(max(times)) + 0.5)],
            yaxis_range=[(int(min(data))), (int(max(data)) + 1)]
        )
    
    # Set font size of y-axis depending on distance between the min and max data values
    if (max(data) - min(data)) > 25:
        fig.update_layout(
            yaxis = dict(
                tickfont = dict(size=8)
            )
        )
    
    # Update x-axis label to reflect the chosen temporal unit
    fig.update_layout(
        xaxis_title=typ
    )
    
    # Open generated graph in new tab in default browser
    fig.show()
    
    # Print that the graph was generated succesfully
    print('Your graph was created successfully!')
    
    # Return to m() function
    return