"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in matrix:
        row_str = ''
        for col in row:
           row_str += str(col) + '  '
        print(row_str)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for row in range( len(matrix) ):
        for col in range( len(matrix[row]) ):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m2n = [row[:] for row in m2]
    for p in range( len(m1) ):
        for q in range( len(m2[0]) ):
            m2[p][q] = 0
            for r in range( len(m2) ):
                m2[p][q] += m1[p][r] * m2n[r][q]
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
