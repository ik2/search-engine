from crawler import crawl_web
from search import search
import pickle

def main():
    name = 'youfollowthefilm'
    fname = name + '.pkl'
    domain = 'http://www.' + name + '.com'
    try:
        with open(fname, 'r') as fout:
            website = pickle.load(fout)
            print "Succesfully read my_site from " + fname
    except:
        website = crawl_web(domain)
        try:
            with open(fname, 'w') as fout:
                pickle.dump(website, fout)
                print "Succesfully wrote my_site to " + fname
        except IOError, e:
            print "Cannot write out my_site: " + str(e)
    print search(website, 'landscape')
    return website._titles

if __name__ == '__main__':
    main()
