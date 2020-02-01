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

"""
    ELEMENTWISE FUNCTIONS:
        Numpy provides vectorized functions for elementwise evaluation of 
        many elementary math functions and operations
        
        They take a single array as input and returns a new array of the same
        shape 
        
        The output datatype is not necessarily the same
        
        Many of the mathematical operator functions operates on two input 
        arrays returning one array
        
        Defining new functions:
            1. Express in terms of already existing numpy operations
            2. np.vectorize function
        
        
"""

# np.sin function -> to compute the sin function for all values in the array
x = np.linspace(-1, 1, 11)
y = np.sin(np.pi * x)
# Rounding
rounded = np.round(y, decimals=4)

# Defining new functions that operate on numpy arrays on an elementwise basis
# Heaviside step function (Works for scalar input)
def heaviside(x):
    return 1 if x > 0 else 0

heaviside(-1)
heaviside(1.5)

# This doesnt work for numpy array input
x = np.linspace(-5, 5, 11)

heaviside(x)

heaviside = np.vectorize(heaviside)
heaviside(x)

"""
Using the np.vectorize the scalar Heaviside function can be converted into 
a vectorized function 

It will be relatively be slow since the original function must be called for
each element in the 

NOTE: A more efficient way is to use is to implement this function
using arithmetic with Boolean-valued arrays

However its quick and convinient for scalar input
"""

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


"""
BOOLEAN ARRAYS AND CONDITIONAL EXPRESSIONS:
    
    When computing with NumPy arrays there is need to compare elements
    in different arrays and perform conditional computations based on the 
    result of such comparisons.
    
    Numpy arrays can be used with the usual comparison operators 
    e.g >, <, >=, <=, == and !=
    
    The comparison are made on an element-by-element basis
    
    The broadcasting rules also apply to comparison operators.
    
    If two operators have compatible shapes and sizes, the result of the 
    comparison is a new array with Boolean values(with dtype as np.bool) that
    gives the result of the comparison for each element:
        
    To use the result of comparison between arrays in e.g
    an if statement, we need to agregate the Boolean values of the resulting
    arrays in some suitable fashion to obtain a single True or False
    
    A common Use-case is to apply the np.all or np.any aggregation functions,
    depending on the situation at hand
        
"""

a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

a < b

np.all(a < b)

np.any(a < b)

if np.all(a < b):
    print (" All elements in a are smaller than their corresponding element in b")
elif np.any(a < b):
    print("Some elements in a are smaller than their corresponding element in b")
else:
    print("All elements in b are smaller than their corresponding element in a")


"""

The advantage of Boolean-valued arrays, however, is that they often make it 
possible to avoid conditional if statements

By using Boolean-valued arrays in arithmetic operations, its possible
to write conditional computations in vectorized form

When appearing in arithmetic expressions together with scalar number, or
another NumPy array with a numerical data type, a Boolean array is converted to 
a numerical - value based array with values 0 and 1 in place of False and True
"""

x = np.array([-2, -1, 0, 1, 2])

x > 0

1 * (x > 0)

x * (x > 0)


"""
np.where selects elements from two arrays(2, 3) arguments given a boolean
valued array condition (1) argument

For elements where condition is True, the corrsponding values from the array
given as 2nd argument are selected

If Condition is Flase elements from the 3rd argument array are selected

np.choose takes the 1 argument a list or array with indices that determine 
from which array in a given list of arrays of an element is picked from

np.nonzero returns a tuple of indices that can be used to index the array
(e.g the one that the condition was based on)

Has same result with abs(x) > 2

It uses fancy indexing with the indices return by np.nonzero rather than 
Boolean-valued array indexing

"""

# np.where
x = np.linspace(-4, 4, 9)
np.where(x<0, x**2, x**3)

# np.choose
np.choose([0, 0, 0, 1, 1, 1, 2, 2, 2], [x**2, x**3, x**4])

#np.nonzero
np.nonzero(abs(x) > 2)
x[np.nonzero(abs(x) > 2)]
x[abs(x) > 2]

"""
    SET OPERATIONS:
        Managing unordered collection of unique objects
        
        numpy has functions for operating on sets stored as numpy arrays
        
        using numpy arrays to describe and operate on sets allows expressing
        certain operations in vectorized form
        
        np.in1d function - testing if the values in a numpy array are included
        in a set 
        tests for existance of each element of its first argument in the 
        array passed as the second argument.
"""
# Creates a new array with unique elements, where each value only appears once.
a = np.unique([1, 2, 3, 3])
b = np.unique([2, 3, 4, 4, 5, 6, 5])

# Tests for the existence of an array of elements in another array.
np.in1d(a, b)

# using the in keyword
1 in a
1 in b

# To test if a is a subset of b
np.all(np.in1d(a, b))

# Union (set of elements included in either or both sets)
np.union1d(a, b)

# Intersection(elements included in both sets)
np.intersect1d(a, b)

# difference (elements included on one of the sets but not the other)
np.setdiff1d(a, b)
np.setdiff1d(b, a)

"""
    OPERATIONS ON ARRAYS:
        Some operations acts on arrays as a whole and produce a transformed
        array of the same size
        
        e.g the Transpose which flips the order of the axes of an array
        
        For an arbitrary N-dimensional array the transpose operation 
        reverses all the axes
        
        The transpose function np.transpose also exists as a method in ndarray
        as the special method name ndarray.T
        
        np.flipr(flip left-right)
        np.flipud(flip up down)
        np.rot90
        np.sort
        
"""

data = np.arange(9).reshape(3, 3)
transposed = np.transpose(data)

data = np.random.randn(1, 2, 3, 4, 5)
data.T.shape