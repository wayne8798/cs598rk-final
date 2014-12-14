import os, cv2
import cv2.cv as cv
from numpy import *
from PIL import Image

class ImageKit:
	def __init__(self, imgpath):
		self.imgName = imgpath.split('/')[-1]
		self.imgDir = imgpath[:-len(self.imgName)]
		self.img = cv2.imread(imgpath, cv.CV_LOAD_IMAGE_COLOR)
		if self.img == None:
			print "Warning: self.img == None!"

	def getWidth(self):
		return len(self.img[0])

	def getHeight(self):
		return len(self.img)

	def getSize(self):
		return self.getWidth()*self.getHeight()

	def getChannelCount(self):
		return len(self.img[0][0])

	def getPixelValue(self, height, weight): # start from 0
		return self.img[height][weight]

	def getPixelColor(self, height, weight, threshold): # start from 0
		pixelVal = int64(self.getPixelValue(height, weight))
		BLACK = array([0,0,0])
		WHITE = array([255,255,255])
		#BLUE = array([255,0,0])
		#GREEN = array([0,255,0])
		#RED = array([0,0,255])
		if max(abs(pixelVal-BLACK)) <= threshold:
			return 'black'
		elif max(abs(pixelVal-WHITE)) <= threshold:
			return 'white'
		#elif max(abs(pixelVal-BLUE)) <= threshold:
		#	return 'blue'
		#elif max(abs(pixelVal-GREEN)) <= threshold:
		#	return 'green'
		#elif max(abs(pixelVal-RED)) <= threshold:
		#	return 'red'
		else:
			return 'other'

	def isBlack(self, threshold = 20, percentile = 1.0):
		count = 0
		for h in range(self.getHeight()):
			for w in range(self.getWidth()):
				if not self.getPixelColor(h,w,threshold) == 'black':
					count += 1
					if float(count)/self.getSize() > (1-percentile):
						return False
		return True

	def isWhite(self, threshold = 20, percentile = 1.0):
		count = 0
		for h in range(self.getHeight()):
			for w in range(self.getWidth()):
				if not self.getPixelColor(h,w,threshold) == 'white':
					count += 1
					if float(count)/self.getSize() > (1-percentile):
						return False
		return True

	def detectFace(self):
		cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
		return cascade.detectMultiScale(self.img, 1.3, 4, cv.CV_HAAR_SCALE_IMAGE, (20,20))

	def getNfaces(self):
		return len(self.detectFace())

	def getFaceCenters(self):
		faceCenters = []
		faces = self.detectFace()
		for i in range(len(faces)):
			cface = faces[i]
			faceCenters.append((cface[0]+cface[2]/2, cface[1]+cface[3]/2))
		return faceCenters

	def getFaceAreas(self):
		faceAreas = []
		faces = self.detectFace()
		for i in range(len(faces)):
			cface = faces[i]
			faceAreas.append(cface[2]*cface[3])
		return faceAreas

	def sortedColors(self):
		PILimg = Image.open(self.imgDir+self.imgName)
		w,h = PILimg.size
		return sorted(PILimg.getcolors(w*h), key=lambda count: count[0], reverse=True)

	def getDominantColors(self, Ndomcolor=10):
		return self.sortedColors()[0:Ndomcolor]

	def isGrayscale(self, threshold=10):
		domColors = self.getDominantColors(10)
		for i in range(len(domColors)):
			c = domColors[i][1]
			if abs(c[0]-c[1])>threshold or abs(c[1]-c[2])>threshold or abs(c[2]-c[0])>threshold:
				return False
		return True

class VideoKit:
	def __init__(self, vidpath):
		self.vidName = vidpath.split('/')[-1]
		self.vidDir = vidpath[:-len(self.vidName)]
		self.vidcap = cv2.VideoCapture(vidpath)
		if self.vidcap == None:
			print "Warning: self.vidcap == None!"

	def getFrameWidth(self):
		return self.vidcap.get(cv.CV_CAP_PROP_FRAME_WIDTH)

	def getFrameHeight(self):
		return self.vidcap.get(cv.CV_CAP_PROP_FRAME_HEIGHT)

	def getDef(self):
		return self.getFrameWidth(), self.getFrameHeight()

	def getFPS(self):
		return round(self.vidcap.get(cv.CV_CAP_PROP_FPS),-1)

	def getDuration(self):
		return round(self.vidcap.get(cv.CV_CAP_PROP_FRAME_COUNT)/self.vidcap.get(cv.CV_CAP_PROP_FPS))

	def getFrameCount(self):
		return self.getFPS()*self.getDuration()

	def toImgs(self, nSec=-1):
		if nSec == -1:
			outputDir = self.vidDir+'../imgs/'+self.vidName.split('.')[0]+'/'
			nFrame = 1
			tiLabel = "["+self.vidName+" / frame]"
		else:
			outputDir = self.vidDir+'../imgs/'+self.vidName.split('.')[0]+str(nSec)+'/'
			nFrame = nSec*self.getFPS()
			tiLabel = "["+self.vidName+" / "+str(nSec)+"sec]"
		if not os.path.isdir(outputDir):
			os.mkdir(outputDir)
		success,image = self.vidcap.read()
		count = 0
		while success:
			if count%nFrame == 0:
				cv2.imwrite(outputDir+"frame%d.jpg" % (count+1), image)
			success,image = self.vidcap.read()
			count += 1
		self.vidcap = cv2.VideoCapture(self.vidDir+self.vidName)
		if count == self.getFrameCount():
			print "Success: "+tiLabel+" video to images completed!"
		else:
			print "Failure: "+tiLabel+" frame count error!"
