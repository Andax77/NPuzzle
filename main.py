#!/usr/bin/env python3
import Parse
import sys

def main(av):
	if len(av) != 2:
		print('Need 1 File')
		return
	Parse.parse(av[1])

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exception:
        print('Dude there is an error : ', exception)
