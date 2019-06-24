#!/usr/bin/env python3
import Parse
import sys

def main(av):
	if len(av) != 2:
		print('Need 1 File')
		return
	Parse.parse(av[1])

main(sys.argv)
