import json
import collections

with open('../data.json') as infile:
    data = json.load(infile)

pData = data['events_data']

categories = []
for item in pData:
    categories.append(item['category'])

# print(len(pData))

c = collections.Counter()

# сколько раз встречалась каждая из категорий
for category in categories:
    c[category] += 1
print(c)



