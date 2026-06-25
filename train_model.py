import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib


data = pd.read_csv("data/spam.csv", sep="\t", header=None, names=["label", "message"])

x_train, x_test, y_train, y_test = train_test_split(data["message"], data["label"], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
x_train_vectors = vectorizer.fit_transform(x_train)
x_test_vectors = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vectors, y_train)

predictions = model.predict(x_test_vectors)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, pos_label="spam")
recall = recall_score(y_test, predictions, pos_label="spam")
f1 = f1_score(y_test, predictions, pos_label="spam")

joblib.dump(model, "spam_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("model and vectorizer saved successfully")