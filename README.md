# Information Retrieval - Tweet Actionability Classification
This is the final project for UIC - CS 582 Information Retrieval. This project is about processing the dataset collection about disaster events in USA during 2017, in order to extract actionable information that could potentially help first responders.

## Getting Started
These instructions will provide a copy of the project up and running on your local machine for development and testing purposes. See _Installing_ for notes on how to deploy the project on a system.

### Requirements
* Python 3.6 or 2.7 https://www.python.org/downloads/
* `pip` should be already installed by default. Installation instructions 
[here](https://www.makeuseof.com/tag/install-pip-for-python/). Note that pip is not required if Anaconda or NLTK are already installed.  
* List of the [stopwords](https://www.dropbox.com/s/5789sj8v07j2id0/stopwords.txt) to remove.
* NLTK https://www.nltk.org/
* The WordNet PAckage inside NLTK. Automatically installed in the first lines of code.

### Installing
* [Anaconda](https://www.anaconda.com/download/) (requires Python versions 3.6, 2.7)
Or
* [NLTK](https://pypi.org/project/nltk/) (requires Python versions 2.7, 3.4, 3.5, or 3.6)
Or
* `pip install nltk` installs NLTK via pip. (Windows)

Check the installation by opening a script and typing `import nltk`. If this command is executed with an error, be sure to include NLTK in the python path of execution. If you are using PyCharm you can also configure PATH by navigating the File tab, clicking on Settings and adding NLTK package in the tab Project Interpreter.

## Running the Program
The program takes as first argument the path (absolute or relative) of the directory where the datsets are and as second argument the path (absolute or relative) of the file containing the list of the keywords, 'path/main.py dataset/ keywords'.

The execution may take several seconds, depending on the amount of the data in input. We have tested the algorithm with up to 20'000 tweets. In this case, results were displayed in less than one minute.

A couple of tunable parameters could be modified to explore the results:
- line 13 on the 'main.py' file: the flag EXPAND could be set to false to not perform any kind of expansion of the keywords.
- line 14 on the 'main.py' file: the flag TOP_N countains the number of the results displayed. We have experienced that the highest precision is reached within the first dozen, since the number of actionable tweets is extremely low.
- line 2 on the 'tfidf.py' file: allows the user to choose whether they want to perform normalizaion of the tf-idf scores.

### Built With
 Windows and:

1. [Python](https://docs.python.org/3/) v3.7
2. [NLTK](https://www.nltk.org/install.html) library
3. [Pycharm](https://www.jetbrains.com/pycharm/) IDE By JetBrains

## Authors
**Alessandro Rennola**, M.Sc. University of Illinois at Chicago
**Edoardo Savini**, M.Sc. University od Illinois at Chicago
