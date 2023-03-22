import requests
import pprint

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3c5006c2f74445e7ba2009f9ffd38ad4"

params = {
    "pageSize": 20
}

res = requests.get(url, params=params)
data = res.json()

# pprint.pprint(data)

# for d in data['articles']:
#     pprint.pprint(d)
#     print()
