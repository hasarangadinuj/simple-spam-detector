# 📩 Spam Detector

A beginner-friendly Machine Learning project that classifies SMS/email messages as **Spam** or **Not Spam**, with a live probability score, built using Python and Streamlit.

## Features
- Paste any SMS or email text and get an instant prediction.
- Shows a spam probability percentage (e.g., "92% likely to be spam").
- Simple, clean web interface built with Streamlit.

## Tech Stack
- **Python** — core programming language
- **pandas** — loading and handling the dataset
- **scikit-learn** — TF-IDF text vectorization and Naive Bayes classification
- **joblib** — saving/loading the trained model
- **Streamlit** — web app interface

## How It Works
1. The model is trained on the [UCI SMS Spam Collection dataset](https://archive.ics.uci.edu/dataset/228/sms+spam+collection), which contains 5,574 real SMS messages labeled as "spam" or "ham" (not spam). (run get_data.py to get the data set that used here)
2. Each message is converted into numerical form using **TF-IDF** (Term Frequency–Inverse Document Frequency), which scores words based on how important/distinctive they are.
3. A **Multinomial Naive Bayes** classifier is trained on these numeric vectors to learn which word patterns are associated with spam.
4. New messages go through the same TF-IDF conversion, and the trained model predicts a spam probability.

## Model Performance (on held-out test data)
- **Accuracy:** 96.68%
- **Precision:** 100.00%
- **Recall:** 75.17%
- **F1-Score:** 85.82%

> Note: This dataset is imbalanced (~87% ham, ~13% spam), so accuracy alone can be misleading. Precision and recall give a more complete picture of performance.

## Running Locally

1. Clone this repository:
    git clone <your-repo-url-here>
    cd spam-detector

2. Install dependencies:
    pip install -r requirements.txt

3. Train the model (creates `spam_model.joblib` and `vectorizer.joblib`):
    python train_model.py

4. Run the app:
    python -m streamlit run app.py

## ⚠️ Disclaimer
This is an educational project built to practice Machine Learning fundamentals. It is **not** a guaranteed spam-detection or security system, and should not be used to make real safety, financial, or security decisions.

## Live Demo
*(Link will be added after deployment)*
