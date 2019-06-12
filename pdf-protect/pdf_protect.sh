#!/bin/bash

# Default variables
outputFlag=0
verbosity=0

# User switches
while getopts o:p:v arg; do
	case "${arg}" in
		o) of=${OPTARG};;
		p) password=${OPTARG};;
		v) ((verbosity++));;
	esac
done
shift "$(($OPTIND - 1))"


if [[ -f "$@" ]]; then
	if [[ -z "$of" ]]; then
		of="${@/.pdf/\ \(Protected\).pdf}"
	fi

	if [[ -z "$password" ]]; then
		read -s -p "Password:" password
		echo
	fi

	if [[ "$verbosity" -gt 1 ]]; then
		echo "Input File: $@"
		echo "Output File: $of"
		if [[ "$verbosity" -gt 2 ]]; then echo "Password: $password"; fi
		echo "Verbosity: $verbosity"
		echo
	fi

	pdftk "$@" output "$of" user_pw "$password"

	if ! [[ -f "$of" ]]; then
		echo "Error during file creation."
		exit

	elif [[ "$verbosity" -ge 1 ]]; then
		echo "Completed. Created File: $of"
	fi

else
	echo File does not exist.
fi
