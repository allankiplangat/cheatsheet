import numpy as np

"""
RESHAPING AND RESIZING:
    Reshaping an array doesnt require modify the underlying array data
    It changes how the data is interpreted y redefining the **strides**
    e.g 2 X 2 matrix reinterreted as a 1 X 4 array (vector)
    
    np.reshape can be used to reconfigure how underlying data is interpreted
    
    The requested new shape of the array should match the number of elements
    in the original size
    
    The number of axes(dimension) dont need to be conserved
    
NOTE: reshaping an array produces a view of the array

If an independent copy of the array is needed the view has to be copied 
explicitly using np.copy() 

np.ravel collapses all the dimensions of an array and returns a flattened 1D
-> Returns a view


ndarray flatten method performs the same function -> Returning a copy

np.ravel and np.flatten collapses the axes of an array into 1D array

INDUCING NEW AXES TO ARRAY:
    1. By using np.reshape
    2. When adding new empty axis
"""

data = np.array([[1,2],[3,4]])

# Reshaping uing np.reshape() method
np.reshape(data, (1, 4))

# Using the reshape()
new_data = data.reshape(4)

# Flattening
flattening = np.array([[1,2], [3,4]])
flatened = flattening.flatten()

#checking the shape
flatened.shape

# Introducing new axes
new_axes = np.arange(0, 5) # One axis

# Indexing with a tuple more than one element
column = new_axes[:, np.newaxis]

row = new_axes[np.newaxis, :] 

# Adding new dimensions to an array
equivalent = np.expand_dims(new_axes, axis=1)
equivalent2 = np.expand_dims(new_axes, axis=0) 

"""
    axis argument above specifies the location relative to existing axes where 
    new axis is to be inserted
    
    MERGING ARRAYS:
        Its often necessary to merge arrays into biger arrays
        
        1. np.vstack - for vertical stacking of rows into a matrix
        2. np.hstack - for horizontal stacking of columns into a matrix
        3. np.concat(axis=0)
        
"""

# Stacking a 1D array vertically
data = np.arange(5)

stacked =  np.vstack((data, data, data))

vdata = np.arange(5)
np.hstack((data, data, data)) # 1D doesnt work

# Make the input array a 2D array of shape (1, 5)
# insert new axis by indexing with
vdata = vdata[:, np.newaxis]
np.hstack((vdata, vdata, vdata))

"""
    NOTE: To  insert  append and remove elements from numpy array
    using the functions np.append, np.insert, np.deelete
    
    New arrays must be created and data copied to it 
    
    Prealocate arrays with size such that they dont need to be resized
    
"""








