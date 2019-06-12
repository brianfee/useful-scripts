#!/bin/bash

# User switches
while getopts p: arg; do
	case "${arg}" in
		p) password=${OPTARG};;
	esac
done
shift "$(($OPTIND - 1))"

if [ -f "$@" ]; then
	of="${@/.pdf/\ \(Protected\).pdf}"

	if [ -z "$password" ]; then
		read -s -p "Password:" password
	fi

	pdftk "$@" output "$of" user_pw "$password"
	echo
	echo "Completed. Created File: $of"

else
	echo File does not exist.
fi
