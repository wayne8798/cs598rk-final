import bs4
import urllib
import sys

def process_video_url(url, count):
	soup = bs4.BeautifulSoup(urllib.urlopen(url).read())
	v = soup.find("video")
	if v != None:
		url = v.find_all("source")[1]["src"]
		file_name = "videos/{}.mp4".format(str(count))
		urllib.urlretrieve(url, file_name)

		return True
	else:
		return False

with open(sys.argv[1], 'r') as f:
	html_data = f.read()

soup = bs4.BeautifulSoup(html_data)
count = 0
for d in soup.find_all("div", class_="project-thumbnail rounded-top clip"):
	url = d.a["href"]
	if url[-13:] == "?ref=category":
		video_url = url[:-13] + "/widget/video.html"
		if process_video_url(video_url, count) == True:
			print url[:-13]
			soup = bs4.BeautifulSoup(urllib.urlopen(url).read())
			goal = soup.find(id="pledged")["data-goal"]
			pledged = soup.find(id="pledged")["data-pledged"]
			percent = soup.find(id="pledged")["data-percent-raised"]
			if soup.findAll("div", {"class": "poll stat"})[0].get_text()[1] == "0":
				finished = True
			else:
				finished = False

			if finished == True:
				print "This project is finished."
				if percent >= 1:
					print "Success!"
				else:
					print "Sorry..."
			else:
				print "This project is not finished."
			count += 1
	