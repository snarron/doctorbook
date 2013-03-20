import BeautifulSoup as bs
import nltk
import re
import pandas as pd
import set_path

soup = bs.BeautifulStoneSoup(open(set_path.PATH, 'rt').read())

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

def search_terms(soup):
	# Declare variables.
	keyword_result = []
	author_result = []
	indexterm_result = []
	orgname_result = []
	phrase_result = []

	total_result = []
	result_category_list = []

	# Start searching.
	for t in soup.findAll('keyword'):
		keyword_result.append(t)
		result_category_list.append('keyword')
	total_result.append(keyword_result)

	for t in soup.findAll('author'):
		author_result.append(t)
		result_category_list.append('author')
	total_result.append(author_result)

	for t in soup.findAll('indexterm'):
		indexterm_result.append(t)
		result_category_list.append('indexterm')
	total_result.append(indexterm_result)

	for t in soup.findAll('orgname'):
		orgname_result.append(t)
		result_category_list.append('orgname')
	total_result.append(orgname_result)

	for t in soup.findAll('phrase'):
		phrase_result.append(t)
		result_category_list.append('phrase')
	total_result.append(phrase_result)

	return total_result, result_category_list

## Cleans up total_result and results_category_list.
## Returns a list of combinations of key terms and their categries.
def not_really_clean_results(total_result, results_category_list):
	not_quite_clean_results = []

	for result_category in total_result:
		for results in result_category:
			#print results
			#print results.prettify()
			not_quite_clean_results.append(re.split(r'[ \t\n]+', nltk.clean_html(results.prettify())))
	return not_quite_clean_results

## Cleans up not_quite_clean_results by deleting excessive whitespace.
def pretty_clean_results(not_quite_clean_resutls):
	clean_results = []
	for i in not_quite_clean_results:
		clean_results.append(' '.join(i))
	return clean_results

## Takes the key terms from clean_results and concatenates them to
## make Google queries.
def add_google_query(clean_results):
	google_query = []
	for entry in clean_results:
		google_query.append('www.google.com/search?q=' + entry.replace(' ', '+'))
	return google_query

def make_pd_df(clean_results, google_query):
	clean_results_series = pd.Series(clean_results)
	result_category_series = pd.Series(result_category_list)
	google_search_series = pd.Series(google_query)
	d = {'Category': result_category_series, 'Entry': clean_results_series, 'Google Search': google_search_series}
	final_result = pd.DataFrame(d)
	return final_result

total_result, result_category_list = search_terms(soup)
not_quite_clean_results = not_really_clean_results(total_result, result_category_list)
clean_results = pretty_clean_results(not_quite_clean_results)
google_query = add_google_query(clean_results)
final_result = make_pd_df(clean_results, google_query)





