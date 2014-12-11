import os, sys
from ClassShop import *

if len(sys.argv) < 2:
	print "Error: input video directory not specified!"
else:
	inputDir = sys.argv[1]
	if not inputDir[-1] == '/':
		inputDir += '/'
	for vfile in os.listdir(inputDir):
		if vfile.endswith('.mp4'):
			currentVid = VideoKit(inputDir+vfile)
			currentVid.toImgs(nSec=1)
			currentVid.toImgs(nSec=10)