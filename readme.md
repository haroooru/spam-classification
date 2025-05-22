

# 📩 Email Spam Classification - Streamlit App

This project is a binary classification system that detects whether an email message is **spam** or **not spam** using a trained machine learning model. It also includes a simple web interface using **Streamlit** for user interaction.

---

## 📚 Dataset Description

The dataset used is the **SMS Spam Collection Dataset** from UCI, available on Kaggle:
🔗 [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

* Contains 5,574 SMS messages.
* Columns used:

  * `v1`: Label (`ham` or `spam`)
  * `v2`: Message text
* Labels converted to:

  * `0`: Ham (Not Spam)
  * `1`: Spam

---

## 🛠️ Preprocessing Steps

1. Convert text to **lowercase**
2. Remove **numbers** and **punctuation**
3. Apply **TF-IDF Vectorization** for feature extraction

---

## 🤖 Model Used

* **Multinomial Naive Bayes**
* Suitable for discrete text-based features
* Trained on 80% of the dataset and tested on the remaining 20%

---

## 📈 Model Performance Summary

### 🔧 Training Set:

* **Accuracy:** 98%

### 🧪 Test Set:

* **Accuracy:** 95.07%
* **Precision / Recall / F1-score:**

| Class | Precision | Recall | F1-score |
| ----- | --------- | ------ | -------- |
| Ham   | 0.95      | 1.00   | 0.97     |
| Spam  | 1.00      | 0.63   | 0.78     |

* **Macro Avg F1-score:** 0.87
* **Weighted Avg F1-score:** 0.95

### ✅ Generalization:

* Very small gap between train and test performance
* Slight drop in spam recall indicates some spam missed
* Model is **not overfitting**

---

## 🖥️ Streamlit Web App

The `app.py` file provides a web UI for testing messages. Users can enter a message and check if it's classified as **spam** or **not spam**.

---

## 📁 Files Included

* `train_model.py` – Training script that saves the model and vectorizer
* `app.py` – Streamlit UI for deployment
* `spam_classifier.pkl` – Trained model
* `tfidf_vectorizer.pkl` – TF-IDF vectorizer
* `requirements.txt` – Python dependencies
* `README.txt` – This documentation

---

## ▶️ How to Run the Project
https://spam-classification29.streamlit.app/

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run Streamlit App

```bash
streamlit run app.py







