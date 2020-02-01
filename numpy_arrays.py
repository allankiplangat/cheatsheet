import numpy as np

"""
AGGREGATE FUNCTIONS:
    Includes functions for calculating agregates for NumPy arrays
    It takes an array as input and by default returns a scalar as an output  
    
    By default they aggregate over the entire input array
    
    using axis keyword argument with the functions, and their corresponding 
    ndarray methods, you can control over which axis in the array aggregation
    is carried out
    
    The axis argument can be an integer which specifies the axis to aggregate
    values over
    
    In many cases the axis argument can be a tuple of integers, which specifies
    multiple axes to aggregate over.
"""


# Getting the mean
data = np.random.normal(size=(15,15))
np.mean(data)
data.mean()

# calling the aggregate np.sum function 
data = np.random.normal(size=(5, 10, 15))

data2 = data.sum(axis=0)

data.sum(axis=0).shape

data.sum(axis=(0, 2)).shape

data.sum()

# Aggregation over all elements
data3 = np.arange(1, 10).reshape(3,3)
data4 = data3.sum() # Sums all elements
data5 = data3.sum(axis=0)
data6 = data3.sum(axis=1)