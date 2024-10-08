import re
from collections import Counter
from nltk import ngrams

def preprocess_text(text):
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

# Pantun Input
print("Masukkan pantun 4 baris:")

baris1 = input("Baris 1: ")
baris2 = input("Baris 2: ")
baris3 = input("Baris 3: ")
baris4 = input("Baris 4: ")

pantun = f"{baris1}\n{baris2}\n{baris3}\n{baris4}"

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
