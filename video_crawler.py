import bs4
import urllib
import sys

def process_video_url(url):
	soup = bs4.BeautifulSoup(urllib.urlopen(url).read())
	v = soup.find("video")
	if v != None:
		print v.find_all("source")[1]["src"]

with open(sys.argv[1], 'r') as f:
	html_data = f.read()

soup = bs4.BeautifulSoup(html_data)
for d in soup.find_all("div", class_="project-thumbnail rounded-top clip"):
	url = d.a["href"]
	if url[-13:] == "?ref=category":
		video_url = url[:-13] + "/widget/video.html"
		process_video_url(video_url)
