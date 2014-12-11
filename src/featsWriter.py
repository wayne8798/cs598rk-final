import os, sys
from ClassShop import *

if len(sys.argv) < 2:
	print "Error: input video directory not specified!"
else:
	inputDir = sys.argv[1]
	if not inputDir[-1] == '/':
		inputDir += '/'
	with open(inputDir+'../feats/allvids.arff', 'wb') as f:
		f.write("@ATTRIBUTE\tframewidth\tNUMERIC\n")
		f.write("@ATTRIBUTE\tframeheigth\tNUMERIC\n")
		f.write("@ATTRIBUTE\tframepersec\tNUMERIC\n")
		f.write("@ATTRIBUTE\tduration\tNUMERIC\n")
		f.write("@ATTRIBUTE\tframecount\tNUMERIC\n")
		f.write("@DATA\n")
		for vfile in os.listdir(inputDir):
			if vfile.endswith('.mp4'):
				currentVid = VideoKit(inputDir+vfile)
				f.write(str(currentVid.getFrameWidth())+",")
				f.write(str(currentVid.getFrameHeight())+",")
				f.write(str(currentVid.getFPS())+",")
				f.write(str(currentVid.getDuration())+",")
				f.write(str(currentVid.getFrameCount())+"\n")
				