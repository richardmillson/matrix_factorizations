
class Matrix(object):

    def __init__(self, entries):
        self.entries = entries
        self.num_rows = len(entries)      # number of rows
        if self.num_rows == 0:
            self.num_cols = 0
        else:
            self.num_cols = len(entries[0])   # number of columns

    def clone(self):
        """
        returns a clone of self
        """
        cloned_entries = []
        for i in range(len(self.entries)):
            cloned_entries.append(list(self.entries[i]))
        return Matrix(cloned_entries)

    def transpose(self):
        """
        interchanges the rows and columns
        """
        transposed_entries = []
        for col in range(self.num_cols):
            transposed_entries.append([])
            for row in range(self.num_rows):
                transposed_entries[col].append(self.entries[row][col])
        self.entries = transposed_entries
        new_num_cols = self.num_rows
        new_num_rows = self.num_cols
        self.num_rows = new_num_rows
        self.num_cols = new_num_cols

    def det(self):
        determinant = 0
        if self.num_rows != self.num_cols:
            raise ArithmeticError("Attempting to take determinant of a nonsquare matrix")
        elif self.num_rows < 2:
            raise ArithmeticError("Attempting to take determinant of a single value")
        elif self.num_rows == 2:
            return self.entries[0][0] * self.entries[1][1] - self.entries[0][1] * self.entries[1][0]
        else:
            for i in range(self.num_rows):
                if i % 2 == 0:
                    determinant += self.submatrix(i, 0).det()
                elif i % 2 == 1:
                    determinant -= self.submatrix(i, 0).det()
            return determinant

    def submatrix(self, i_exclude, j_exclude):
        """
        submatrix(A,i_exclude,j_exclude) takes a matrix of m rows and n columns
        and returns a matrix of size m-1 by n-1
        where the ith row and jth column have been excluded
        """
        sub = Matrix([[0] * (self.num_cols - 1) for i in range(self.num_rows - 1)])
        for i in range(self.num_rows):
            if i == i_exclude:
                pass
            elif i < i_exclude:
                for j in range(self.num_cols):
                    if j == j_exclude:
                        pass
                    # issue with submatrix pointing to original entries, not copies
                    elif j < j_exclude:
                        sub.entries[i][j] = self.entries[i][j]
                    elif j > j_exclude:
                        sub.entries[i][j-1] = self.entries[i][j]
            elif i > i_exclude:
                for j in range(self.num_cols):
                    if j == j_exclude:
                        pass
                    elif j < j_exclude:
                        sub.entries[i-1][j] = self.entries[i][j]
                    elif j > j_exclude:
                        sub.entries[i-1][j-1] = self.entries[i][j]
        return sub

    def scalar_mult(self, constant):
        """
        scalar_mult() multiplies each entry of self by constant
        """
        mult = []
        for i in range(self.num_rows):
            mult.append([constant * x for x in self.entries[i]])
        return Matrix(mult)

    def mult(self, other):
        """
        returns the matrix product of self times other
        """
        if self.num_cols != other.num_rows:
            raise ArithmeticError("Attempting to multiply matrices of incompatible size")
        else:
            product = zero(self.num_rows, other.num_cols)
            trans_other = other.clone()
            trans_other.transpose()
            for i in range(product.num_rows):
                for j in range(product.num_cols):
                    product.entries[i][j] = Vector([self.entries[i]]).dot_product(Vector([trans_other.entries[j]]))
            return product

    def add(self, other):
        """
        returns the matrix sum of self and other
        """
        mat_sum = []
        if (self.num_rows == other.num_rows) & (self.num_cols == self.num_cols):
            for i in range(self.num_rows):
                mat_sum.append([sum(x) for x in zip(self.entries[i], other.entries[i])])
            return Matrix(mat_sum)
        else:
            raise ArithmeticError("Attempting to add matrices of differing size")

    def row_add(self, source, target, multiple):
        """
        row_add() takes the source row, multiplies it by the given mutliple, adds this to the target row
        it changes the matrix in place and does not return anything
        """
        mult_source = Vector([self.entries[source]]).scalar_mult(multiple)
        mult_target = Vector([self.entries[target]])
        new_row = mult_target.add(mult_source)
        self.entries[target] = new_row.entries[0]

    def col_add(self, source, target, multiple):
        """
        col_add() takes the source column, multiplies it by the given mutliple, and adds this to the target column
        """
        self.transpose()
        self.row_add(source, target, multiple)
        self.transpose()

    def inverse(self):
        """
        inverse() takes a matrix A and returns A^-1
        satisfying AA^-1 = I the identity matrix
        """
        if (self.num_rows == 2) & (self.num_cols == 2):
            inv = Matrix([[self.entries[1][1], -self.entries[0][1]], [-self.entries[1][0], self.entries[0][0]]]).scalar_mult(1.0 / self.det())
            return inv
        elif self.num_rows == self.num_cols:
            inv = identity(self.num_rows)
            for i in range(self.num_rows):
                if self.entries[i][i] == 0:
                    itom = i + 1
                    while (self.entries[itom][i] == 0) & (itom < m + 1):
                        itom += 1
                    if itom == m + 1:
                        raise ArithmeticError("Attempting to take inverse of noninvertible matrix")
                    else:
                        row_add(inv, itom, i, 1)
                        row_add(mat, itom, i, 1)
                kill_col(inv, i, n)
                kill_col(mat, i, n)
            #print mat, inv
        else:
            raise ArithmeticError("Attempting to take inverse of nonsquare matrix")

    def kill_col(self, row, size):
        matrix[row] = [(1.0 / matrix[row][row]) * x for x in matrix[row]]
        for ith in range(size):
            if row == ith:
                pass
            elif matrix[ith][row] == 0:
                pass
            else:
                row_add(matrix, row, ith, (- 1.0 / matrix[ith][row]))



def identity(size):
    """
    identity() creates a size * size matrix where i == j = 1, i != j = 0
    """
    entries = [[0.0] * size for i in range(size)]
    for diagonal in range(size):
        entries[diagonal][diagonal] = 1.0
    return Matrix(entries)

def zero(num_rows, num_cols):
    """
    zero() returns a matrix of the given size with all entries zero
    """
    zero = Matrix([[0.0] * num_cols for i in range(num_rows)])
    return zero



class Vector(Matrix):

    def __init__(self, entries):
        self.entries = entries
        self.num_rows = len(entries)      # number of rows
        if self.num_rows != 1:
            raise ArithmeticError("Attempting to create a vector that is actually a matrix")
        else:
            self.num_cols = len(entries[0])   # number of columns

    def dot_product(self, other_vector):
        product = 0
        if self.num_cols != other_vector.num_cols:
            raise ArithmeticError("Attempting to dot product two vectors of differing lengths")
        elif self.num_cols == 0:
            raise ArithmeticError("Attempting to dot product an empty vector")
        else:
            for x in range(self.num_cols):
                product += self.entries[0][x] * other_vector.entries[0][x]
            return product

    def cross_product(self, other_vector):
        product = Vector([[None, None, None]])
        if (self.num_cols == 3) & (other_vector.num_cols == 3):
            product.entries[0][0] = Matrix([[self.entries[0][1], self.entries[0][2]], [other_vector.entries[0][1], other_vector.entries[0][2]]]).det()
            product.entries[0][1] = Matrix([[self.entries[0][0], self.entries[0][2]], [other_vector.entries[0][0], other_vector.entries[0][2]]]).det()
            product.entries[0][2] = Matrix([[self.entries[0][0], self.entries[0][1]], [other_vector.entries[0][0], other_vector.entries[0][1]]]).det()
            return product
        else:
            raise ArithmeticError("Attempting to cross product two vectors not of length 3")
