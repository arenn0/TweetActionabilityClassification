

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
        # Then, we're going to use the term "program" to find synsets like so:

        s_map[word]=1
        print(s_map)
        syns = wordnet.synsets(word)
        l= 'lost.a.01'
        print(syns)
        i=0
        similarity = {}
        #  find similarity of word with its synonims
        # if there is only a synonim, add it directly with weight 1
        if len(syns) == 1:
            s_map[syns[0].name().split(".")[0]] = 1
        else:
            #  take all the meanings of word and sum their similarity with all the other synonims
            for w in syns:
                if w.name().startswith(word):
                    for synonims in syns:
                        s = synonims.wup_similarity(w)
                        if i == 0:
                            similarity[synonims.name()] = 0
                        if s is not None:
                            similarity[synonims.name()] += s
                        else:
                            similarity[synonims.name()] += 0
                        print(similarity)
                    i=i+1
                    print(i)
            sim_clean = {}
            rep = {}
            #  compute the mean similarity
            for w in syns:
                similarity[w.name()] /= i
                if similarity[w.name()] != 0:
                    sim_clean[w.name().split(".")[0]] = 0
                    rep[w.name().split(".")[0]] = 0
            i=0
            # aggregate all the same words in a new s_map
            for w in syns:
                if similarity[w.name()] != 0:
                    sim_clean[w.name().split(".")[0]] += similarity[w.name()]
                    rep[w.name().split(".")[0]] += 1
            print(sim_clean)
            print(rep)
            # compute the mean of the words in the new s_map and add them to the final s_map
            for k, v in sim_clean.items():
                if k != word:
                    v = v/rep[k]
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
    expand_list(s_list)
