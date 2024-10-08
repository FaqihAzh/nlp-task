import re
from collections import Counter
from nltk import ngrams

def preprocess_text(text):
    # Lowercase the text and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def calculate_ngrams(words, n):
    return list(ngrams(words, n))

def count_ngrams(ngrams_list):
    return Counter(ngrams_list)

def display_ngrams(ngram_counts, n):
    print(f"\n{n}-gram:")
    for ngram, count in ngram_counts.items():
        print(f"{ngram}: {count}")

# Input pantun
pantun = """
Rumah mpok Atun ada di samping bang Mandra
Di depannya ada warung kopi om Botak
Jangankan disuruh nyari pantun segera
Nyari Harun Masiku aja saya siap pak
"""

words = preprocess_text(pantun)

# Calculate unigram, bigram, and trigram
unigrams = words
bigrams = calculate_ngrams(words, 2)
trigrams = calculate_ngrams(words, 3)

# Count the occurrences of each n-gram
unigram_counts = count_ngrams(unigrams)
bigram_counts = count_ngrams(bigrams)
trigram_counts = count_ngrams(trigrams)

# Display the results
display_ngrams(unigram_counts, 1)
display_ngrams(bigram_counts, 2)
display_ngrams(trigram_counts, 3)
