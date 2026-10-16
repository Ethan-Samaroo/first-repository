import csv
import json
from collections import Counter
import re
f = open('./data/obama_speech.txt')
txt = f.read()
txt_lines = txt.splitlines()
words = txt.split()
f.close()
f = open('./data/michelle_obama_speech.txt')
txt = f.read()
txt_lines = txt.splitlines()
words = txt.split()
f.close()
f = open('./data/donald_speech.txt')
txt = f.read()
txt_lines = txt.splitlines()
words = txt.split()
f.close()
f = open('./data/melina_trump_speech.txt')
txt = f.read()
txt_lines = txt.splitlines()
words = txt.split()
f.close()


def most_spoken_languages(filename, num):
    f = open(filename, encoding='utf-8')
    txt = f.read()
    country_dct = json.loads(txt)
    most_spoken_list = Counter()
    for country in country_dct:
        most_spoken_list.update(country['languages'])
    f.close()
    return most_spoken_list.most_common(num)


def most_populated_countries(filename, num):
    f = open(filename, encoding='utf-8')
    txt = f.read()
    country_dct = json.loads(txt)
    sorted_countries = sorted(
        country_dct, key=lambda country: country['population'], reverse=True)
    returned_sorted_countries = list()
    for nums in range(num):
        returned_sorted_countries.append(sorted_countries[nums])
    only_population = list()
    for country in returned_sorted_countries:
        temp_dict = dict()
        temp_dict['country'] = country['name']
        temp_dict['population'] = country['population']
        only_population.append(temp_dict)
    return only_population


f = open('./data/email_exchanges_big.txt')
text = f.read()
regex_pattern = r'<([^<>]+)>'
emails = re.findall(regex_pattern, text)


def find_most_common_words(filename, num):
    f = open(filename)
    txt = f.read()
    regex_pattern = r'\b\w+\b'
    words = re.findall(regex_pattern, txt.lower())
    word_counts = Counter(words)
    f.close()
    return word_counts.most_common(num)


with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    python_count = 0
    javascript_count = 0
    java_count = 0
    for row in csv_reader:
        row_text = ' '.join(row).lower()
        if 'python' in row_text:
            python_count += 1
        if 'javascript' in row_text:
            javascript_count += 1
        if 'java' in row_text and 'javascript' not in row_text:
            java_count += 1
    print(python_count)
    print(java_count)
    print(javascript_count)
