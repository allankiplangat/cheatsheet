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
  - [Arrays Filled with Incremental Sequences](#arrays-filled-with-incremental-sequences)
  - [Arrays Filled with Logarithmic Sequences](#arrays-filled-with-logarithmic-sequences)
  - [Meshgrid Arrays](#meshgrid-arrays)
  - [Uninitialized Arrays](#uninitialized-arrays)
  - [Creating Arrays with Properties of Other Arrays](#creating-arrays-with-properties-of-other-arrays)

## Arrays Created from Lists and Other Array-Like Objects

>**Function:** 
    <span style="color:red">```np.array```</span>
    
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
    ```np.zeros``` ```np.ones``` ```np.full``` ```np.fill``` ```np.empty```

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
    ```np.full```

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
    ```np.fill```

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
    ```np.empty```

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

## Arrays Filled with Incremental Sequences

>**Usecases** When an array with evenly spaced values between starting and ending values

>**Function:** 
    ```np.arange```
    ```np.linspace```

>**Arguments:** 
    First argument (start value)
    Second argument (end value)
    Third argument (increment/step on the arange & total number of points for linspace)

>**Returns:** NumPy array with evenly spaced values

```python
    # Does not include end value 20

    In [2]: data = np.arange(0, 20, 1)

    In [3]: data
    Out[3]: 
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])

```

```python
    # Includes the end value this behaviour can be changed by using endpoint keyword argument
    # Ideal to be used whenever the increment is a non integer

    In [2]: data = np.linspace(0,10,11)

    In [3]: data
    Out[3]: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])

```

## Arrays Filled with Logarithmic Sequences

**Function:** 
    ```np.logspace```

>**Arguments:** 
    First argument (start value)
    Second argument (end value)
    The 1st and 2nd arguments are powers of the optional base keyword arguments (which defaults to 10)
    Third argument (increment/step ) the increments between the elements are logarithmically distributed

>**Returns:** NumPy array with logarithmically distributed values

```python

    # 5 data points between 10**0 = 1 to 10**2=100
    In [5]: data = np.logspace(0, 2, 5) 

    In [6]: data
    Out[6]: 
    array([  1. , 3.16227766,  10. , 31.6227766 ,1. ])

```

## Meshgrid Arrays
>**Usecase:**
    Evaluate functions over two variables _x_ and _y_
    This can be used when plotting functions over two variables, as color maps plots and contour plots 
    e.g (x+y)^2 

>**Function:** 
    ```np.meshgrid```

>**Arguments:** 
    Arrays

>**Returns:** A Multidimentiona; NumPy array

```python

    In [9]: x = np.array([-1, 0, 1])

    In [10]: y = np.array([-2, 0, 2])

    In [11]: x
    Out[11]: array([-1,  0,  1])

    In [12]: y
    Out[12]: array([-2,  0,  2])

    In [13]: X, Y = np.meshgrid(x, y)

    In [14]: X
    Out[14]: 
    array([[-1,  0,  1],
           [-1,  0,  1],
           [-1,  0,  1]])

    In [15]: Y
    Out[15]: 
    array([[-2, -2, -2],
           [ 0,  0,  0],
           [ 2,  2,  2]])

```

```python

    In [16]: Z = (X + Y) ** 2

    In [17]: Z
    Out[17]: 
    array([[9, 4, 1],
           [1, 0, 1],
           [1, 4, 9]], dtype=int32)

```

> Higher dimensional coordinate arrays can be generated by passing more arrays as arguments to
    ```np.mgrid``` and ```np.ogrid```  Its slightly used a different syntax based on indexing and slice objects

## Uninitialized Arrays
>**Usecase:**
    To create an array of specific size and datatype without initializing the elements

>**Function:** 
    ```np.empty```

>**Arguments:** 
    shape
    dtype

>**Returns:** Numpy array with uninitialized values

```python

    # No guarantee elements have any particular values
    # Actual values vary time to time
    # Advised all values explicitly assigned before array is used 

    In [18]: np.empty((3,4), dtype=np.float)
    Out[18]: 
    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])

```

## Creating Arrays with Properties of Other Arrays
>**Usecase:**
    A function that takes arrays of unspecified type and size and requires working arrays of the same size and type

>**Function:** 
    ```np.ones_like```
    ```np.zeros_like```
    ```np.full_like```
    ```np.empty_like```

```python

    In [19]: def f(x):
    ...:     y = np.ones_like(x)
    ...:     # compute with x and y
    ...:     return y
    ...:     

    In [20]:

```





