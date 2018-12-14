

import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
dler.download("wordnet")
# nltk.download()
# First, you're going to need to import wordnet:
from nltk.corpus import wordnet as wordnet


def expand_list(wordlist):
    s_map = {}
    for word in wordlist:
        #  for each word in the file analyze its synonims (a word may have itself between its syns)
        s_map[word]=1
        print(s_map)
        syns = wordnet.synsets(word)
        l= 'lost.a.01'
        print(syns)
        i=0
        # map to contain word + similarity
        similarity = {}
        #  find similarity between our word and its synonims
        #  if there is only a synonim different from the word itself, add it directly with weight 1
        if len(syns) == 1:
            s_map[syns[0].name().split(".")[0]] = 1
        else:
            #  for all the meanings of word take the max similarity with all the other synonims
            for w in syns:
                if w.name().startswith(word):
                    for synonims in syns:
                        s = synonims.wup_similarity(w)
                        if i == 0:
                            similarity[synonims.name()] = 0
                        if s is not None:
                            if s > similarity[synonims.name()]:
                                similarity[synonims.name()] = s
                            #  similarity[synonims.name()] += s
                        print(similarity)
                    i=i+1
                    print(i)
            sim_clean = {}
            rep = {}
            #  create new map to contain the max similarity
            if len(similarity) > 0:
                for w in syns:
                    if similarity[w.name()] != 0:
                        sim_clean[w.name().split(".")[0]] = 0
                i=0
                # between all the same words take the max similarities
                for w in syns:
                    if similarity[w.name()] != 0 and similarity[w.name()] > sim_clean[w.name().split(".")[0]]:
                        sim_clean[w.name().split(".")[0]] = similarity[w.name()]
                print(sim_clean)
                print(rep)
                # add the new words + similarity value to the final s_map
                for k, v in sim_clean.items():
                    if k != word:
                        s_map[k] = v

        print(s_map)
    return s_map


def read_file(file):   # "ManuallyAnnotatedWords.txt"
    s_list = []
    file = open(file, "r")
    p = file.readlines()

    for i in range(0, len(p)):
        s_list.append(p[i].strip("\n"));

    print(s_list)
    return expand_list(s_list)

# read_file("ManuallyAnnotatedWords.txt")
