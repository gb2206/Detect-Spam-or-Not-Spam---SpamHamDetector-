import joblib
import os

# Path to models folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "ml_models")

# Load models once at startup
models = {
    "Naive Bayes": joblib.load(os.path.join(MODEL_DIR, "NaiveBayes.joblib")),
    "Logistic Regression": joblib.load(os.path.join(MODEL_DIR, "LogisticRegression.joblib")),
    "SVM": joblib.load(os.path.join(MODEL_DIR, "SVM.joblib")),
}
