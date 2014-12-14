import os, sys
from ClassShop import *

#T = 1
T = 10
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
		f.write("@ATTRIBUTE\tblackcount\tNUMERIC\n")
		f.write("@ATTRIBUTE\twhitecount\tNUMERIC\n")
		f.write("@ATTRIBUTE\tgrayscount\tNUMERIC\n")
		f.write("@ATTRIBUTE\tfacecount\tNUMERIC\n")
		f.write("@ATTRIBUTE\tfaceavelocx\tNUMERIC\n")
		f.write("@ATTRIBUTE\tfaceavelocy\tNUMERIC\n")
		f.write("@ATTRIBUTE\tfacesumarea\tNUMERIC\n")
		f.write("@DATA\n")
		for vfile in os.listdir(inputDir):
			if vfile.endswith('.mp4'):
				print "==> Analyzing "+vfile
				cVID = VideoKit(inputDir+vfile)
				f.write(str(cVID.getFrameWidth())+",")
				f.write(str(cVID.getFrameHeight())+",")
				f.write(str(cVID.getFPS())+",")
				f.write(str(cVID.getDuration())+",")
				f.write(str(cVID.getFrameCount())+",")
				cVID_NAME = vfile.split('.')[0]
				cVID_IMGFOLDER = inputDir+'../imgs/'+cVID_NAME+str(T)+'/'
				cIMG_BlackCount = 0
				cIMG_WhiteCount = 0
				cIMG_GraysacleCount = 0
				cIMG_FaceCount = 0
				cIMG_FaceAveLocation = [0,0]
				cIMG_FaceSumArea = 0
				for ifile in os.listdir(cVID_IMGFOLDER):
					if ifile.endswith('.jpg'):
						cIMG = ImageKit(cVID_IMGFOLDER+ifile)
						if cIMG.isBlack():
							cIMG_BlackCount += 1
						if cIMG.isWhite():
							cIMG_WhiteCount += 1
						if cIMG.isGrayscale():
							cIMG_GraysacleCount += 1
						cIMG_FaceCount += cIMG.getNfaces()
						faceCenters = cIMG.getFaceCenters()
						faceAreas = cIMG.getFaceAreas()
						for i in range(cIMG.getNfaces()):
							cIMG_FaceAveLocation[0] += faceCenters[i][0]
							cIMG_FaceAveLocation[1] += faceCenters[i][1]
							cIMG_FaceSumArea += faceAreas[i]
				if cIMG_FaceCount == 0:
					cIMG_FaceAveLocation[0] = -1
					cIMG_FaceAveLocation[1] = -1
				else:
					cIMG_FaceAveLocation[0] /= cIMG_FaceCount
					cIMG_FaceAveLocation[1] /= cIMG_FaceCount
				f.write(str(cIMG_BlackCount)+",")
				f.write(str(cIMG_WhiteCount)+",")
				f.write(str(cIMG_GraysacleCount)+",")
				f.write(str(cIMG_FaceCount)+",")
				f.write(str(cIMG_FaceAveLocation[0])+",")
				f.write(str(cIMG_FaceAveLocation[1])+",")
				f.write(str(cIMG_FaceSumArea)+"\n")
