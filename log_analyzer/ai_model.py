# ai_model.py
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

MODEL_PATH = "log_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

def train_if_needed(log_lines):
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        return
    vect = TfidfVectorizer()
    X = vect.fit_transform(log_lines)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vect, VECTORIZER_PATH)

def detecter_ligne_anormale(log_line):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        return False
    model = joblib.load(MODEL_PATH)
    vect = joblib.load(VECTORIZER_PATH)
    try:
        X = vect.transform([log_line])
        prediction = model.predict(X)
        return prediction[0] == -1
    except:
        return False