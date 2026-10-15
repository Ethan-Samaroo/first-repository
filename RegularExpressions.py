import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'\b\w+\b'
words = re.findall(regex_pattern, paragraph.lower())
word_counts = Counter(words)

paragraph_2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles'
regex_pattern_2 = r'-?\d+'
numbers = re.findall(regex_pattern_2, paragraph_2)
sorted_numbers = list(map(int, numbers))


def is_valid_variable(string) -> bool:
    regex_pattern_3 = r'^[a-zA-Z_][a-zA-Z0-9_]*'
    if re.fullmatch(regex_pattern_3, string, re.I) is not None:
        return True
    return False


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(string) -> str:
    cleaned = re.sub(r'[%$@&#;]', '', string)
    cleaned = re.sub(r'[.!?,]', '', cleaned)
    cleaned = cleaned.strip()
    return cleaned


print(clean_text(sentence))
cleaned_text = clean_text(sentence)


def most_frequent_words(string):
    regex_pattern_4 = r'\b\w+\b'
    most = re.findall(regex_pattern_4, string)
    count = Counter(most)
    return count.most_common(3)


print(most_frequent_words(cleaned_text))
