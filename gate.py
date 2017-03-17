import requests
import random
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
proxy_list = ["https://94.177.230.13:4646","http://185.43.210.238:80","https://185.106.121.94:1080","https://5.2.69.102:1080","https://5.2.69.100:1080","http://138.201.186.128:80","https://96.47.235.3:1080","http://121.193.143.249:80","http://200.229.202.72:8080","https://72.11.151.14:1080"]
proxies = {
  'http': random.choice(proxy_list),
  # 'https': random.choice(proxy_list),
}
#Replace this number with 'id' of the subject you are scraping
#26 is for aptitude
params = (
    ('id', '26'),
)
#Enter the url of the subject. Here: Aptitude
r = requests.get('http://eclassesbyravindra.com/course/view.php', headers=headers, params=params, cookies=cookies,proxies=proxies)
soup =  BeautifulSoup(r.content, "html.parser")
subject = soup.find("div",{"id":"page-header"}).h1.get_text()

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
		os.mkdir("D:\\Videos\\GATE\\Set Theory and Algebra\\"+topic_num.strip()+" "+topic_name.strip())
	except:
		pass
	k = requests.get(topic_link, headers=headers, cookies=cookies,proxies=proxies)
	ksoup = BeautifulSoup(k.content, "html.parser")
	
	#DEBUGGING
	# print len(soup.find_all("ul",{"class":"section img-text"}))
	
	#All the subtopics in the chosen topic. Each subtopic contains 1 video
	try:
		all_subtopics = ksoup.find_all("ul",{"class":"section img-text"})[1].find_all('a')
	except:
		all_subtopics = ksoup.find_all("ul",{"class":"section img-text"})[0].find_all('a')
	for j in xrange(len(all_subtopics)):
	
		#DEBUGGING
		# print len(ksoup.find_all("ul",{"class":"section img-text"}))
		
		#Example:  http://eclassesbyravindra.com/mod/page/view.php?id=2499
		subtopic_link = all_subtopics[j]['href']
		
		#Example:  Introduction to Partnership
		subtopic_name = all_subtopics[j].get_text()
		
		v = requests.get(subtopic_link, headers=headers, cookies=cookies,proxies=proxies)
		vsoup = BeautifulSoup(v.content, "html.parser")
		
		#Text file in which the links are stored
		textfile = topic_num.strip()+" "+topic_name.strip()+".txt"
		
		#The youtube link of the video
		cur_link = vsoup.find("div",{"role":"main"}).p.iframe['src']
		#Name of the video/subtopic_name
		cur_name = vsoup.find("div",{"role":"main"}).h2.get_text()+ ":"
		print cur_name
		print cur_link
		
		with open("D:\\Videos\\GATE\\Set Theory and Algebra\\"+topic_num.strip()+" "+topic_name.strip()+"\\"+textfile,"a") as f:
			f.write(str(j+1) + " " + cur_name)
			f.write("\n")
			f.write(cur_link)
			f.write("\n\n")
