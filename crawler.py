import urllib
from bs4 import BeautifulSoup
from storage import Storage
import re

def get_page(url):
    try:
        return BeautifulSoup(urllib.urlopen(url).read())
    except:
        return ""

def get_all_links(page):
    links = [link.get('href') for link in page.find_all('a')]
    links2 = []
    for link in links:
        try:
            if str(link)[-4:] == '.php':
                links2.append('http://www.youfollowthefilm.com/'+link)
        except:
            print "Error"
    return links2

def crawl_web(seed):
    tocrawl = set([seed])
    crawled = []
    database = Storage()
    while tocrawl: 
        url = tocrawl.pop()
        if url not in crawled:
            content = get_page(url)
            text = content.get_text()
            text = re.sub(r"[-/']", ' ', text)
            text = re.sub(ur'[\u0932\u094b\u0917\u092a\u0930\u093f\u0926\u0943\u0936\u094d\u092f\u0938\u094d\u0925\u093e\u0928\u0915\u0930\u094d\u092e\u091a\u093e\u0930\u0940\u201c\u2013\u2019\u092b\u201d]', ' ', text)
            outlinks = get_all_links(content)
            for outlink in outlinks:
                database.add_link(url, outlink)
            punctuation = ".?;,!()|:\""
            for word in text.split():
                word = word.lstrip(punctuation).rstrip(punctuation).lower()
                search = re.search(r"[^a-z0-9]", word)
                if not search and word != "":
                    database.add_word_occurrence(url, word)
            tocrawl.update(outlinks)
            crawled.append(url)
    return database
