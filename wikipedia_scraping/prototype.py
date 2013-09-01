import time
start = time.time()

import wikipedia
import requests

def _wiki_request(**params):
    api_url = "http://mt.wikipedia.org/w/api.php"
    params['format'] = "json"
    params['action'] = "query"
    
    r = requests.get(api_url, params=params)
    return r.json()

wikipedia.wikipedia._wiki_request = _wiki_request

hfile = open('./maltese_wiki','a')

for i in range(1,10000): #around 3000 articles, this should capture
    #most of them
    try:
        random_article =  wikipedia.random()
        page = wikipedia.page(random_article)
        content = page.content
        hfile.write(content.encode('utf8'))
    except:
        pass

print 'It took', time.time()-start, 'seconds.'
