import sys
sys.path.insert(0, 'libs')
import os
import webapp2
import jinja2
from crawler import crawl_web
from search import search
import pickle

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def main(keyword):
    name = 'youfollowthefilm'
    fname = name + '.pkl'
    domain = 'http://www.' + name + '.com'
    try:
        with open(fname, 'r') as fout:
            website = pickle.load(fout)
    except:
        website = crawl_web(domain)
    return search(website, keyword), website._titles

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class SearchEngine(webapp2.RequestHandler):
    def get(self):
        keyword = self.request.get('keyword')
        results, titles = main(keyword)
        template_values = {'keyword' : keyword, 'results' : results, 'titles' : titles,}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage), ('/results', SearchEngine)], debug=True)
