#!/bin/bash

# Default variables
verbosity=0

# User switches
while getopts p:v arg; do
	case "${arg}" in
		p) password=${OPTARG};;
		v) ((verbosity++));;
	esac
done
shift "$(($OPTIND - 1))"


if [[ -f "$@" ]]; then
	of="${@/.pdf/\ \(Protected\).pdf}"

	if [[ -z "$password" ]]; then
		read -s -p "Password:" password
		echo
	fi

	if [[ "$verbosity" -gt 1 ]]; then
		echo "Input File: $@"
		echo "Output File: $of"
		echo "Password: $password"
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
