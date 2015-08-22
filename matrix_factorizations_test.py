
from matrix_factorizations import *

def test_mult():
    a_mat = [[1, 1, 0], [0, 1, 0]]
    b_mat = [[1], [1], [0]]
    #show_matrix(mult(a_mat, b_mat))
    assert mult(a_mat, b_mat) == [[2], [1]]

def test_submatrix():
    a_mat = [['a', 'b', 'c'], ['d', 'e', 'f'], ['h', 'i', 'j']]
    sub = submatrix(a_mat, 2, 2)
    #show_matrix(sub)
    assert sub == [['a', 'b'], ['d', 'e']]

def test_det():
    a_mat = [[1, 2],
             [2, 2]]
    #print det(a_mat)
    assert det(a_mat) == -2
    b_mat = [[1, 0, 0],
             [0, 1, 2],
             [0, 2, 2]]
    #print det(b_mat)
    assert det(b_mat) == -2

def test_cross_product():
    a_mat = [[1, 0, 0]]
    b_mat = [[0, 1, 0]]
    product = cross_product(a_mat, b_mat)
    #print product
    assert product == [[0, 0, 1]]

def test_scalar_mult():
    a_mat = [[1, 2], [2, 2]]
    #print scalar_mult(2, a_mat)
    assert scalar_mult(2, a_mat) == [[2, 4], [4, 4]]
    b_mat = [[1, 2]]
    assert scalar_mult(2, b_mat) == [[2, 4]]

def test_add():
    a_mat = [[1, 0], [0, 1]]
    b_mat = [[-1, 0], [0, -1]]
    assert add(a_mat, b_mat) == [[0, 0], [0, 0]]

def test_row_add():
    a_mat = [[1, 2], [2, 2]]
    sum_mat = row_add(a_mat, 0, 1, -2)
    assert sum_mat == [[1, 2], [0, -2]]
"""
def test_col_add():
    a_mat = [[1, 2], [2, 2]]
    sum_mat = col_add(a_mat, 0, 1, -2)
    assert sum_mat == [[1, 0], [2, -2]]
"""
def test_inverse():
    a_mat = [[1.0, 2.0], [2.0, 2.0]]
    #print inverse(a_mat)
    #print mult(inverse(a_mat), a_mat)
    #print mult(a_mat, inverse(a_mat))
    assert inverse(a_mat) == [[-1.0, 1.0], [1.0, -0.5]]
    assert mult(inverse(a_mat), a_mat) == [[1.0, 0], [0, 1.0]]
    assert mult(a_mat, inverse(a_mat)) == [[1.0, 0], [0, 1.0]]
    b_mat = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]
    print b_mat
    inverse(b_mat)

def test_init():
    mat_a = Matrix([[1, 0]])
    assert mat_a.entries == [[1, 0]]
    assert mat_a.num_rows == 1
    assert mat_a.num_cols == 2
    mat_b = Matrix([])
    assert mat_b.num_rows == 0
    assert mat_b.num_cols == 0

def test_clone():
    mat_a = Matrix([[1, 2], [2, 2]])
    mat_b = mat_a.clone()
    mat_b.entries[0][0] = 0
    assert mat_b.entries == [[0, 2], [2, 2]]
    assert mat_a.entries[0][0] == 1

def test_identity():
    assert identity(3).entries == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_transpose():
    mat_a = Matrix([[1, 1, 0], [0, 1, 0]])
    mat_a.transpose()
    assert mat_a.entries == [[1, 0], [1, 1], [0, 0]]
    mat_b = Matrix([[1], [1], [0]])
    mat_b.transpose()
    assert mat_b.entries == [[1, 1, 0]]



test_transpose()
test_identity()
test_clone()
test_init()
#test_inverse()
#test_add()
#test_col_add()
#test_row_add()
#test_mult()
#test_submatrix()
#test_det()
#test_cross_product()
#test_scalar_mult()
