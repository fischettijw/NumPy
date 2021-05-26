# https://youtu.be/9JUAPgtkKpI?t=1065

import numpy as np

import os
os.system('cls')

print('LEARNING NUM_PY\n')

a = np.array([[1, 2], [4, 5], [7, 8]])
print('       a = np.array([[1, 2], [4, 5], [7, 8]])\n')
print('version =>', np.__version__)
print(f'a => \n{a}')
print(f"shape => {a.shape}")
print(f'dtype => {a.dtype}')
print(f'type => {type(a)}')
print(f'ndim => {a.ndim}')
print(f'size => {a.size}')
print(f'itemSize => {a.itemsize}')
print()

print(f'a => \n{a}\n')
print(f'a[1][0] => {a[1][0]}')
print(f'a[1, 0] => {a[1, 0]}')
print(f'a[0] => {a[0]}')
print()

# numpy transpose matrix
print(f'a.T => \n{a.T}')
print()

# numpy inverse matrix.
b = np.array([[1, 2], [4, 5]])
print(f'b = np.array([[1, 2], [4, 5]]) =>\n{np.array([[1, 2], [4, 5]])}\n')
print(
    f'np.linalg.inv(b) => \n{np.linalg.inv(b)}')
print()

# numpy inverse matrix.
c = np.array([[1, 9, 3], [4, 5, 8], [3, 8, 9]])
print(f'c = np.array([[1, 9, 3], [4, 5, 8], [3, 8, 9]]) =>\n{c}\n')
print(
    f'np.linalg.inv(c) =>\n{np.linalg.inv(c)}')
print()
