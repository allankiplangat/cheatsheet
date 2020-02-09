Scalar Vectors and Matrices
=============

## Definitions

> **Scalar** is a constant e.g ```python 3 , 8, 10```

> **Vector** a single **row** or **column** of numbers

> **Matrix** rectangular collection of numbers

#### Creating Scalars Vectors and Matrices

```python
    import numpy as np
    # Creating a vector as a row (one dimentional array)
    In [15]: row_vector = np.array([3, 5, 8, 0])

    In [16]: row_vector
    Out[16]: array([3, 5, 8, 0])


    # Creating a vector as a column (one dim array)
    In [17]: column_vector = np.array([[1],[3],[6],[9]])

    In [18]: column_vector
    Out[18]: 
    array([[1],
        [3],
        [6],
        [9]])

    # Creating a matrix (Use the numpy 2D array)
    In [19]: matrix = np.array([
    ...:         [4, 5],
    ...:         [6, 7],
    ...:         [9, 10],
    ...:         [6, 1] 
    ...:         ])

    In [20]: matrix
    Out[20]: 
    array([[ 4,  5],
        [ 6,  7],
        [ 9, 10],
        [ 6,  1]])
```


## Dimensions

