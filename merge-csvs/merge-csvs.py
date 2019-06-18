#!/usr/bin/env python3

import argparse
import pandas as pd
import sys

from difflib import SequenceMatcher as SM


def best_match(text, comparison_list):
	best = {'ratio': None, 'value': None}

	for item in comparison_list:
		ratio = SM(None, text.lower(), item.lower()).ratio()
		if best['ratio'] is None or ratio > best['ratio']:
			best['ratio'] = ratio
			best['value'] = item

	return best



def load_csv(fileName):
	try:
		data = pd.read_csv(fileName)
	except FileNotFoundError:
		print('File:', fileName, 'not found...')
		return None
	
	return data



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Joins two csvs.')
	parser.add_argument('--best-match', action='store_true')
	parser.add_argument('files', metavar='file_name', type=str, nargs=2)
	parser.add_argument('column', metavar='column_name', type=str, nargs='+')

	args = parser.parse_args()

	file1 = args.files[0]
	file2 = args.files[1]

	try:
		col1 = args.column[0]
		col2 = args.column[1]
	except IndexError:
		col1 = args.column[0]
		col2 = args.column[0]

	# Load CSV files
	data1 = load_csv(file1)
	data2 = load_csv(file2)

	if data1 is None or data2 is None:
		print('Exiting...')
		quit()


	if col1 not in data1.columns:
		print(col1, 'is not a valid column name in', file1)
		quit()
	elif col2 not in data2.columns:
		print(col2, 'is not a valid column name in', file2)
		quit()

	# Best Match flag handling
	if args.best_match:
		best_matches = []
		# Get a list of best matches
		for record in data1[col1]:
			best_matches.append(best_match(record, data2[col2])['value'])

		# Append best matches column to first dataset, 
		data1['best_match'] = best_matches

		# Rename specified column to best matches column within second dataset
		data2.rename(columns = {col2: 'best_match'}, inplace = True)
		merged = data1.merge(data2, on='best_match')

	else:
		merged = data1.merge(data2, on = col1)

	merged.to_csv('merged.csv', index = False)
