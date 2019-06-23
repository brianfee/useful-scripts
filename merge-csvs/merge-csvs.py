#!/usr/bin/env python3

import pandas as pd


def best_match(text, comparison_list):
	from difflib import SequenceMatcher as SM

	bestRatio = None
	bestValue = None

	text = text.lower()

	for item in comparison_list:
		x = item.lower()
		ratio = SM(None, text, x).ratio()

		ratio += text_in_string_ratio(x, text)
		ratio = round(ratio, 3)

		if bestRatio is None or ratio > bestRatio:
			bestRatio = ratio
			bestValue = item

	return bestRatio, bestValue



def text_in_string_ratio(text, string):
	def partial_word_match(w1, w2):
		for i in reversed(range(3, len(w1) + 1)):
			if w1[:i] in w2:
				return i / len(w1)
		return 0


	overall_ratio = 0
	textLength = len(text.replace(' ', ''))

	for w1 in text.split(' '):
		match_ratio = 0

		for w2 in string.split(' '):
			if args.partial_matching:
				match_ratio = partial_word_match(w1, w2)

			elif w1 == w2:
				match_ratio = 1

			overall_ratio += len(w1) * match_ratio

	return overall_ratio / textLength



def load_csv(fileName):
	try:
		data = pd.read_csv(fileName)
	except FileNotFoundError:
		print('File:', fileName, 'not found...')
		return None

	return data



def parse_arguments():
	import argparse

	parser = argparse.ArgumentParser(description='Joins two csvs.',
				usage='%(prog)s [OPTIONS] FILE FILE COLUMN [COLUMN2]')

	# Short Arguments
	parser.add_argument('-r', '--include-ratio', action='store_true')
	parser.add_argument('-t', '--ratio-threshold', type=float,
						metavar='THRESHOLD')

	# Long Arguments
	parser.add_argument('--best-match', action='store_true')
	parser.add_argument('--join-type', type=str, default='inner',
						metavar='JOIN')
	parser.add_argument('--partial-matching', action='store_true')

	# Positional Arguments
	parser.add_argument('input_files', metavar='Files', type=str, nargs=2)
	parser.add_argument('col1', metavar='Match Column', type=str)
	parser.add_argument('col2', metavar='[2nd File Match Column]', type=str,
						nargs='?')

	return parser.parse_args()



def main(args):
	file1 = args.input_files[0]
	file2 = args.input_files[1]

	col1 = args.col1
	col2 = args.col1 if args.col2 is None else args.col2

	threshold = args.ratio_threshold
	thresholdFlag = True if threshold is not None else False

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
		best_ratios = []

		# Get a list of best matches
		for record in data1[col1]:
			best_record = best_match(record, data2[col2])

			if thresholdFlag and best_record[0] < threshold:
				best_ratios.append(None)
				best_matches.append(None)
			else:
				best_ratios.append(best_record[0])
				best_matches.append(best_record[1])

		# Append best matches column to first dataset,
		if args.include_ratio:
			data1['ratio'] = best_ratios

		data1['best_match'] = best_matches

		# Rename specified column to best matches column within second dataset
		data2.rename(columns = {col2: 'best_match'}, inplace = True)
		merged = data1.merge(data2, how=args.join_type, on='best_match')

	else:
		merged = data1.merge(data2, on = col1)

	merged.to_csv('merged.csv', index = False)
	return



if __name__ == '__main__':
	args = parse_arguments()
	main(args)

