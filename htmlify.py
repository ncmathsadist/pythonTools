#!/usr/bin/python
from sys import argv
from cgi import escape
inFileName = argv[1]
outFileName = inFileName + ".out"
inFilePipe = open(inFileName, "r")
outFilePipe = open(outFileName, "w")
text = inFilePipe.readlines()
for line in text:
	line = escape(line)
	outFilePipe.write(line)
outFilePipe.close()
inFilePipe.close()
