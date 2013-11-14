import urllib
from bs4 import BeautifulSoup
from storage import Storage
import re
from urlparse import urlparse
from urlparse import urljoin

def get_page(url):
    try:
        return BeautifulSoup(urllib.urlopen(url).read())
    except:
        return BeautifulSoup("")

def get_all_links(page):
    links = []
    for link in page.find_all('a'):
        link_url = link.get('href')
        research = re.search(r"#", str(link_url))
        research2 = re.search(r".jspx", str(link_url))
        if link_url == None or link_url == '#' or link_url[:11] == 'javascript:' or research2 or link_url[-4:] == '.pdf' or research:
            pass
        elif urlparse(link_url)[1] == 'www.duracell.com':
            links.append(link_url)
        elif urlparse(link_url)[1] == "":
            newlink = urljoin('http://www.duracell.com', link_url)
            links.append(newlink)
        else:
            pass
    return links

def crawl_web(seed):
    tocrawl = set([seed])
    crawled = []
    database = Storage()
    while tocrawl: 
        url = tocrawl.pop()
        if url not in crawled:
            print url
            content = get_page(url)
            text = content.get_text()
            text = re.sub(r"[-/']", ' ', text)
            outlinks = get_all_links(content)
            for outlink in outlinks:
                database.add_link(url, outlink)
            punctuation = ".?;,!()|:\""
            for word in text.split():
                word = word.lstrip(punctuation).rstrip(punctuation).lower()
                search = re.search(r"[^a-z0-9]", word)
                if not search and word is not "": #!=
                    database.add_word_occurrence(url, word)
            tocrawl.update(outlinks)
            crawled.append(url)
    return database
