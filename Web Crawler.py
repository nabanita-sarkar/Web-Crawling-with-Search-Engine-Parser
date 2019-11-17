import search_engine_parser
from search_engine_parser import YahooSearch, GoogleSearch, BingSearch, AolSearch, BaiduSearch, DuckDuckGoSearch

search_args = ('web crawling king', 1)
gsearch = GoogleSearch()
ysearch = YahooSearch()
bsearch = BingSearch()
asearch = AolSearch()
b2search = BaiduSearch()
dsearch = DuckDuckGoSearch()

gresults = gsearch.search(*search_args)
yresults = ysearch.search(*search_args)
bresults = bsearch.search(*search_args)
aresults = asearch.search(*search_args)
b2results = b2search.search(*search_args)
dresults = dsearch.search(*search_args)

for i in range(10):
  print(gresults["titles"][i])
  print(gresults["links"][i])
  print(gresults["descriptions"][i])

  print(yresults["titles"][i])
  print(yresults["links"][i])
  print(yresults["descriptions"][i])

  print(dresults["titles"][i])
  print(dresults["links"][i])
  print(dresults["descriptions"][i])

  print(aresults["titles"][i])
  print(aresults["links"][i])
  print(aresults["descriptions"][i])

for i in range (5):
  print(bresults["titles"][i])
  print(bresults["links"][i])
  print(bresults["descriptions"][i])

  print(b2results["titles"][i])
  print(b2results["links"][i])
  print(b2results["descriptions"][i])

