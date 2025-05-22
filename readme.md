# Email Spam Classification - Streamlit App

This project is a binary classification system that detects whether an email message is **spam** or **not spam** using a trained machine learning model. It also includes a simple web interface using **Streamlit** for user interaction.

---

##  Dataset Description

The dataset used is the **SMS Spam Collection Dataset** from UCI, available on Kaggle:
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

- It contains over 5,000 SMS messages labeled as "ham" (not spam) or "spam".
- Only the `v1` (label) and `v2` (message) columns are used.
- The labels are converted into binary format: 0 for ham, 1 for spam.

---

## Preprocessing Steps

1. Convert all text to lowercase.
2. Remove numbers and punctuation.
3. Apply **TF-IDF vectorization** to convert text into numerical features.

---

##  Model Used

- **Multinomial Naive Bayes Classifier**
- Chosen for its effectiveness with text classification problems.
- Trained using an 80-20 train-test split.

---

## Performance Metrics

- Accuracy: ~97% on the test set
- Evaluated using:
  - Accuracy Score
  - Precision, Recall, F1 Score (via Classification Report)

---

##  Streamlit Web App

The `app.py` file creates a Streamlit UI where users can input their own message and classify it instantly as spam or not spam.

### Files Included:

- `train_model.py` - script to train and save the model
- `app.py` - Streamlit interface
- `spam_classifier.pkl` - trained ML model
- `tfidf_vectorizer.pkl` - saved TF-IDF vectorizer
- `requirements.txt` - list of Python dependencies

---

## How to Run

1. Install dependencies:





