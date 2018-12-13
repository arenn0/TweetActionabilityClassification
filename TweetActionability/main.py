import csv
import sys
import os
import string
import operator
import tfidf
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
dler.download("wordnet")
import wnet
# nltk.download()
# First, you're going to need to import wordnet:
from nltk.corpus import wordnet as wordnet
EXPAND = True



def preprocess_corpus(corpus):
    c = {}
    exclude = set(string.punctuation)
    exclude.add('.')
    [exclude.add(i) for i in range(10)]
    exclude.add('amp')
    # exclude.add('#')

    for file_name in corpus:
        c[file_name] = []
        for i in corpus[file_name]:
            words = []
            for word in i.split():
                #print(word)
                w = ''.join(ch for ch in word if ch not in exclude)
                #print(w)
                if 'http' in w or w in exclude:
                    pass
                else:
                    words.append(w.lower())
            c[file_name].append(words)

    # print(c)
    return c



def load_dataset (dirName):
    directory_path = dirName
    directory_list = sorted(os.listdir(directory_path))
    global n_docs
    n_docs = len(directory_list)  # Size of the dataset
    # print(n_docs)
    corpus = {}
    for i in range(n_docs):
        # print(directory_list[i])  # Prints the names of the Datasets
        corpus[directory_list[i]] = []
        with open(directory_path + directory_list[i], encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print("Hello")
                    print(f'Column names are {", ".join(row)}')
                else:
                    corpus[directory_list[i]].append(row[5])

                line_count += 1
            #print(f'Processed {line_count} lines.')
    return corpus


def load_queries(fileName):
    """content = open(fileName, "r")

    terms = set()
    q = []
    query = ''
    for _i in content:
        for _j in _i:
            if _j != '.' and _j != '\n':
                query += _j
            else:
                if query:
                    if query[len(query) - 1] != ' ':
                        query += ' '
                    q.append(query)
                    [terms.add(query.split(" ")[i]) for i in range(len(query.split(" ")))]
                    query = ''
    if '' in terms:
        terms.remove('')
    final = []
    final.append(list(terms))



    return {0: final}, mapSimilarities
    """
    mapSimilarities = wnet.read_file(sys.argv[2])
    print(mapSimilarities)
    return {0: [list(mapSimilarities.keys())]}, mapSimilarities



corpus = load_dataset(sys.argv[1])
queries, wp_similarities = load_queries(sys.argv[2])

#print(queries)
#print(queries)
corpus = preprocess_corpus(corpus)
#print(corpus)
[dictionary_texts, max_docs, n_tweets] = tfidf.create_dictionary(corpus)
#print(corpus)
#print(queries)
[dictionary_queries, max_queries, n_queries] = tfidf.create_dictionary(queries)
dictionary_text_tfidf = tfidf.compute_tfidf(dictionary_texts, dictionary_texts, max_docs, n_tweets)
#print(dictionary_queries)
dictionary_queries_tfidf = tfidf.compute_tfidf(dictionary_queries, dictionary_texts, max_queries, n_tweets)
print(dictionary_queries_tfidf)

for key in list(wp_similarities.keys()):
    if EXPAND:
        if dictionary_queries_tfidf[key] != {}:
            dictionary_queries_tfidf[key][0] *= wp_similarities[key]
        else:
            dictionary_queries_tfidf[key] = {0: 0}
    else:
        if wp_similarities[key] != 1:
            dictionary_queries_tfidf[key] = {0:0}
print(dictionary_queries_tfidf)
similarities = tfidf.calc_rank(dictionary_text_tfidf, dictionary_queries_tfidf, queries, n_tweets, n_queries)

#print(dictionary)
#print(dictionary_text_tfidf)

# filtered_final_queries = get_queries(associations)
#print(similarities)
sorted_similarities = similarities[0]

#print(sorted_similarities)
sorted_similarities = sorted(sorted_similarities.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_similarities)
#print(corpus)