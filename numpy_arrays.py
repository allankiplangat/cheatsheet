"""
THE NUMPY ARRAY OJECT:
    
"""
import numpy as np
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