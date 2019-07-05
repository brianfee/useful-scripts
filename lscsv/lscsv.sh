#!/bin/bash

# Set default variables
depth=1
path=.
verbosity=0

# User switches
while getopts d:v arg; do
	case "${arg}" in
		d) depth=${OPTARG};;
		v) ((verbosity++));;
	esac
done
shift "$(($OPTIND - 1))"


# If path exists, override default
if ! [[ -z "$@" ]] && ([[ -f "$@" ]] || [[ -d "$@/" ]]); then
	path=$@

elif [[ -z "$@" ]]; then
	if [[ "$verbosity" -ge 1 ]]; then
		echo "No path specified. Using current directory..."
	fi

else
	echo "Invalid Path..."
	exit
fi

if [[ "$verbosity" -gt 1 ]]; then
	echo "Path:" $path
	echo "Depth:" $depth
	echo "Verbosity:" $verbosity
	echo 
fi

if [[ "$verbosity" -ge 1 ]]; then
	find $path -maxdepth $depth -ls
fi

find $path -maxdepth $depth -ls | python -c "
import sys

csv = []
exportfile = 'filelist.csv'

for line in sys.stdin:
	line = line.strip('\n')
	r = line.split(None, 10)
	fn = r.pop()
	fn = (','.join(r) + ',\"' + fn.replace('\"', '\"\"').replace('\\ ', ' ') + '\"')
	fn = fn.split(',').pop()
	csv.append(fn)

with open(exportfile, 'w') as writer:
	for item in csv:
		writer.write('{}\n'.format(item))
"
