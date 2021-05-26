import numpy as np

import os
os.system('cls')


class arrayRow_DataStructure():

    def __init__(self, num_columns):
        self.num_columns = num_columns
        self.arr = np.empty((0, self.num_columns))
        return

    def append(self, record):
        self.arr = np.append(self.arr, record, axis=0)

    def delete(self, index):
        self.arr = np.delete(self.arr, index, axis=0)

    def row_size(self):
        return len(self.arr)


people = arrayRow_DataStructure(4)
print(people.arr, people.row_size())
print()


# ==================================================
col_01_first_name = 'Joseph'
col_02_last_name = 'Fischetti'
col_03_eye_color = 'green'
col_04_age = 75

people.append(np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]))

print(people.arr, people.row_size())
print()

# ==================================================
col_01_first_name = 'Mary'
col_02_last_name = 'Smith'
col_03_eye_color = 'blue'
col_04_age = 35

people.append(np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]))

print(people.arr, people.row_size())
print()

# ==================================================
col_01_first_name = 'Susan'
col_02_last_name = 'Mosley'
col_03_eye_color = 'brown'
col_04_age = 16

people.append(np.array([
    [col_01_first_name, col_02_last_name, col_03_eye_color, col_04_age]]))

print(people.arr, people.row_size())
print()

# ==================================================
people.delete((0, 2))
print(people.arr, people.row_size())
print()
