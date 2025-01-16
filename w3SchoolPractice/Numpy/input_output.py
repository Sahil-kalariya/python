import numpy as np
import csv

csv_file_path = 'data.csv'

data_list = []

with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        numeric_row = []
        for element in row:
            try:
                numeric_value = float(element)
                numeric_row.append(numeric_value)
            except ValueError:
                continue
        if numeric_row:
            data_list.append(numeric_row)

data_array = np.array(data_list, dtype=object)

print(data_array)