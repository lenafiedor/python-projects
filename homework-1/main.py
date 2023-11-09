import string
from collections import Counter

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
        max_freq_word = max(counter, key = counter.get)
        return max_freq_word
    return None


f = open('abstract.txt', 'r')
abstract = f.read()

def show_properties(abstract):

    sentences = abstract.split('.')[:-1]
    print(f'Number of sentences : {len(sentences)}')

    words = remove_punctuation(abstract.split())
    print(f'Number of words : {len(words)}')

    print(f'Longest word : {longest_word(words)}')

    freq = most_frequent_word(words)
    print(f'The most frequent word : {freq}')

def display_align_right(abstract):

    max_row_length = 55
    rows = []

    row = ''
    for word in abstract.split():
        if len(row) + len(word) < max_row_length:
            row += word
            if len(row) < max_row_length:
                row += ' '
        else:
            aligned_row = ' ' * (max_row_length - len(row)) + row
            rows.append(aligned_row)
            row = word + ' '
    if row:
        align = max_row_length - len(row)
        aligned_row = ' ' * (max_row_length - len(row)) + row
        rows.append(aligned_row)

    for row in rows:
        print(row)
            
def display_reverse(abstract):
    words_reverse = [word[::-1] for word in abstract.split()]
    display_align_right(' '.join(words_reverse))

def sentence_properties(abstract):
    sentences = abstract.split('.')
    lengths = [[len(word) for word in sentence.split()] for sentence in sentences]
    print(lengths)
    means = [sum(length)/len(length) for length in lengths if length]
    print(means)

if __name__ == '__main__':
    show_properties(abstract)
    display_align_right(abstract)
    display_reverse(abstract)
    sentence_properties(abstract)
