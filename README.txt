Email Classification using Naïve Bayes

 #Overview
This project classifies emails as **spam** or **ham** (not spam) using the **Naïve Bayes** algorithm. The model is trained on a dataset containing labeled emails and deployed using **Streamlit** for easy access.

 #Features
- **Text Preprocessing**: Tokenization, stopword removal, and TF-IDF vectorization.
- **Naïve Bayes Classifier**: A probabilistic model for classification.
- **Streamlit Web App**: User-friendly interface for testing email classification.

#Dataset
The dataset contains labeled emails with two categories:
- **Spam**: Unwanted emails, advertisements, and phishing attempts.
- **Ham**: Regular, useful emails.

#Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/email-classification.git
   cd email-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

#ModelTraining
1. Load and preprocess the dataset.
2. Convert text into numerical features using TF-IDF.
3. Train a **Multinomial Naïve Bayes** classifier.
4. Evaluate model accuracy on test data.

#Usage
- Open the app and input an email text.
- Click the "Classify" button.
- The model predicts if the email is **Spam** or **Ham**.

[Click here to access the app](#) *(https://spam-classification29.streamlit.app/)*
## Web App Link


Performance Metrics (on test data)
Metric	Value
Accuracy	~98%
Precision	~96–99%
Recall	~95–98%
F1-Score	~97%




