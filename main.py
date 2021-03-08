from display import *
from draw import *
from matrix import *

screen = new_screen()

# TESTING ROUTINES
m2 = [[],[],[],[]]
print('Testing add edge. Adding (1, 2, 3), (4, 5, 6) m2 = ')
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

m1 = new_matrix()
print('\nTesting ident. m1 = ')
ident(m1)
print_matrix(m1)

print('\nTesting matrix mult. m1 * m2 = ')
print_matrix( matrix_mult(m1, m2) )

# CREATING IMAGE
color = [ 150, 0, 150 ]
matrix1 = new_matrix()
for x in range( XRES ):
    add_edge(matrix1, x, 0, 0, 0, YRES-x, 0)
draw_lines( matrix1, screen, color )

color = [ 230, 230, 0 ]
matrix2 = new_matrix()
for y in range( YRES ):
    add_edge(matrix2, XRES, y, 0, XRES-y, YRES, 0)
draw_lines( matrix2, screen, color )

color = [ 0, 255, 0 ]
matrix3 = new_matrix()
for y in range( YRES, 0, -1 ):
    add_edge(matrix3, XRES, y, 0, y, 0, 0)
draw_lines( matrix3, screen, color )

color = [ 255, 0, 0 ]
matrix4 = new_matrix()
for y in range( YRES ):
    add_edge(matrix4, 0, y, 0, y, YRES, 0)
draw_lines( matrix4, screen, color )

display(screen)
