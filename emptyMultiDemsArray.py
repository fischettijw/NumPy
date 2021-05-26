import numpy as np

import os
os.system('cls')

# Create an empty Numpy array with 4 columns or 0 rows
arr = np.empty((0, 4), int)
print('Empty 2D Numpy array:')
print(arr)
print()

''''
Now to append a new row to this empty
2D Numpy array, we can use the numpy.append().
But we need to pass the row as a numpy array
of same shape only, and pass axis=0, 
so that it can be appended along the column,
'''

# Append a row to the 2D numpy array
arr = np.append(arr, np.array([[11, 21, 31, 41]]), axis=0)
# Append 2nd rows to the 2D Numpy array
arr = np.append(arr, np.array([[15, 25, 35, 45]]), axis=0)
print('2D Numpy array:')
print(arr)
print()

people = np.empty((0, 4))
print(people)

# ==================================================
col_01_first_name = 'Joseph'
col_02_last_name = 'Fischetti'
col_03_eye_color = 'green'
col_04_age = 75

people = np.append(people, np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]), axis=0)
print(people)
print()

# ==================================================
col_01_first_name = 'Mary'
col_02_last_name = 'Smith'
col_03_eye_color = 'blue'
col_04_age = 35

people = np.append(people, np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]), axis=0)
print(people)
print()

# ==================================================
col_01_first_name = 'Susan'
col_02_last_name = 'Mosley'
col_03_eye_color = 'brown'
col_04_age = 16

people = np.append(people, np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]), axis=0)
print(people)
print()
