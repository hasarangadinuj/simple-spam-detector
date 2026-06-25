# 📩 Spam Message Classifier

A beginner Machine Learning project that classifies SMS/email messages as Spam or Not Spam, with a live probability score. Built with Python and Streamlit.

🔗 **Live demo:** [add your Streamlit Cloud URL here]

## Features
- Paste any SMS/email text, get an instant Spam / Not Spam prediction
- Shows a spam probability percentage
- Simple Streamlit web interface

## Tech Stack
Python · pandas · scikit-learn (TF-IDF + Multinomial Naive Bayes) · joblib · Streamlit

## How It Was Built
1. Downloaded the UCI SMS Spam Collection dataset (5,574 labeled SMS messages)
2. Loaded and explored the data with pandas
3. Split into training (80%) and testing (20%) sets
4. Converted message text into numeric vectors using TF-IDF
5. Trained a Multinomial Naive Bayes classifier on the training set
6. Evaluated on the held-out test set (accuracy, precision, recall, F1)
7. Saved the trained model + vectorizer using joblib
8. Built a Streamlit app that loads the saved model and predicts on user input
9. Deployed on Streamlit Community Cloud

## Model Performance (on held-out test data)
- Accuracy: 96.68%
- Precision: 100.00%
- Recall: 75.17%
- F1-score: 85.82%

Note: dataset is imbalanced (~87% ham / 13% spam), so accuracy alone is misleading — precision/recall give the fuller picture.

## ⚠️ Known Limitations
- **Trained on old data:** the dataset is from ~2001-era UK SMS messages. It recognizes classic spam patterns ("free," "win," "claim," "prize," text-to-shortcode offers) well, but has little to no exposure to modern phishing-style language (e.g. "your account has been suspended, verify your identity"), so it may miss these as spam.
- **Single ambiguous words aren't reliable on their own:** Naive Bayes combines word evidence against a strong prior (87% of messages are ham). A message needs multiple strong spam signals together to be confidently flagged — one suspicious word alone usually isn't enough.
- **Some words are contradictory in this dataset:** e.g. "won" appears almost as often in normal messages ("I won the game") as in spam, so it's a weak signal here despite intuition suggesting otherwise.
- **Not a real security tool.** This is an educational project, not a production-grade spam/phishing filter. Don't rely on it for real safety or security decisions.

## Running Locally
```
git clone <your-repo-url>
cd spam-classifier
pip install pandas scikit-learn joblib streamlit
python train_model.py
python -m streamlit run app.py
```