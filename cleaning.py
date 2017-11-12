from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def clean_input(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")

    clean_input = []

    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input.append(item)

    return clean_input


def is_common(words):
    common_words = ['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it',
                    'i', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say',
                    'this', 'they', 'is', 'an', 'at', 'but', 'we', 'his', 'from',
                    'that', 'not', 'by', 'she', 'or', 'as', 'what', 'go',
                    'their', 'can', 'who', 'get', 'if', 'would', 'her', 'all',
                    'my', 'make', 'about', 'know', 'will', 'as', 'up', 'one',
                    'time', 'has', 'been', 'there', 'year', 'so', 'think',
                    'when', 'which', 'them', 'some', 'me', 'people', 'take',
                    'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could',
                    'now', 'than', 'like', 'other', 'how', 'then', 'its', 'our',
                    'two', 'more', 'these', 'want', 'way', 'look', 'first',
                    'also', 'new', 'because', 'day', 'more', 'use', 'no', 'man',
                    'find', 'here', 'thing', 'give', 'many', 'well']

    for word in words:
        if word in common_words:
            return True

    return False


def get_names(input, n):
    input = clean_input(input)
    output = {}

    for i in range(len(input)-n+1):
        ngram_candidate = input[i:i+1]
        if is_common(ngram_candidate):
            continue

        ngram_temp = " ".join(input[i:i+n])

        if ngram_temp not in output:
            output[ngram_temp] = 0

        output[ngram_temp] += 1

    return output


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = get_names(content, 2)
sorted_ngrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_ngrams)

# print(ngrams)
# print("2-grams count is: " + str(len(ngrams)))