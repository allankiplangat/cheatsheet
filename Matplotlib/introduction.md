Plotting and Visualization
============

## Alook at python visualizing libraries

- Visualizations is a tool for investigation and communicating of results of computational studies

>**```Matplotlib```**  -> A general purpose visualization library focuses on generating static publication-quality 2D and 3D graphs

>**```Bokeh``` and ```Plotly```** -> Both focuses on interactivity and web connectivity

>**```Seaborn```** -> Hign level plotting library targeting statistical data analysis and is based on Matplotliblibrary

>**```Mayavi```** -> For high quality 3D visualization using the venerable VTK software for heavy dutyscientific visualization

>**```VisPy```** -> OpenGl based 2D and 3D visualization  with great interactivity and connectivity with browser based environments 

## Importing modules

- Matplotlib actually provides multiple enttries to the library
    1. Stateful API
    2. Object-oriented API both provided by the module **```matplotlib.pyplot```**

```python
    # Configures matplotlib to use "inline# backend
    %matplotlib inline 
    # Main Matplotlib module
    import matplotlib as mpl 
    # submodule providing functions that will use to create new figure instances
    import matplotlib.pyplot as plt  
    from mpl_toolkits.mplot3d.axes3d import Axes3D
```