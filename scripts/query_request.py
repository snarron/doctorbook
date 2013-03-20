import docbookparse as dp
import json
import urllib
import urllib2
import BeautifulSoup as bs

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

#showsome('Robert J. Glushko')


search_list = []
for query in dp.final_result['Google Search'][:5]:
	link_list = []
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
	req = urllib2.Request(url + query, headers={'User-Agent' : "Magic Browser"}) 
	search_response = urllib2.urlopen(req)
  	search_results = search_response.read()
  	results = json.loads(search_results)
  	data = results['responseData']
  	print 'Total results: %s' % data['cursor']['estimatedResultCount']
  	hits = data['results']
  	print 'Top %d hits:' % len(hits)
  	for h in hits: print ' ', h['url']
  	print 'For more results, see %s' % data['cursor']['moreResultsUrl']
	#q_results = bs.BeautifulSoup(urllib2.urlopen(req))
	#end = q_results.findAll('a')
	#search_list.append(data)

print search_list
#print q_results.read()


"""
for query in dp.final_result['Google Search'][:5]:
	query = query.replace('+', ' ')
	#print query
	showsome(query)
"""