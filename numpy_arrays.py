import numpy as np

"""
INDEXING AND SLICING:
    Works for accessing elements and subarrays of numpy arrays
    Square bracket notation is used
VARIETIES OF INDEX FORMATS:
    In general, the expression within a bracket is a tuple
    where each item in the tuple is a specification which elements to 
    select from each axis/Dimension of the array   
"""

"""
ONE DIMENSIONAL ARRAYS:
    integers : Selects single elements
    slices: Selects ranges and sequences of elements
    
    INT:
    Positive integers: Index elements from the beginning of the array
    negative integers: Indexes elements at the end of an array lats being -1
    
    SLICES:
    Specified using the : notation 
    range can be selected using expression like m:n  starting m ending n-1
    also written explicitly as m:n:1 1-> specifies every element between m and
    n should be selected:  m:n:2 -> Select every second element: m:n:p -> 
    select every p elements. 
    
    if p is negative elements are returned in reverse order starting from m to
    n+1 (m has to be larger than n)
"""

# Indexing Array of axis/dimention 1

array_one = np.arange(0, 11)
array_one
array_one.ndim

array_one[0]  # First element
array_one[-1] # Last Element
array_one[4]  # Fifth Element

# Selecting range of elements
# -> Select from the second to the second to the second-to-last
array_one[1:-1]

#Select every element and every second element
array_one[1:-1:2]

# Select the first 5 and the last 5 
array_one[:5]
array_one[-5:]

# Reversing the array
array_one[::-1]

# Reverse the array and select every second 
array_one[::-2]

"""
MULTIDIMENSIONAL ARRAYS:
    Elements selection discussed above can be applied on each axis/dimension
    The result is a reduced array where each element matches the given 
    selection rules
    
    By applying slice on each of the aray axes, we extract sub arrays
    (Submatrices)
    
    With Element spacing other than 1, Submatrices made up of nonconcesecutive
    elements can be extracted
    
    
"""

f = lambda m, n: n + 10 * m
A = np.fromfunction(f, (6, 6), dtype=int)

# Extracting The Second Column
column_one = A[:, 1] # m columns x n rows

# Extracting the second row
second_row =A[1,:] # m column x n rows

# Upper half diagonal block matrix
upper_half = A[:3, :3]

# Lower left off-diagonal block matrix
lower_left = A[3:,:3]

# Every second element starting from 0, 0
every_second = A[::2, ::2]

# Every second and third element starting from 1,1 
second_third = A[1::2, 1::3]