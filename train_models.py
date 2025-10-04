# train_models.py
import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# ---------- Load your dataset ----------
df = pd.read_csv("..\smsspamcollection.tsv" , sep="\t")  # should have 'label' and 'text'

df = df.drop(columns=["length","punct"])

blanks=[]
for i,j,k in df.itertuples():
    if(j.isspace() or k.isspace()):
        blanks.append(i)


df.drop(blanks,inplace=True)

# ---------- Preprocess ----------
def clean_text(s):
    s = str(s).lower()
    s = re.sub(r'http\S+|www\S+','', s)
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    return re.sub(r'\s+',' ',s).strip()

df['clean_text'] = df['text'].apply(clean_text)



X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['label'],
                                                    test_size=0.2, random_state=42, stratify=df['label'])

# ---------- Define models ----------
pipelines = {
    "NaiveBayes": Pipeline([('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
                            ('clf', MultinomialNB())]),
    "LogisticRegression": Pipeline([('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
                                    ('clf', LogisticRegression(max_iter=1000))]),
    "SVM": Pipeline([('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
                     ('clf', LinearSVC())])
}

import os

SAVE_DIR = os.path.join(os.path.dirname(__file__), "detector", "ml_models")
os.makedirs(SAVE_DIR, exist_ok=True)


# ---------- Train & save ----------
for name, pipe in pipelines.items():
    pipe.fit(X_train, y_train)
    model_path = os.path.join(SAVE_DIR, f"{name}.joblib")
    joblib.dump(pipe, model_path)
    print(f"✅ Saved {name} at {model_path}")


