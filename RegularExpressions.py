import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'\b\w+\b'
words = re.findall(regex_pattern, paragraph.lower())
word_counts = Counter(words)

paragraph_2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles'
regex_pattern_2 = r'-?\d+'
numbers = re.findall(regex_pattern_2, paragraph_2)
print(numbers)