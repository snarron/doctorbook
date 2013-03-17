import BeautifulSoup as bs
import nltk

# READ_PATH = raw_input('Enter the path to the input resource: ')
# SEARCH_TAG = raw_input("Enter the tag you're looking for: ")

# soup = bs.BeautifulStoneSoup(open(READ_PATH, 'rt').read())

# result_t = []

# for t in soup.findAll('keywords'):
# 	result_t.append(t)

# clean_results = []

# for t in result_t:
# 	clean_results.append(nltk.clean_html(t.prettify()))

# print clean_results

import re
PATH = 'Chapter1.xml'
soup = bs.BeautifulStoneSoup(open(PATH, 'rt').read())

keyword_result = []
author_result = []
indexterm_result = []
orgname_result = []
phrase_result = []

total_result = []

for t in soup.findAll('keyword'):
	keyword_result.append(t)
total_result.append(keyword_result)

for t in soup.findAll('author'):
	author_result.append(t)
total_result.append(author_result)

for t in soup.findAll('indexterm'):
	indexterm_result.append(t)
total_result.append(indexterm_result)

for t in soup.findAll('orgname'):
	orgname_result.append(t)
total_result.append(orgname_result)

for t in soup.findAll('phrase'):
	if t < 30:
		phrase_result.append(t)
total_result.append(phrase_result)

not_quite_clean_results = []

for result_category in total_result:
	for results in result_category:
		#print results
		#print results.prettify()
		not_quite_clean_results.append(re.split(r'[ \t\n]+', nltk.clean_html(results.prettify())))

clean_results = []
for i in not_quite_clean_results:
	clean_results.append(' '.join(i))
print clean_results
