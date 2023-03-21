# Name: graph-data.py
# Author: Stephen C. Sanders <https://stephensanders.me>
# License: MIT
# Description: Allows user to enter precipitation data for a specified number of months, and then gives
# the user the option to generate a bar graph, line graph, or scatter plot using the data.
# Requirements: Python3, Pandas, Plotly, Kaleido

# Import libraries needed to import modules from src directory
import os
import sys
import inspect
import time

# Determine current path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Add src directory to end of path
sys.path.insert(1, os.path.join(sys.path[0], 'src'))

# Import main module from src directory
import main

# Execute main function
if __name__ == "__main__":
    main.main()