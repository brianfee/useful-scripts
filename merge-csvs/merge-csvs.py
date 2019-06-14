#!/usr/bin/env python3

import pandas as pd
import sys

from difflib import SequenceMatcher as SM

def best_match(text, comparison_list):
	best = {'ratio': None, 'value': None}

	for item in comparison_list:
		ratio = SM(None, text, item).ratio()
		if best['ratio'] is None or ratio > best['ratio']:
			best['ratio'] = ratio
			best['value'] = item

	return best


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
