import sys
import cv2
import math
from PIL import Image

colors = [[0, 0, 0],[157, 157, 157],[255, 255, 255], \
	[190, 38, 51],[224, 111, 139],[73, 60, 43], \
	[164, 100, 34],[235, 137, 49],[247, 226, 107], \
	[47, 72, 78],[68, 137, 26],[163, 206, 39], \
	[27, 38, 50],[0, 87, 132],[49, 162, 242],[178, 220, 239]]

def detect_face(img, cascade):
	rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
	# return a list of (x,y,w,h)
	return rects

def calc_euclidean_dist(p1, p2):
	x = p1[0] - p2[0]
	y = p1[1] - p2[1]
	z = p1[2] - p2[2]

	return math.sqrt(x*x + y*y + z*z)

def find_dominant_color(img):
	w, h = img.size
	pixels = img.getcolors(w * h)
	sorted_pixels = sorted(pixels, key=lambda count: count[0], reverse=True)

	return sorted_pixels

def check_greyscale(pixels):
	color_count = len(pixels)
	if color_count > 10:
		color_count = 10

	greyscale_flag = True
	for i in range(color_count):
		c = pixels[i][1]
		if (math.fabs(c[0] - c[1]) < 10) and \
			(math.fabs(c[0] - c[2]) < 10) and \
			(math.fabs(c[1] - c[2]) < 10):
			continue
		else:
			greyscale_flag = False
			break

	print greyscale_flag

img = cv2.imread(sys.argv[1])
cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

detect_face(img, cascade)

pil_img = Image.open(sys.argv[1])
pixels = find_dominant_color(pil_img)

print pixels[:10]
check_greyscale(pixels)