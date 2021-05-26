# https://youtu.be/9JUAPgtkKpI?t=0

from timeit import default_timer as timer
import numpy as np

import os
os.system('cls')

print('LEARNING NUM_PY\n')
a = np.array([1, 2, 3, 4])
print('            a = np.array([1, 2, 3, 4])\n')
print('version =>', np.__version__)
print(f'a => {a}')
print(f"shape => {a.shape}")
print(f'dtype => {a.dtype}')
print(f'type => {type(a)}')
print(f'ndim => {a.ndim}')
print(f'size => {a.size}')
print(f'itemSize => {a.itemsize}')
print()

print(f'a => {a}')
b = np.array([2, 4, 6, 16])
print(f'b = np.array([2, 4, 6, 16]) => {b}')
b[3] = 8
print(f'b[3] = 8  => {b}')
print(f'b => {b}')

c = 3 + b
print(f'c = 3 + b --- c = {c}')

c = 3 * b
print(f'c = 3 * b --- c = {c}')

c = a + b
print(f'a + b => {c}')

d = np.array([1, 4, 9, 16])
print(f'd = np.array([1,4,9,16]) => {d}')

e = np.sqrt(d)
print(f'e = np.sqrt(d)  => {e}')
print(f'e.dtype => {e.dtype}')
print(f'e.itemsize => {e.itemsize}')
print()

# Python Lists ... DOT Product     AxBx + AyBy = Abs(A)Abs(B)cos(O)
L1 = [1, 2, 3]
L2 = [4, 5, 6]
A1 = np.array(L1)
A2 = np.array(L2)

dot = 0
for i in range(len(L1)):
    dot += L1[i] * L2[i]
print(f'[1, 2, 3] dot [4, 5, 6] => {dot}')

print(f'[1 2 3] dot [4 5 6] => {np.dot(A1, A2)}')
print(f'[1 2 3] @ [4 5 6] => {A1 @ A2}')

print()


a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000


def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot


def dot2():
    return np.dot(a, b)


start = timer()
for i in range(T):
    dot1()
end = timer()
t1 = end - start

start = timer()
for i in range(T):
    dot2()
end = timer()
t2 = end - start

print(f'list calculation time {t1}')
print(f'np.dot calculation time {t2}')
print(f'ratio {t1/t2}')
print('')
