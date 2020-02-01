import numpy as np
"""
    MATRIX VECTOR OPERATIONS:
        Main applications of N-dimetional arrays is to represent the math 
        concepts of **vectors** **matrices** and **tensors**
        
        In this use case, its frequently needed to calculate vector and
        matrix operations
        
np.dot:
    Matrix multiplication (dot product) between two given arrays representing
    vectors, arrays, or tensors.
    
np.inner:
    Scalar multiplication (inner product) between two arrays representing vectors.
    
np.cross:
    The cross product between two arrays that represent vectors.
    
np.tensordot:
    Dot product along specified axes of multidimensional arrays.
    
np.outer:
    Outer product (tensor product of vectors) between two arrays representing 
    vectors.
    
np.kron:
    Kronecker product (tensor product of matrices) between arrays representing
    matrices and higher-dimensional arrays.
    
np.einsum:
    Evaluates Einstein’s summation convention for multidimensional arrays.
    
"""
# computing product of two matrices

A = np.arange(1, 7).reshape(2, 3)
B = np.arange(1, 7).reshape(3, 2) 
        
np.dot(A, B)
np.dot(B, A)

"""
The dot function can also be used for matrix-vector multiplication
(multiplication of 2D array) representing a matrix 1D representing a vector

There is also a corresponding method dot in ndarray

""" 
A = np.arange(9).reshape(3, 3)     
X = np.arange(3)

np.dot(A, X)

# method on the ndarray
A.dot(X)

"""
Non trivial matrix multiplication expressions can become complex and hard to read
when using either np.dot or np.ndarray.dot

e.g matrix for similarity transform A'=BAB-1

Numpy provides an alternative data structure matrix for matrix multiplication
with convinient special attributes like matrix.I for inverse and Matrix.H for
complex conjugate transpose of a matrix

"""

# matrix for similarity transform A'=BAB-1
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

Ap = np.dot(B, np.dot(A, np.linalg.inv(B)))
App = np.dot(B, np.dot(A, np.linalg.inv(B)))


# Using instances of the matrix class

A = np.matrix(A)
B = np.matrix(B)

Ap = B * A * B.I

"""
    NOTE: Using the matrix class does have a few disadvantages (discouraged)
    
    1.  Expresions like A * B is context dependant (not clear is it elementwise
    or matrix) -> Code redability
    
    The np.asmatrix function creates a view of the original array in the form
    of an np.matrix instance
    
    explicitly casting arrays back and forth between ndarray and matrix does 
    offset much of the benefits of the improved readability of matrix 
    expressions
    
    2. Some functions that operate on arrays and matrices might not respect
    the type of input and may return an ndarray even though was called with
    an input argument of type matrix. so a matrix of type matrix might be
    unintentionally converted to ndarray changing behaviour of the expression
    
HINT: 
    Using matrix class instance for complicated matrix expressions is an 
    important use case in this cases its a good idea to explicitly cast arrays
    to matrices before the computation and explicitly cast the result back
    to ndarray type
    
"""
# Demo of Above

A = np.asmatrix(A)
B = np.asmatrix(B)

Ap = B * A * B.I

"""
    Inner product(scalar product) between two arrays representing vectors
    can be computed using the np.inner function
    
    Inner(Mapping two vectors to a scalar)
    Outer(Complementary operation of mapping two vectors to a matrix)
    
"""

x = np.arange(3)

# np.inner (Expects two arguments with same dimension)
np.inner(x, x)

# equivalent to np.dot (Can take input vectors of shape 1 X N and N x 1 )
np.dot(x, x)

y= x[:, np.newaxis]
np.dot(y.T, y)

# Mapping two vectors to a matrix
x = np.array([1, 2, 3])
np.outer(x, x)

"""
    KRONECKER PRODUCT: 
        The outer product can also be calculated using the named product
        function np.kron
        
        In contrast to the outer np.outer produced an output array
        of shape(M*P, N*Q) if the input arrays have shapes (M, N) and (P, Q)
        therefore for the case of two 1D arrays of length M and P the resulting
        array has shape (M*P,)
"""

#kron
np.kron(x, x)

"""
To obtain the result that corresponds to np.outer(x, x) the input array x
must expanded to shape (N, 1) and (1, N) in the first and second argument to
np.kron

"""

np.kron(x[:, np.newaxis], x[np.newaxis, :])

"""
IN GENERAL:
    np.outer primarily intended for vectors as input, the np.kron
    function can be used for computing tensor products of arrays
    of arbitrary dimensio(but both inputs must have the same number of axes)
    
e.g For computing the tensor product of two 2 x 3 matrices

"""

np.kron(np.ones((2, 2)), np.identity(2))

"""
    EINSTEIN SUMMATION CONVENTION:
        Working with multidimensional arrays is often possible to express common
        array operations - in which an implicit summation is assumed over each
        index that occurs multiple times in an expression.
        
        e.g scalr product between two vectors x and y is compactly expressed
        as XnYn, and matrix multiplication of two matrices A and B is expressed
        as AmkBkn.
        
        Numpy np.einsum for carrying einstein summation
        
        First argument -> Index expression
        Second argumet -> Number of arrays included in expression
        
        Index expression is a string with comma separated indices, where each 
        comma separates the indices of each array.
        
        Each array can have any number of indices
        
        e.g Scalr product expression XnYn can be evaluated with np.einsum using
        the expresindex expression "n, n" i.e using np.einsum("n,n, x, y)
        
"""

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

np.einsum("n,n", x,y)
np.inner(x, y)

"""
Similarly for matrix multiplication
AmkBkn can be evaluated usin the np.einsum and the index expression "mk, kn"

"""
A = np.arange(9).reshape(3, 3)
B = A.T

np.einsum("mk,kn", A, B)

np.alltrue(np.einsum("mk,kn", A, B) == np.dot(A, B))

"""
NOTE: 
    
The Einstein summation convention can be particularly convenient when dealing
with multidimensional arrays, since the index expression that defines the operation
makes it explicit which operation is carried out and along which axes it is performed.
An equivalent computation using, for example, np.tensordot might require giving the
axes along which the dot product is to be evaluated.
"""




    
    
    