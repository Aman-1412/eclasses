# eclasses

Python2 compatible for the moment

HOW To:
Download this repo and install the requirements using
    python -m pip install -r requirements.txt

##Open gate.py and insert the value of cookie in 5th line

gate.py
scrapes all the download links for the subject mentioned.. 
ALL THE LINKS ARE STORED in the format as follows.. 

Lets say you run the script on the subject aptitude:

Folders created would be
1 Average
2 whatever
3 3rd topic
Etc.. 

In each folder, there will be a textfile with all the scraped links of that topic. 
Ex:
In the folder 1 Average, there will be a textfile
1 average.txt

This textfile contains all the video links from that topic. 

Now, the scraping part is over. 

To be continued (part 2 - downloading)


-*-*-*-*-*-*-*-*-*-*-*-*-**-*


There are two more py files
youtubeplaylistcreator.py
#this is useless now. 


The last py file, takes your 
1 average.txt
and outputs a ready.txt which is a refined list of videos. 

The contents of ready.txt are:
https://player.vimeo.com/...
https://player.vimeo.com/... 
....etc

Or it could be:
https://youtube.com/....
https://youtube.com/... 
....etc

now just run downthemall.bat in the folder and you're all set.
Numbered downloads, with the names. 
Happy downloading

Files you will need:
gate.py
refinedlinks.py
downthemall.bat



#Troubleshooting

52 59 62
Replace[1] with [0] for Index out of bounds error