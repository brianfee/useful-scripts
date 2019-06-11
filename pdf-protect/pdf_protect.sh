#!/bin/bash

if [ -f "$@" ]; then
	of="${@/.pdf/\ \(Protected\).pdf}"
	read -s -p "Password:" password
	pdftk "$@" output "$of" user_pw "$password"
	echo
	echo "Completed. Created File: $of"

else
	echo File does not exist.
fi
