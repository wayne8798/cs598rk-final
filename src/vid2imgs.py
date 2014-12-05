import sys, os, cv2
from ClassShop import *

input_filename = sys.argv[1].split('/')[-1]
input_dir = sys.argv[1][:-len(input_filename)]
output_dir = input_dir+'../imgs/'+input_filename.split('.')[0]+'/'

if len(sys.argv)-1 >= 2:
	nFrame = int(sys.argv[2])
else:
	nFrame = 1

aVideo = VideoKit(sys.argv[1])

if not os.path.isdir(output_dir):
	os.mkdir(output_dir)
success,image = aVideo.vidcap.read()
countV = 0
countG = 0
while success:
	if countV%nFrame == 0:
		cv2.imwrite(output_dir+"frame%d.jpg" % (countV+1), image)
		#cv2.imwrite(output_dir+"frame%d.jpg" % (countG+1), image)
		countG += 1
	success,image = aVideo.vidcap.read()
	countV += 1
print str(countV)+" frames have been visited!"
print str(countG)+" frames have been generatd!"