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