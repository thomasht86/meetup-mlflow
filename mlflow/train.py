#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'meetup-mlflow/mlflow'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
import numpy as np
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, f1_score, auc as sk_auc, roc_curve, precision_score, recall_score, accuracy_score
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
import pickle
import random
import re
import keras
import os
import mlflow
from mlflow import log_metric, log_param, log_artifact
import mlflow.sklearn

seed = 42
use_idf = True
ngram_range = (1,1)
alpha = 1
fit_prior = True
conda_env_path = "environment.yml"
model_path = "models"

mlflow.set_experiment("ntnu_course_classifier")
## Data import and cleaning
with mlflow.start_run() as run:
    # Log params
    mlflow.log_param("seed", seed)
    mlflow.log_param("use_idf", use_idf)
    mlflow.log_param("ngram_range", ngram_range)
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("fit_prior", fit_prior)
    
    df = pd.read_csv("data/course_descriptions.csv", usecols=[1,2,3,4,5,6])


    #%%
    df = df.dropna()

    #%%
    def remove_punctuation(document):
        return "".join([ (c if c not in string.punctuation+"\n\r\t" else " ") for c in document])

    def tokenize(document):
        return [w.lower() for w in remove_punctuation(document).split(" ") if len(w)>0]


    #%%
    stoplist = [l.strip() for l in open("stopwords.txt", "r").readlines()]


    #%%
    y = df["fac"].astype(str)
    X_train, X_test, y_train, y_test = train_test_split(df["description"], y, stratify=y, random_state=seed)

    #%%
    vec = TfidfVectorizer(tokenizer=tokenize, stop_words=stoplist, use_idf=use_idf, ngram_range=ngram_range)
    trn_vec= vec.fit_transform(X_train.values)
    test_vec = vec.transform(X_test.values)

    #%%
    label_cols = df["fac"].astype(str).unique().tolist()

    clf = MultinomialNB(alpha=alpha, fit_prior=fit_prior)

    clf.fit(trn_vec, y_train)

    preds = clf.predict(test_vec)
    
    acc = accuracy_score(y_test, preds)
    f1_macro = precision_score(y_test, preds, average="macro")
    f1_micro = precision_score(y_test, preds, average="micro")
    f1_per_class = precision_score(y_test, preds, labels=label_cols, average=None)

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_macro", f1_macro)
    mlflow.log_metric("f1_micro", f1_micro)
    for c, f1 in zip(label_cols, f1_per_class):
        mlflow.log_metric("f1_"+c, f1)
    
    mlflow.sklearn.save_model(clf, model_path, conda_env=conda_env_path, serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE)

    #%% [markdown]
    # ## Next steps
    # - Define metrics
    # - Plot
    # - Script evolution
    # - Think about steps




