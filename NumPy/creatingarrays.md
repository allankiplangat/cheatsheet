Creating Arrays
============

- [Creating Arrays](#creating-arrays)
  - [Arrays Created from Lists and Other Array-Like Objects](#arrays-created-from-lists-and-other-array-like-objects)
      - [1D Array](#1d-array)
      - [2D Array](#2d-array)
  - [Arrays Filled with Constant Values](#arrays-filled-with-constant-values)
      - [Zeros](#zeros)
      - [ones](#ones)
      - [Any constant value](#any-constant-value)
      - [Filling an already created array](#filling-an-already-created-array)
      - [Filling an array with uninitialized values](#filling-an-array-with-uninitialized-values)

## Arrays Created from Lists and Other Array-Like Objects

>**Function:** 
    np.array

>**Arguments:** 
    Explicit python lists, Iterable expressions, array-like objects (ndarray instances)

>**Returns:** 
    NumPy array containing the passed data

#### 1D Array

```python

    In [3]: data = np.array([1, 2, 3, 4])

    In [4]: data
    Out[4]: array([1, 2, 3, 4])

    In [5]: data.ndim
    Out[5]: 1

    In [6]: data.shape
    Out[6]: (4,)

```

#### 2D Array

- Nested sequences, like a list of equal-length lists, will be converted into a multidimensional array

```python

    In [17]: data = np.array([[1, 2],[3, 4]])

    In [18]: data
    Out[18]: 
    array([[1, 2],
           [3, 4]])

    In [19]: data.ndim
    Out[19]: 2

    In [20]: data.shape
    Out[20]: (2, 2)

```

## Arrays Filled with Constant Values

>**Functions:** 
    np.zeros and np.ones np.full np.fill np.empty

>**Arguments:** 
    1. First argument (shape) - ``int`` for **1D** or ```tuple```  describing number of elements along each dimension of the array e.e (2,3)
    2. Optional keyword argument to specify the data type for elements in array default ```type=float64```


>**Returns:** NumPy array filled with the specified shape

#### Zeros

```python

    In [22]: data = np.zeros((2,3))

    In [23]: data
    Out[23]: 
    array([[0., 0., 0.],
           [0., 0., 0.]])

    In [24]: data.ndim
    Out[24]: 2

    In [25]: data.shape
    Out[25]: (2, 3)

```

#### ones

```python

    In [27]: data = np.ones(4)

    In [28]: data
    Out[28]: array([1., 1., 1., 1.])

    In [29]: data.ndim
    Out[29]: 1

    In [30]: data.shape
    Out[30]: (4,)

```
#### Any constant value

>**Function:** 
    np.full

>**Arguments:** 
    1. First argument (shape) - ``int`` for **1D** or ```tuple```  describing number of elements along each dimension of the array e.e (2, 3)
    2. Fill value

>**Returns:** NumPy array filled with the desired fill value

- Method 1:

```python

    In [32]: data = np.full((4,4),2.6)

    In [33]: data
    Out[33]: 
    array([[2.6, 2.6, 2.6, 2.6],
           [2.6, 2.6, 2.6, 2.6],
           [2.6, 2.6, 2.6, 2.6],
           [2.6, 2.6, 2.6, 2.6]])

    In [34]: data.ndim
    Out[34]: 2

    In [35]: data.shape
    Out[35]: (4, 4)

```

- Method 2

```python

    In [37]: data = np.ones((4,4))

    In [38]: data
    Out[38]: 
    array([[1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.]])

    In [39]: data * 1.6
    Out[39]: 
    array([[1.6, 1.6, 1.6, 1.6],
           [1.6, 1.6, 1.6, 1.6],
           [1.6, 1.6, 1.6, 1.6],
           [1.6, 1.6, 1.6, 1.6]])

```
#### Filling an already created array

>**Function:** 
    np.fill

>**Arguments:** 
    First argument (value)

>**Returns:** NumPy array filled with the desired fill value

```python
    In [41]: data = np.zeros((4,4))

    In [41]: 

    In [42]: data = np.zeros((4,4))

    In [43]: data
    Out[43]: 
    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])

    In [44]: data.fill(1.8)

    In [45]: data
    Out[45]: 
    array([[1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8]])

```

#### Filling an array with uninitialized values

>**Function:** 
    np.empty

>**Arguments:** 
    First argument (value)

>**Returns:** NumPy array filled with uninitialized values

**_NOTE: This function should only be used when the initialization of all elements can be quaranteed by other means e.g an explicit loop or assignment_**

```python

    In [50]: data = np.empty((4,4))

    In [51]: data
    Out[51]: 
    array([[1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8],
           [1.8, 1.8, 1.8, 1.8]])

    In [52]: data.fill(0.5)

    In [53]: data
    Out[53]: 
    array([[0.5, 0.5, 0.5, 0.5],
           [0.5, 0.5, 0.5, 0.5],
           [0.5, 0.5, 0.5, 0.5],
           [0.5, 0.5, 0.5, 0.5]])

```

