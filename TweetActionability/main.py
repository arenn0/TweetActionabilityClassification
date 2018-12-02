import csv
import sys
import os


def preprocess_corpus(corpus):
    for file_name in corpus:
        for i in corpus[file_name]:
            for word in corpus[file_name][i]:
                pass



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
                    print("Hello")
                    # print(f'Column names are {", ".join(row)}')
                else:
                    corpus[directory_list[i]].append(row[5])

                line_count += 1
            print(f'Processed {line_count} lines.')
    return corpus


corpus = load_dataset(sys.argv[1])

print(corpus)
corpus = preprocess_corpus(corpus)