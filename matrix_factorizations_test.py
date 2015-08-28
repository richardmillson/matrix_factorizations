
from matrix_factorizations import *

def test_matrix_init():
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

def test_zero():
    assert zero(2, 3).entries == [[0, 0, 0], [0, 0, 0]]

def test_transpose():
    mat_a = Matrix([[1, 1, 0], [0, 1, 0]])
    mat_a.transpose()
    assert mat_a.entries == [[1, 0], [1, 1], [0, 0]]
    mat_b = Matrix([[1], [1], [0]])
    mat_b.transpose()
    assert mat_b.entries == [[1, 1, 0]]

def test_vector_init():
    vec_a = Vector([[1, 2, 0]])
    assert vec_a.entries == [[1, 2, 0]]

def test_dot_product():
    vec_a = Vector([[1, 2, 0]])
    vec_b = Vector([[0, 2, 1]])
    assert vec_a.dot_product(vec_b) == 4

def test_submatrix():
    mat_a = Matrix([['a', 'b', 'c'], ['d', 'e', 'f'], ['h', 'i', 'j']])
    sub = mat_a.submatrix(2, 2)
    assert sub.entries == [['a', 'b'], ['d', 'e']]

def test_det():
    mat_a = Matrix([[1, 2], [2, 2]])
    assert mat_a.det() == -2
    mat_b = Matrix([[1, 0, 0], [0, 1, 2], [0, 2, 2]])
    assert mat_b.det() == -2

def test_cross_product():
    vec_a = Vector([[1, 0, 0]])
    vec_b = Vector([[0, 1, 0]])
    assert vec_a.cross_product(vec_b).entries == [[0, 0, 1]]

def test_scalar_mult():
    mat_a = Matrix([[1, 2], [2, 2]])
    assert mat_a.scalar_mult(2).entries == [[2, 4], [4, 4]]
    mat_b = Matrix([[1, 2]])
    assert mat_b.scalar_mult(2).entries == [[2, 4]]
    vec_a = Vector([[1, 3, 9]])
    assert vec_a.scalar_mult(3).entries == [[3, 9, 27]]

def test_mult():
    mat_a = Matrix([[1, 1, 0], [0, 1, 0]])
    mat_b = Matrix([[1], [1], [0]])
    assert mat_a.mult(mat_b).entries == [[2], [1]]

def test_add():
    mat_a = Matrix([[1, 0], [0, 1]])
    mat_b = Matrix([[-1, 0], [0, -1]])
    assert mat_a.add(mat_b).entries == [[0, 0], [0, 0]]
    vec_a = Vector([[1, 0, 1]])
    vec_b = Vector([[0, 1, 0]])
    assert vec_a.add(vec_b).entries == [[1, 1, 1]]

def test_row_add():
    mat_a = Matrix([[1, 2], [2, 2]])
    mat_a.row_add(0, 1, -2)
    assert mat_a.entries == [[1, 2], [0, -2]]

def test_col_add():
    mat_a = Matrix([[1, 2], [2, 2]])
    mat_a.col_add(0, 1, -2)
    assert mat_a.entries == [[1, 0], [2, -2]]

def test_inverse():
    mat_a = Matrix([[1.0, 2.0], [2.0, 2.0]])
    mat_a_inv = mat_a.inverse()
    assert mat_a_inv.entries == [[-1.0, 1.0], [1.0, -0.5]]
    assert mat_a.mult(mat_a_inv).entries == identity(2).entries
    assert mat_a_inv.mult(mat_a).entries == identity(2).entries
    #mat_b = [[1.0, 0.0, 0.0], [0.0, 1.0, 2.0], [0.0, 2.0, 2.0]]
    #print mat_b.entries
    #mat_b.inverse()



test_inverse()
test_col_add()
test_row_add()
test_add()
test_mult()
test_scalar_mult()
test_cross_product()
test_det()
test_submatrix()
test_dot_product()
test_vector_init()
test_transpose()
test_zero()
test_identity()
test_clone()
test_matrix_init()
