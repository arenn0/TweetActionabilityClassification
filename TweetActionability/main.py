import csv
import sys
import os
import string
import nltk
import tfidf

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


corpus = load_dataset(sys.argv[1])

#print(corpus)
corpus = preprocess_corpus(corpus)

[dictionary, max_docs, n_tweets] = tfidf.create_dictionary(corpus)
dictionary_text_tfidf = tfidf.compute_tfidf(dictionary, dictionary, max_docs, n_tweets)


print(dictionary)
print(dictionary_text_tfidf)

filtered_final_queries = get_queries(associations)

similarities = tfidf.calc_rank(dictionary_text_tfidf, dictionary_queries_tfidf, filtered_final_queries)
