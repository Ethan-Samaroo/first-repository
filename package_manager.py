import requests
from collections import Counter
import re
import statistics
url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = requests.get(url)
txt = response.text
regex_pattern = r'\b\w+\b'
words = re.findall(regex_pattern, txt.lower())
word_counts = Counter(words)

url = 'https://api.thecatapi.com/v1/breeds'
headers = {
    'x-api-key': ''
}

response = requests.get(url, headers=headers)
cats = response.json()
weights = list()
for cat in cats:

    try:
        weight_range = cat['weight']['metric']
        numbers = weight_range.split('-')
        midpoint = (float(numbers[0]) + float(numbers[1])) / 2
        weights.append(midpoint)
    except ValueError:
        pass

life_span = list()
for cat in cats:

    try:
        life_range = cat['life_span']
        numbers = life_range.split('-')
        if len(numbers) == 2:
            midpoint = (float(numbers[0]) + float(numbers[1])) / 2
            life_span.append(midpoint)
        else:
            life_span.append(float(numbers[0]))
    except ValueError:
        pass

countries = list()
for cat in cats:
    countries.append(cat['origin'])
countries_count = Counter(countries)


names = list()
for cat in cats:
    names.append(cat['name'])
names_count = Counter(names)


url = 'https://api.restcountries.com/countries/v5'

headers = {
    'Authorization': ''
}

response = requests.get(url, headers=headers)
print(response.status_code)
payload = response.json()
country_data = payload['data']['objects']
areas = dict()
for country in country_data:
    areas[country['names']['common']] = country['area']['kilometers']
sorted_areas = sorted(
    areas.items(), key=lambda distance: distance[1], reverse=True)
print(sorted_areas[:10])
languages = list()
for country in country_data:
    for language in country['languages']:
        languages.append(language['name'])
language_count = Counter(languages)
print(language_count.most_common(10))
print(len(language_count))
