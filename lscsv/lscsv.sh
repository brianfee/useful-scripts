#!/bin/bash

depth=1

while getopts d: arg; do
	case "${arg}" in
		d) depth=${OPTARG};
	esac
done
shift "$(($OPTIND - 1))"

find . -maxdepth $depth -ls | python -c "
import sys

csv = []
exportfile = 'filelist.csv'

for line in sys.stdin:
	line = line.strip('\n')
	r = line.split(None, 10)
	fn = r.pop()
	fn = (','.join(r) + ',\"' + fn.replace('\"', '\"\"') + '\"')
	fn = fn.split(',').pop()
	csv.append(fn)

with open(exportfile, 'w') as writer:
	for item in csv:
		writer.write('{}\n'.format(item))
"
