import string
from collections import Counter
from functools import reduce

def remove_punctuation(words):
    translator = str.maketrans('', '', string.punctuation)
    return [word.translate(translator) for word in words]

def longest_word(words):
    if words:
        m = words[0]
        for word in words[1:]:
            if len(word) > len(m):
                m = word
        return m
    return None

def most_frequent_word(words):
    if words:
        distinct_words = [word.lower() for word in words if len(word) >= 5]
        counter = Counter(distinct_words)
        max_freq_word = max(counter, key=counter.get)
        return max_freq_word
    return None

def show_properties(abstract):

    sentences = [sentence for sentence in abstract.split('.')]
    sentences = list(filter(lambda x: x.strip() != '', sentences))
    print(f'Number of sentences : {len(sentences)}')

    words = remove_punctuation(abstract.split())
    print(f'Number of words : {len(words)}')

    print(f'Longest word : {longest_word(words)}')

    freq = most_frequent_word(words)
    print(f'The most frequent word : {freq}')

def align_words(acc, word, max_length):
    if len(acc[-1]) + len(word) < max_length:
        acc[-1] += word + ' '
    else:
        acc.append(word + ' ')
    return acc

def display_align_right(abstract):
    max_row_length = 55
    words = abstract.split()
    
    rows = reduce(lambda acc, word: align_words(acc, word, max_row_length), words, [''])

    aligned_rows = [(' ' * (max_row_length - len(row)) + row) for row in rows if row]

    for row in aligned_rows:
        print(row)
            
def display_reverse(abstract):
    words_reverse = [word[::-1] for word in abstract.split()]
    display_align_right(' '.join(words_reverse))

def mean_word_length(sentence):
    return sum(length for length in sentence)/len(sentence) if len(sentence) else 0

def sentence_properties(abstract):
    sentences = abstract.split('.')
    lengths = [[len(word) for word in sentence.split()] for sentence in sentences if sentence]
    means = list(map(mean_word_length, lengths))
    print(means)

if __name__ == '__main__':

    f = open('abstract.txt', 'r')
    abstract = f.read()

    print('Main properties:')
    show_properties(abstract)
    print('----------')

    print('Text aligned to right, with max row length = 55:')
    display_align_right(abstract)
    print('----------')

    print('Text reversed:')
    display_reverse(abstract)
    print('----------')

    print('Main word length for each sentence:')
    sentence_properties(abstract)
    print('----------')
