from crawler import crawl_web
from search import search

def main():
    print "Testing..."
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'
    my_site = crawl_web('http://udacity.com/cs101x/urank/index.html')
    assert search(my_site, 'Hummus', 'lucky') == kathleen
    assert search(my_site, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    assert search(my_site, 'the', 'lucky') == nickel
    assert search(my_site, 'the') == [nickel, arsenic, hummus, indexurl]
    assert search(my_site, 'babaganoush', 'lucky') == None
    assert search(my_site, 'babaganoush') == None
    print "Finished tests."

if __name__ == '__main__':
    main()
