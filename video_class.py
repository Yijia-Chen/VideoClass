import re
from collections import namedtuple

import numpy
from bs4 import BeautifulSoup
from sklearn import svm
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer,
                                             TfidfVectorizer)

LabeledVideo = namedtuple('LabeledVideo', ['path', 'label'])
DATA_STORAGE = []
numpy.set_printoptions(threshold=numpy.nan)

# Sample categories
CLASSES = [
    'SCIENCE'
    'HUMOR'
    'LAW'
]


def transcribe(path):
    with open(path, encoding="utf-8", mode="r") as file:
        string = file.read()
    whole_list = string.split("\n")
    final_list = []
    for i in range(len(whole_list)):
        if i % 4 == 2:
            final_list.append(whole_list[i])
    final_string = "  ".join(final_list)
    return final_string


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


def vectorize(corpus):
    vectorizer = CountVectorizer()
    train = vectorizer.fit_transform(corpus).toarray()
    return (train, vectorizer)


def weigh_terms(matrix):
    transformer = TfidfTransformer()
    return transformer.fit_transform(matrix).toarray()


def prepare_classification(TRAIN_URLS):

    # Apply text processing to all websites
    train_corpus = list(map(transcribe, [pt.path for pt in TRAIN_URLS]))

    # test_corpus = list(map(get_text, [pt.url for pt in TEST_URLS]))

    # Vectorize array
    (X_train, vectorizer) = vectorize(train_corpus)

    # Weigh terms
    Xw_train = weigh_terms(X_train)
    print(Xw_train)
    print(len(Xw_train))
    print(len(Xw_train[0]))

    # Prepare results
    Y_train = list(
        map(CLASSES.index, [pt.label for pt in TRAIN_URLS]))

    # return (Xw_train, Xw_test, Y_train, Y_test)
    return (Xw_train, Y_train, vectorizer)


def generate_classifier(TRAIN_URLS):
    (X_train, Y_train, vectorizer) = prepare_classification(TRAIN_URLS)
    classifier = svm.SVC()
    classifier.fit(X_train, Y_train)
    return classifier, vectorizer


def predict_video(path, classifier, vectorizer):
    test_corpus = [transcribe(input("enter the path of the srt file: "))]
    X = vectorizer.transform(test_corpus).toarray()
    X_test = weigh_terms(X)
    return CLASSES[classifier.predict(X_test)[0]]


def label(path, label):
    vid = LabeledVideo(path, label)
    DATA_STORAGE.append(vid)
    return "Label successful."


def predict(path):
    (classifier, vectorizer) = generate_classifier(DATA_STORAGE)
    return predict_video(path, classifier, vectorizer)
