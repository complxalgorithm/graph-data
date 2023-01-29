# graph_data
Command line program that collects precipitation data from user, then graphs the data.

# Feature
- Asks user how many months for which they have precipitation data, and then prompts user to enter data (in inches) for each month.
- Asks user whether they want to generate a graph of the data.
- If the user wants to generate a graph, they will be asked whether they want a bar graph, line graph, or a scatter plot.
- A graph will then be generated using the data, and then the graph will open in the user's default browser.

# Requirements
1. Python 3 - download the latest version [here](https://www.python.org/downloads/).
2. Pandas - learn how to install the Pandas library [here](https://pandas.pydata.org/docs/getting_started/install.html).
3. Plotly - learn how to install the Plotly library [here](https://plotly.com/python/getting-started/#installation).

# How to Use
To download the program, you can either clone the repo on your command line
```
git clone https://github.com/complxalgorithm/graph_data.git
```
or download here: https://github.com/complxalgorithm/graph_data/archive/refs/heads/master.zip

To execute, cd into the graph_data directory, and then enter
```
python3 graph_data.py
```

# To-Do
- [ ] Generalize program so non-precipitation data can be graphed
- [ ] Hide 0.5 intervals on y-axis
- [ ] Prompt user whether they want to use inches or cms (or other units such as ft or m)
- [ ] Ask user if the data is correct, and allow them to change the values of the months and precipitation
- [ ] Give user option to add trendline to generated graph (and make it a different color)
- [ ] Give user option to name the graph
- [ ] Give user option to customize axes labels
- [ ] Give user option to save graph from command line into any directory
- [ ] Give user option to display graph as .png, .jpeg, .svg, or .pdf
- [ ] Allow user to use data from .csv or .xls files
- [ ] Allow user to use data that is stored in external databases (e.g. MySQL, PostgreSQL)

# Copyright
&copy; 2023 [Stephen C. Sanders](https://stephensanders.me). Licensed under the <a href="https://github.com/complxalgorithm/graph_data/blob/master/LICENSE">MIT License</a>.