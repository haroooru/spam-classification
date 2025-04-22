import streamlit as st
import joblib
import re
import string

# Load the trained model and TF-IDF vectorizer
model = joblib.load("https://github.com/haroooru/spam-classification/raw/refs/heads/main/spam_classifier.pkl")
vectorizer = joblib.load("https://github.com/haroooru/spam-classification/raw/refs/heads/main/spam_classifier.pkl")

# Function to clean user input text (same as in training)
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Streamlit UI
st.title("📩 Spam Email Classifier")
st.write("Enter a message to check if it's **Spam or Not Spam**.")

# User Input Box
user_input = st.text_area("✍️ Enter your message here:", height=100)

# Predict Button
if st.button("Classify"):
    if user_input:
        # Preprocess Input
        clean_message = clean_text(user_input)
        input_tfidf = vectorizer.transform([clean_message])  # Convert text to TF-IDF features
        prediction = model.predict(input_tfidf)[0]  # Get prediction
        
        # Display the result
        if prediction == 1:
            st.error("🚨 This is **Spam**!")
        else:
            st.success("✅ This is **Not Spam**.")
    else:
        st.warning("⚠️ Please enter a message to classify.")
