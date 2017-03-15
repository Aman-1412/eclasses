import requests
import re,os
from bs4 import BeautifulSoup

COOKIE = ""

cookies = {
    'gsScrollPos': '',
    'MoodleSession': COOKIE,
}

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://eclassesbyravindra.com/course/view.php?id=26^&section=9',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

#Replace this number with 'id' of the subject you are scraping
#26 is for aptitude
params = (
    ('id', '26'),
)
#Enter the url of the subject. Here: Aptitude
r = requests.get('http://eclassesbyravindra.com/course/view.php', headers=headers, params=params, cookies=cookies)
soup =  BeautifulSoup(r.content, "html.parser")

#All the topics in that subject. Here: 34
all_topics = soup.find("div",{"class":"course-content"}).find_all('a')

for i in xrange(0, len(all_topics)):
	#URL for each topic and some extra information
	#Example: http://eclassesbyravindra.com/course/view.php?id=26&section=10
	#Example: Partnership
	#Example: 10 .. The number after section=
	topic_link = all_topics[i]['href']
	topic_name = all_topics[i].get_text()
	topic_num = re.findall("\d*$",all_topics[i]['href'])[0]
	try:
		os.mkdir("D:\\Videos\\GATE\\Aptitude\\"+topic_num.strip()+" "+topic_name.strip())
	except:
		pass
	k = requests.get(topic_link, headers=headers, cookies=cookies)
	ksoup = BeautifulSoup(k.content, "html.parser")
	
	#DEBUGGING
	# print len(soup.find_all("ul",{"class":"section img-text"}))
	
	#All the subtopics in the chosen topic. Each subtopic contains 1 video
	all_subtopics = ksoup.find_all("ul",{"class":"section img-text"})[1].find_all('a')
	for j in xrange(len(all_subtopics)):
	
		#DEBUGGING
		# print len(ksoup.find_all("ul",{"class":"section img-text"}))
		
		#Example:  http://eclassesbyravindra.com/mod/page/view.php?id=2499
		subtopic_link = ksoup.find_all("ul",{"class":"section img-text"})[1].find_all('a')[j]['href']
		
		#Example:  Introduction to Partnership
		subtopic_name = ksoup.find_all("ul",{"class":"section img-text"})[1].find_all('a')[j].get_text()
		
		v = requests.get(subtopic_link, headers=headers, cookies=cookies)
		vsoup = BeautifulSoup(v.content, "html.parser")
		
		#Text file in which the links are stored
		textfile = topic_num.strip()+" "+topic_name.strip()+".txt"
		
		#The youtube link of the video
		cur_link = vsoup.find("div",{"role":"main"}).p.iframe['src']
		#Name of the video/subtopic_name
		cur_name = vsoup.find("div",{"role":"main"}).h2.get_text()+ ":"
		print cur_name
		print cur_link
		
		with open("D:\\Videos\\GATE\\Aptitude\\"+topic_num.strip()+" "+topic_name.strip()+"\\"+textfile,"a") as f:
			f.write(str(j+1) + " " + cur_name)
			f.write("\n")
			f.write(cur_link)
			f.write("\n\n")
			
		
		
		
		
		
		
		
		
		
		
		
		
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.get('http://eclassesbyravindra.com/course/view.php?id=26', headers=headers, cookies=cookies)
