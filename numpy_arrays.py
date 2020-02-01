import numpy as np

"""
VECTORIZED EXPRESSIONS:
    Storing numerical data ain arrays enables us to process the data with 
    **vectorised expressions**, representing batch operations that are applied
    to all elements in the arrays.
    
    Efficient use if vectorized expression eliminate need of many explicit for 
    loops
    
    * Less verbose code
    * Better maintainability
    * Higher performing code
    
    Many of the functions and operations acts on the array on the elementwise
    basis
    
    Binary operations require all arrays in an expression to be of compatible
    size (Variables in an expression represents either scalars or arrays
    of the same size and shape)
    
    A binary operation between two arrays is well defined if the arrays can
    be broadcasted into the same shape and size
    
    Incase of an operation between a scalar and an array, Broadcasting refers
    to the scalar being distributed and the operation applied to each element 
    in the array
    
    For an expression containing arrays of unequal sizes the operations may
    still be well defined if the smaller of the array can be broadcasted
    ("Effectively expanded") to a much larger array
    
    NumPy BROADCASTIGN RULE: 
        An array can be broadcasted over another array if their **Axes**
        on a one-by-one basis either have the same length or if either of 
        them have length 1.
        
        If the number of axes of the two arrays is not equal the arrays with
        fewer axes is padded with new axes of length 1 from the left until
        the numbers of dimensions of the two arrays agree.
        
"""


"""
    ARITHMETIC OPERATIONS:
        The standard operations with NumPy arrays perform elementwise
        operations.
        
        In operations between scalars and arrays the scalar value is applied 
        to each element in the array
        
        The  dtype of the resulting array for an expression can be promoted 
        if the computation requires it
        
        ValueError:
            If an arithmetic operation is performed on arrays with incompatible 
            size or shape a ValueError is raised
"""

# (+, -, x, /) of Equal-sized arrays
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

X + Y
Y - X
X * Y
Y / X

# Operations between scalars and arrays
X * 2
2 ** X

# Division between an iteger array and an Integer scalar
Y / 2 
(Y / 2).dtype

# ValueError: operands could not be broadcast together with shapes (2,2) (4,)

A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([1, 2, 3, 4])

A / B


C = np.array([[2, 4]])
C.shape

A / C

CC = np.concatenate([C, C], axis=0)
CC

A / CC