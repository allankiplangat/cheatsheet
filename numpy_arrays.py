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

# The numpy array object
"""
Numpy Library is the data structures for representing multidimentional arrays
of homogenious data

Homogeneous referes to all the elements in the array having the same data type

In addition to data stored in the array it contains the metadata about its 

shape, size, data type and other attributes

"""
# Finding information about the array
help(np.ndarray)

# Creating the array
array_attribute = np.array([[1,2],[3,4],[5,6]])

# Checking the type
type(array_attribute)

# Checking the dimentions
array_attribute_dim =  array_attribute.ndim

# Checking the shape of the array
array_attribute_shape = array_attribute.shape

# Checking the size of the array
array_attribute_size = array_attribute.size

# Checking the data type of the array
array_attribute.dtype

# Checking the number of bytes
array_attribute.nbytes

"""
DATA TYPES:
    Since Numpy Arrays are homogeneous all elements have same type
    For numerical work most importdant data types are int float and complex
    they come in different sizes as int32 int 64    
"""

# How to use the dtype attribute to generate arrays of integer, float and 
# Complex valued elements

array_int = np.array([1, 2, 3], dtype=np.int)
array_float = np.array([1, 2, 3], dtype=np.float)
array_complex = np.array([1, 2, 3], dtype=np.complex)

"""
TYPE CASTING:
    Once created the datatype cannot be changed but creating a copy is valid
    with the type casted array values
    
METHODS:
    1. Using the np.array function
    2. Using astype method of the ndarray clas
    
"""

# Type casting an array for method 1
tobecasted = np.array([1, 2, 3], dtype=np.float)
tobecasted.dtype

tobecasted2 = np.array(tobecasted, dtype=np.int)
tobecasted2.dtype

# Type Casting using method  2
casting = np.array([1, 2, 3,], dtype=np.float)
casting2 = casting.astype(np.int)

# Promotion of datatype if required by the operation
promotion = np.array([1, 2, 3], dtype=float)
promotion2 = np.array([1, 2, 3], dtype=complex)

(promotion + promotion2).dtype

# Approprite to set data type either int or complex default is float
# You cant take a squareroot of a negative number

square_root = np.sqrt(np.array([-1, 0, 1]))

# Squareroot of complex number
complex_sqrt = np.sqrt(np.array([-1, 0, 1], dtype=complex))

"""
REAL AND IMAGINARY PARTS:
    All numpy array instance have attributes real and imag for extracting real
    and imaginary parts of the array
    
"""
realimaginary = np.array([1, 2, 3], dtype=complex)

# Extracting the real
realimaginary.real

# Extracting the imaginary
realimaginary.imag