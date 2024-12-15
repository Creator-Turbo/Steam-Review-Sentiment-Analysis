from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer
model = pickle.load(open('model/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/tfidf_vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review_text = request.form['review']
        # Transform the text using the vectorizer
        review_vector = vectorizer.transform([review_text])
        prediction = model.predict(review_vector)
        sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
        return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
