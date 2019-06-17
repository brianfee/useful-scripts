#!/usr/bin/env python3

import argparse
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
	parser = argparse.ArgumentParser(description='Joins two csvs.')
	parser.add_argument('--best-match', action='store_true')

	parser.add_argument('files',
						metavar='file_name', 
						type=str, nargs=2)

	parser.add_argument('column_name',
						metavar='column_name',
						type=str)

	args = parser.parse_args()

	file1 = args.files[0]
	file2 = args.files[1]
	column = args.column_name

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

	# Best Match flag handling
	if args.best_match:
		best_matches = []
		# Get a list of best matches
		for record in data1[column]:
			best_matches.append(best_match(record, data2[column])['value'])

		# Append best matches column to first dataset, 
		data1['best_match'] = best_matches

		# Rename specified column to best matches column within second dataset
		data2.rename(columns = {column: 'best_match'}, inplace = True)
		print(data2)
		merged = data1.merge(data2, on='best_match')

	else:
		merged = data1.merge(data2, on = column)

	merged.to_csv('merged.csv', index = False)
