import bs4
import urllib
import sys

with open(sys.argv[1], 'r') as f:
	html_data = f.read()

output = open('percent.dat', 'w')

soup = bs4.BeautifulSoup(html_data)
count = 0
for d in soup.find_all("div", class_="project-thumbnail rounded-top clip"):
	url = d.a["href"]
	if url[-13:] == "?ref=category":
		video = bs4.BeautifulSoup(urllib.urlopen(url).read()).find("video")
		if video == None:
			continue

		page_soup = bs4.BeautifulSoup(urllib.urlopen(url).read())
		goal = page_soup.find(id="pledged")["data-goal"]
		pledged = page_soup.find(id="pledged")["data-pledged"]
		percent = page_soup.find(id="pledged")["data-percent-raised"]

		output.write("{} {}\n".format(count, percent))

		print "{}: {}".format(count, url)

		count += 1
		if count >= 200:
			break

output.close()