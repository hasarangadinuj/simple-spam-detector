import streamlit as st
import joblib

model = joblib.load("spam_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

st.title("📩 Spam Message Classifier")
st.write("Paste a message below to check if it's spam or not.")

user_input = st.text_area("Enter your message here:")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("please enter a messsage to check")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        probability =model.predict_proba(input_vector)[0]

        spam_index = list(model.classes_).index("spam")
        spam_probability = probability[spam_index] * 100

        if prediction == "spam":
            st.error(f"⚠️ This message is likely SPAM! (Probability: {spam_probability:.2f}%)")
        else:
            st.success(f"✅ This message is likely NOT SPAM. (Probability: {100 - spam_probability:.2f}%)")