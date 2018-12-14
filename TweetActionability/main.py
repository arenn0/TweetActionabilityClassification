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

EXPAND = True
TOP_N = 10

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

    #print(c)
    #exit()
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
                    pass
                    # print("Hello")
                    # print(f'Column names are {", ".join(row)}')
                else:
                    corpus[directory_list[i]].append(row[5])

                line_count += 1
            #print(f'Processed {line_count} lines.')
    return corpus


def load_queries(fileName):
    mapSimilarities = wnet.read_file(sys.argv[2])
    return {0: [list(mapSimilarities.keys())]}, mapSimilarities



corpus = load_dataset(sys.argv[1])
queries, wp_similarities = load_queries(sys.argv[2])

corpus = preprocess_corpus(corpus)

[dictionary_texts, max_docs, n_tweets, tweets] = tfidf.create_dictionary(corpus)

[dictionary_queries, max_queries, n_queries, _s] = tfidf.create_dictionary(queries)
dictionary_text_tfidf = tfidf.compute_tfidf(dictionary_texts, dictionary_texts, max_docs, n_tweets)

dictionary_queries_tfidf = tfidf.compute_tfidf(dictionary_queries, dictionary_texts, max_queries, n_tweets)

for key in list(wp_similarities.keys()):
    if EXPAND:
        if dictionary_queries_tfidf[key] != {}:
            dictionary_queries_tfidf[key][0] *= wp_similarities[key]
        else:
            dictionary_queries_tfidf[key] = {0: 0}
    else:
        if wp_similarities[key] != 1:
            dictionary_queries_tfidf[key] = {0:0}

similarities = tfidf.calc_rank(dictionary_text_tfidf, dictionary_queries_tfidf, queries, n_tweets, n_queries)

sorted_similarities = similarities[0]

sorted_similarities = sorted(sorted_similarities.items(), key=operator.itemgetter(1), reverse=True)
print("Number of Tweets")
print(n_tweets)
print("Expanded List:")
print(wp_similarities)
print("Top k results:")
print(sorted_similarities)
for i in range(TOP_N):
    print(" ".join(list(tweets[sorted_similarities[i][0]])))

