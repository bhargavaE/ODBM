import requests
import pprint
r = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=e26e533a')
pprint.pprint(r.json())
