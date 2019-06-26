#!/usr/bin/env python3
from Boardinfo import BoardInfo
import re
import sys

def parse(file):
	fp = open(file)
	line = fp.readline()
	while line.strip()[:1] == '#':
		line = fp.readline()
	info = BoardInfo()
	info.size = int(line)
	countLine = 0
	line = fp.readline()
	while line:
		line = " ".join(re.sub("\#.*$", "",line).split()).strip()
		space = 0
		if countLine < info.size and bool(re.search("[^0-9\s]", line)):
			sys.exit("Error Map Syntax !")
		for f in line.split():
			if countLine < info.size:
				info.tab.insert(int(f))
		if ((len(line.strip().split()) == info.size) and countLine <= info.size):
			countLine += 1
			if countLine > info.size:
				sys.exit("Error Map Size !")
		line = fp.readline()
	fp.close()
	info.tab.show()
	return info
