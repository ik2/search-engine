import urllib
from bs4 import BeautifulSoup
from storage import Storage

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

def get_all_links(page):
    return [link.get('href') for link in BeautifulSoup(page).find_all('a')]

def crawl_web(seed):
    tocrawl = set([seed])
    crawled = []
    database = Storage()
    while tocrawl: 
        url = tocrawl.pop()
        if url not in crawled:
            content = get_page(url)
            outlinks = get_all_links(content)
            for outlink in outlinks:
                database.add_link(url, outlink) 
            for word in content.split():
                database.add_word_occurrence(url, word)
            tocrawl.update(outlinks)
            crawled.append(url)
    return database
