# -*- coding: utf-8 -*-
"""Spam_Classification .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AyI1ZzPls5lpUE88avlFuXayiUFDcNY6
"""

!pip install scikit-learn
!pip install pandas

# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Upload CSV File in Google Colab
# In Colab, run this cell to upload the CSV file
from google.colab import files
uploaded = files.upload()

# Load the uploaded CSV file into a DataFrame
# Replace 'filename.csv' with the name of your uploaded file
df = pd.read_csv(next(iter(uploaded)))

# Step 2: Inspect the Data
print("First 5 rows of the dataset:")
print(df.head())

# Ensure your CSV file has columns named 'Message' and 'Label'.
# If your column names are different, replace 'Message' and 'Label' in the following code.

# Step 3: Preprocessing
# Map labels to numeric values (e.g., spam = 1, ham = 0)
df['Label'] = df['Label'].map({'ham': 0, 'spam': 1})

# Split the data into features (X) and labels (y)
X = df['Message']
y = df['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create a Pipeline
# The pipeline combines CountVectorizer, TfidfTransformer, and MultinomialNB
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

# Step 5: Train the Model
pipeline.fit(X_train, y_train)

# Step 6: Test the Model
y_pred = pipeline.predict(X_test)

# Print evaluation metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Step 7: Test with Custom User Messages
# Take user input
user_message = input("Enter a message to check: ")

# Predict whether the message is spam or not
prediction = pipeline.predict([user_message])[0]

# Print the result
print(f"Message: '{user_message}' -> {'Spam' if prediction == 1 else 'Not Spam'}")

# prompt: code for saving the model using pickle

import pickle

# Save the trained model
filename = 'spam_detection_model.pkl'
pickle.dump(pipeline, open(filename, 'wb'))

print(f"Model saved to {filename}")