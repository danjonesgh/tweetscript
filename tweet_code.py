import urllib2
import re
import threading
from bs4 import BeautifulSoup

def getTweets():
	threading.Timer(5,getTweets).start()
	url = 'https://twitter.com/DaveGeorgeson'
	page = urllib2.urlopen(url).read()
	expression = r'tweet-text">(.*?)</p>'
	tweets = re.findall(expression, page)
	for wordstring in tweets:
		words = wordstring.split()
		for word in words:
			if len(word) > 1:
				if word[0].isupper() and word[1] and word[1].isupper() or word[1].isdigit():
					print word


getTweets (); 
#print fragments
