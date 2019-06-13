#!/usr/bin/env python3

import pandas as pd
import sys


if __name__ == '__main__':
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	column = sys.argv[3]

	try:
		data1 = pd.read_csv(file1)
	except FileNotFoundError:
		print('File:', file1, 'not found. Exiting...')
		quit()

	try:
		data2 = pd.read_csv(file2)
	except FileNotFoundError:
		print('File:', file2, 'not found. Exiting...')
		quit()

	if column not in data1.columns:
		print(column, 'is not a valid column name in', file1)
		quit()
	elif column not in data2.columns:
		print(column, 'is not a valid column name in', file2)
		quit()

	merged = data1.merge(data2, on=column)
	merged.to_csv('merged.csv', index = False)
