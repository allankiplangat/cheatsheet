Fundamental principles of Matplotlib
============

## Building a graph

> **Graph**  - Is tructured in terms of **Figure** instance and one or more **Axes** Instances within the figure

> **Figure Instance** - Provides a canvas area for drawing 

> **Axes Instance** - Provides the coordinate systems that are assigned to fixed regions of the total figure

- A **Figure** can contain multiple **Axes** instances e.g  to show multiple panels in a figure, or to show insets within another Axes instance.
- An **Axes** instance can be automatically added to a figure canvas using one of several layout managers provided by Matplotlib.
- An **Axes** instance provides a coordinate system that can be used to plot data in a variety of plot styles e.g graphs, scatterplots, bar plots and many other styles.
- The **Axes** instance also determines how the coordinate axes are displayed. e.g with respect to the axis labels, ticks and ticklabels e.t.c
- When working with matplotlib oop API most functions needed to tune apearance of a graph are methods of the **Axes** class

## Graphing a function (demo to use the API)
- Graphing _y(x) = x^3+5x^2+10_ together with its first and second derivatives over the range _x element of [-5,2]_

> **Workfow:** 

- Creation of the numpy arrays for the x range, 
- Compute the three functions we want to graph. 
- When the data of the graph is prepaired, 
- We need to create Matplotlib **Figure** and **Axes** instances, 
- Use the the **plot** method of the axes instance to plot the data
- Set basic graph properties e.g the **x** and **y** labels with **```set_xlabel```** and **```set_ylabel```** methods 
- Generating a legend using the **```legend```** method




