#!/usr/bin/env python3

import sys

import parse_file

def main(av):
        args = parse_args.get_args()
        print(args)
	if len(av) != 2:
		print('Need 1 File')
		return
	parse_file.parse(av[1])

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exception:
        print('Dude there is an error : ', exception)
