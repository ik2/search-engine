def search(site, keyword, results=None):
    pages = site.lookup((keyword).lower())
    if not pages:
        return None
    pages_ranks = {page : site.page_rank(page) for page in pages}
    pages_sort = sorted(pages_ranks, key=pages_ranks.get, reverse=True)
    return pages_sort[0] if results == 'lucky' else pages_sort
