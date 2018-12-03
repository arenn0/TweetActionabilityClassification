import math
NORMALIZE = True

def create_dictionary(words_):
    dictionary = {}
    maxs = {}
    i=-1
    for documentId in words_:
        maxrel = 0
        for tweetid in words_[documentId]:
            i += 1
            # print(word, end=' ')
            for word in tweetid:
                if word not in dictionary:
                    dictionary[word] = {}
                    dictionary[word][i] = 1
                else:
                    if i not in dictionary[word]:
                        dictionary[word][i] = 1
                    else:
                        # print("Working with word: " + word + " and document: " + str(documentId))
                        dictionary[word][i] += 1
                if dictionary[word][i] > maxrel:
                    maxrel = dictionary[word][i]
                    # print("max of " + str(documentId) + " is " + word + ": " + str(maxrel))
            maxs[i] = maxrel

    return [dictionary, maxs, i]

# We need filtered_final to compute tf denominator
def compute_tfidf(dictionary, d, maxs, ndocs):
    table = {}
    # print(dictionary)
    for word in dictionary.keys():
        table[word] = {}
        for docId in dictionary[word]:

            if word in d:
                if NORMALIZE:
                    # print(word)
                    # print(" docId " + str(docId) + " length " + str(len(f[docId])) + " " + str(f[docId]))
                    table[word][docId] = dictionary[word][docId] /\
                                     maxs[docId] *\
                                     math.log(ndocs/len(d[word]), 2)
                else:
                    table[word][docId] = dictionary[word][docId] * \
                                         math.log(ndocs / len(d[word]), 2)
    return table


def calc_rank(table_docs, table_queries, queries_):
    table_similarity = {}
    di = {}
    # print(queries_)
    indexes = {}
    for queryId in range(0, nqueries):  # for each query
        # print(q)
        indexes[queryId] = []
        for word in queries_[queryId]:
            if word in table_docs:
                for docId in table_docs[word]:  # for each document
                    # print(docId)
                    if docId not in di:
                        di[docId] = calc_q(table_docs, docId)
                    if docId not in indexes[queryId]:
                        indexes[queryId].append(docId)
    for queryId in range(0, nqueries):  # for each query
        table_similarity[queryId] = {}
        q = calc_q(table_queries, queryId)
        # print(q)
        for docId in indexes[queryId]:  # for each document with which cosine similarity is non-zero
            di = calc_q(table_docs, docId)

            similarity = 0

            for word in queries_[queryId]:
                if word in table_queries and word in table_docs:
                    if docId in table_docs[word]:
                        similarity += table_docs[word][docId] * table_queries[word][queryId]
                        # print("Query: " + str(queryId) + " word: " + word + " docID: " + str(docId) + " tfidf: " + str(table_docs[word][docId]))
            table_similarity[queryId][docId] = similarity / math.sqrt(q * di)

    return table_similarity

def get_queries(associations):
    return associations.keys()