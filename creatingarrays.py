"""
CREATING ARRAYS:
    
"""
import numpy as np

# Arrays created from list and other array like objects 

array_one = np.array([1,2,3,4])
array_one

# Array filled with constant values
zeros_array = np.zeros((10, 5))
zeros_array

# Array of ones
ones_array = np.ones((3,5), dtype=np.int16)
ones_array

# Filling the array
to_fill = 5.4*np.ones(10)
filled = np.full(10, 5.5)

# Empty Arrays ( Uninitialized array)
empty_array = np.empty((4,5))
empty_array

# square matrix with one along the diagonals
array_eye = np.eye(5)
array_eye

# identity matrix
identity_matrix = np.identity(4)
identity_matrix

# Optional offset
offset_matrix = np.eye(3, k=1)
offset_matrix

# Diagonal Matrix
diagonal_matrix = np.diag(np.arange(0, 20, 5))
diagonal_matrix
# Arrays with Incremental steps
array_odds = np.arange(3, 30, 2)
array_odds

increased = np.linspace(0, 10, 11)
increased

# Two dimentional arrays (matrix)
array_2d = np.array([(1,2,3),(4,5,6)])
array_2d

# Determining the dimention of an array
shape = array_2d.shape
shape

# Reshaping arrays
tobe_reshaped = np.arange(6)
reshaped = tobe_reshaped.reshape(2,3)

# Create an array with the dimentions of anothe array filling with ones
array_like = np.ones_like(reshaped)
array_like

# Arrays filled with logarithmic sequences
log_space = np.logspace(0, 2, 5)
log_space

# Creating Meshgrid arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
x
y
X, Y = np.meshgrid(x, y)
