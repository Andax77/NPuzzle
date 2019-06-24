#!/usr/bin/env python3
from Boardinfo import BoardInfo
import re

def parse(file):
	fp = open(file)
	line = fp.readline()
	print(line)
	while line.strip()[:1] == '#':
		line = fp.readline()
	count = 1
	info = BoardInfo("Test")
	print(line)
	info.size = line
	while line:
		line = " ".join(line.split()).strip()
		space = 0
		line = re.sub("\#.*$", "",line)
		if (len(line.split()) == info.size):
			print("Perfect")
		print("Line {}: {}".format(count, line))
		line = fp.readline()
		count += 1
	fp.close()
