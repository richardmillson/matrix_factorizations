"""
class Matrix(object):
    def __init__(self, entries):
        self.entries = entries
"""

def size(matrix):
    """
    size() returns the number of rows m and columns n of the given matrix
    """
    if len(matrix) == 0:
        raise ArithmeticError("Matrix is empty")
    else:
        m = len(matrix)
        n = len(matrix[0])
        return m, n

def empty_matrix(m, n):
    """
    empty_matrix() takes two integers m and n as arguments
    and creates a matrix with m rows and n columns
    with elements of type None
    """
    matrix = [[None]*n for i in range(m)]
    return matrix

def transpose(matrix):
    """
    transpose() interchanges the rows and columns
    """
    m, n = size(matrix)
    trans = empty_matrix(n, m)
    for row in range(m):
        for col in range(n):
            trans[col][row] = matrix[row][col]
    return trans

def dot_product(v1, v2):
    product = 0
    if len(v1) != len(v2):
        raise ArithmeticError("Attempting to dot product two vectors of differing lengths")
    elif len(v1) == 0:
        raise ArithmeticError("Attempting to dot product an empty vector")
    else:
        for x in range(len(v1)):
            product += v1[x] * v2[x]
        return product

def cross_product(v1, v2):
    product = empty_matrix(1, 3)
    if ((len(v1) == 1) & (len(v1[0]) == 3)) & ((len(v2) == 1) & (len(v2[0]) == 3)):
        product[0][0] = det([[v1[0][1], v1[0][2]], [v2[0][1], v2[0][2]]])
        product[0][1] = det([[v1[0][0], v1[0][2]], [v2[0][0], v2[0][2]]])
        product[0][2] = det([[v1[0][0], v1[0][1]], [v2[0][0], v2[0][1]]])
        return product
    else:
        raise ArithmeticError("Attempting to cross product two vectors not of length 3")

def scalar_mult(c, A):
    """
    scalar_mult() takes a scalar c and matrix A and returns a matrix
    """
    am, an = size(A)
    mult = empty_matrix(am, an)
    for i in range(am):
        for j in range(an):
            mult[i][j] = c * A[i][j]
    return mult

def mult(A, B):
    am, an = size(A)
    bm, bn = size(B)
    B = transpose(B)
    product = empty_matrix(am, bn)
    if an != bm:
        raise ArithmeticError("Attempting to multiply matrices of incompatible size")
    else:
        for i in range(am):
            for j in range(bn):
                product[i][j] = dot_product(A[i], B[j])
        return product

def det(A):
    m, n = size(A)
    determinant = 0
    if m != n:
        raise ArithmeticError("Attempting to take determinant of a nonsquare matrix")
    elif m < 2:
        raise ArithmeticError("Attempting to take determinant of a single value")
    elif m == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        for i in range(m):
            if i % 2 == 0:
                determinant += det(submatrix(A,i,0))
            elif i % 2 == 1:
                determinant -= det(submatrix(A,i,0))
        return determinant

def submatrix(A, i_exclude, j_exclude):
    """
    submatrix(A,i_exclude,j_exclude) takes a matrix of m rows and n columns
    and returns a matrix of size m-1 by n-1
    where the ith row and jth column have been excluded
    """
    m, n = size(A)
    sub = empty_matrix(m - 1, n - 1)
    for i in range(m):
        if i == i_exclude:
            pass
        elif i < i_exclude:
            for j in range(n):
                if j == j_exclude:
                    pass
                # issue with submatrix pointing to original entries, not copies
                elif j < j_exclude:
                    sub[i][j] = A[i][j]
                elif j > j_exclude:
                    sub[i][j-1] = A[i][j]
        elif i > i_exclude:
            for j in range(n):
                if j == j_exclude:
                    pass
                elif j < j_exclude:
                    sub[i-1][j] = A[i][j]
                elif j > j_exclude:
                    sub[i-1][j-1] = A[i][j]
    return sub

def inverse(mat):
    """
    inverse() takes a matrix A and returns A^-1
    satisfying AA^-1 = I the identity matrix
    """
    m, n = size(mat)
    if (m == 2) & (n == 2):
        inv = scalar_mult(1.0 / det(mat), [[mat[1][1], -mat[0][1]], [-mat[1][0], mat[0][0]]])
        return inv
    elif m == n:
        inv = empty_matrix(m, n)
        for i in range(m):
            inv[i][i] = 1
        for i in range(m):
            #mat[i] = 
            pass
    else:
        raise ArithmeticError("Attempting to take inverse of nonsquare matrix")

def row_mult(c, row):
    """
    row_mult takes a row and multiplies each entry by the scalar c
    """
    new_row = [None] * len(row)
    for j in range(len(row)):
        new_row[j] = c * row[j]
    return new_row

def add(A, B):
    """
    returns the matrix sum of A and B
    """
    am, an = size(A)
    mat_sum = empty_matrix(am, an)
    if size(A) == size(B):
        for i in range(am):
            for j in range(an):
                mat_sum[i][j] = A[i][j] + B[i][j]
        return mat_sum
    else:
        raise ArithmeticError("Attempting to add matrices of differing size")

def row_add(matrix, source, target, multiple):
    """
    row_add() takes the source row, multiplies it by the given mutliple, and adds this to the target row
    """
    mult_source = scalar_mult(multiple, [matrix[source]])
    new_row = add([matrix[target]], mult_source)
    matrix[target] = new_row[0]
    return matrix

def col_add(matrix, source, target, multiple):
    """
    col_add() takes the source column, multiplies it by the given mutliple, and adds this to the target column
    """
    trans = transpose(matrix)
    trans_sum = row_add(trans, source, target, multiple)
    return transpose(trans_sum)

def show_matrix(matrix):
    """
    :type matrix: list
    """
    for row in matrix:
        print row
