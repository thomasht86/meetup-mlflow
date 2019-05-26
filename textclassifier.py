import mlflow.pyfunc
import string
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

def remove_punctuation(document):
    # Remove weird characters
    return "".join([ (c if c not in string.punctuation+"\n\r\t" else " ") for c in document])

def tokenize(document):
    # From document to list of lower case tokens
    return [w.lower() for w in remove_punctuation(document).split(" ") if len(w)>0]

# Define the model class
class TextClassifier(mlflow.pyfunc.PythonModel):

    def __init__(self, vectorizer, clf):
        self.vectorizer = vectorizer
        self.clf = clf
        
    def predict(self, model_input):
        prepped_input = self.vectorizer.transform(model_input)
        preds = self.clf.predict(prepped_input)
        return preds