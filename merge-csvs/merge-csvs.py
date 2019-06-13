#!/usr/bin/env python3

import pandas as pd
import sys

if __name__ == '__main__':
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	column = sys.argv[3]

	data1 = pd.read_csv(file1)
	data2 = pd.read_csv(file2)

	merged = data1.merge(data2, on=column)
	merged.to_csv('merged.csv', index = False)
