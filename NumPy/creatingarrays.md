Creating Arrays
============

## Arrays Created from Lists and Other Array-Like Objects

>**Function:** np.array

>**Accepted Inputs:** Explicit python lists, Iterable expressions, array-like objects (ndarray instances)

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

- Creating a 2D array with the same data you can use a nested python list

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