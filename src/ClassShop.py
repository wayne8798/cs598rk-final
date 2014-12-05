import cv2
import cv2.cv as cv
from numpy import *

class ImageKit:
	def __init__(self, filename):
		self.img = cv2.imread(filename, cv.CV_LOAD_IMAGE_COLOR)
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
		BLUE = array([255,0,0])
		GREEN = array([0,255,0])
		RED = array([0,0,255])
		BLACK = array([0,0,0])
		WHITE = array([255,255,255])
		if max(abs(pixelVal-BLUE)) <= threshold:
			return 'blue'
		elif max(abs(pixelVal-GREEN)) <= threshold:
			return 'green'
		elif max(abs(pixelVal-RED)) <= threshold:
			return 'red'
		elif max(abs(pixelVal-BLACK)) <= threshold:
			return 'black'
		elif max(abs(pixelVal-WHITE)) <= threshold:
			return 'white'
		else:
			return 'other'

	def isBlack(self, threshold = 20, percentile = 1.0):
		count = 0
		for h in range(self.getHeight()):
			for w in range(self.getWidth()):
				if self.getPixelColor(h,w,threshold) == 'black':
					count += 1
		blackLevel = float(count)/self.getSize()
		#print blackLevel
		if blackLevel >= percentile:
			return True
		else:
			return False

	def isWhite(self, threshold = 20, percentile = 1.0):
		count = 0
		for h in range(self.getHeight()):
			for w in range(self.getWidth()):
				if self.getPixelColor(h,w,threshold) == 'white':
					count += 1
		whiteLevel = float(count)/self.getSize()
		#print whiteLevel
		if whiteLevel >= percentile:
			return True
		else:
			return False


class VideoKit:
	def __init__(self, filename):
		self.vidcap = cv2.VideoCapture(filename)
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

