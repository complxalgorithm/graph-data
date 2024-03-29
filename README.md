# graph-data
Command line program that collects precipitation data from user, then graphs the data.

This is a work-in-progress. I created this program so that I could learn the Plotly library. More features will be added as time goes on. My main focus is generalizing the program so that non-precipitation data can be collected and graphed.

# Features
- Asks user how many months for which they have precipitation data, and then prompts user to enter data (in inches) for each month.
- Asks user whether they want to generate a graph of the data.
- If the user wants to generate a graph, they will be asked whether they want a bar graph, line graph, or a scatter plot.
- Gives an option to add a trendline on scatter plots.
- Allows user to name the title of their graph, and rename it in case they entered it incorrectly.
- A graph will then be generated using the data, and then the graph will open in the user's default browser.

# Requirements
1. Python 3 - download the latest version [here](https://www.python.org/downloads/).
2. Pandas - learn how to install the Pandas library [here](https://pandas.pydata.org/docs/getting_started/install.html).
3. Plotly - learn how to install the Plotly library [here](https://plotly.com/python/getting-started/#installation).

# How to Use
To download the program, you can either clone the repo on your command line
```
git clone https://github.com/complxalgorithm/graph-data.git
```
or download here: https://github.com/complxalgorithm/graph-data/archive/refs/heads/master.zip

To execute, cd into the graph_data directory, and then enter
```
python3 graph-data.py
```

# To-Do
- [ ] Speed up run time so there isn't a large delay after first executing program
- [X] Modulize the script so it isn't all on one long script file
- [ ] Generalize program so non-precipitation data can be graphed
- [ ] Hide 0.5 intervals on y-axis
- [X] Allow user to choose temporal unit (hour, day, week, month, year)
- [ ] Prompt user whether they want to use inches or cms (or other units such as ft, m, lbs, kgs, etc.)
- [ ] Ask user if the data is correct, and allow them to change data values
- [X] Give user option to add trendline to generated graph
- [ ] Allow user to change color of trendline
- [X] Give user option to name the graph
- [ ] Give user option to customize axes labels
- [ ] Give user option to customize graph font, size, and/or color
- [ ] Give user option to save graph from command line into any directory
- [ ] Give user option to display graph as .png, .jpeg, .svg, or .pdf
- [ ] Add support for data from .csv or .xls files
- [ ] Add support for data from feature classes and shapefiles (ArcGIS, QGIS)
- [ ] Add support for data that is stored in external databases (e.g. MySQL, PostgreSQL)
- [ ] Add support for the generation of multivariate graphs

# Contributing
Contributions are more than welcome. Simply make a pull request for my review. If there are any issues with or suggestions for the program that you may have, create an issue for my review.

I should specify again, though, that I created this program as a way to learn the Plotly library. As such, I would prefer completing the to-do list on my own. However, if you would like to check off anything that is on the to-do list (or add any features that are not on the to-do list), I request that you make helpful comments so that I understand what you did and can learn from it.

# Copyright
&copy; 2023 [Stephen C. Sanders](https://stephensanders.me). Licensed under the <a href="https://github.com/complxalgorithm/graph_data/blob/master/LICENSE">MIT License</a>.