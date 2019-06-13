#!/usr/bin/env python3

import csv
import subprocess
import sys

def import_csv(datafile):
	data = []

	try:
		with open(datafile, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for line in reader:
				data.append(line)

	except FileNotFoundError:
		return None

	return data



if __name__ == '__main__':
	csvFile = str(sys.argv[-1])
	data = import_csv(csvFile)

	for datum in data:
		f = datum['file']
		pwd = datum['password']

		argString = '-p ' + pwd
		subprocess.call(['pdf-protect.sh', argString, f])
