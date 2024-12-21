from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer
model = pickle.load(open('model/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/count_vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

## updated code here show it on githube 
@app.route('/predict', methods=['POST'])
def predict():
    if 'review' in request.form:
        review_text = request.form['review']
        
        # Transform the review text using the fitted vectorizer
        review_vector = vectorizer.transform([review_text])
        print(review_text)
        
        # Make a prediction

        prediction = model.predict(review_vector)
        sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
        
        return render_template('result.html', sentiment=sentiment)
    else:
        return "Error: Review text is missing", 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
