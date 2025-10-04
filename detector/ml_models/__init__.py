import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

models = {}
for model_file in ["NaiveBayes.joblib", "LogisticRegression.joblib", "SVM.joblib"]:
    path = os.path.join(BASE_DIR, model_file)
    models[model_file.split(".")[0]] = joblib.load(path)
