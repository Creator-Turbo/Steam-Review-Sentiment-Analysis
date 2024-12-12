## End to End ML Project 

# Steam Review Sentiment Analysis

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [Credits](#credits)

---

## Demo
This project processes user reviews of Steam games and predicts whether the sentiment is positive or negative.  
**Link to Demo:** [Steam Review Sentiment Analysis](https://steam-sentiment-analysis.onrender.com)

![Steam Sentiment Analysis](sentiment_analysis.jpg)

---

## Overview
The **Steam Review Sentiment Analysis** project focuses on analyzing user reviews from the Steam platform to classify them as positive or negative. Using natural language processing (NLP) and machine learning techniques, the project provides insights into user feedback and gaming trends.

Key features:
- Preprocessing of review text data
- Sentiment classification using machine learning models
- Interactive web application for real-time predictions

---

## Motivation
Analyzing user sentiment in reviews helps game developers and stakeholders understand user satisfaction and address critical feedback. This project demonstrates the practical use of NLP and machine learning to solve a real-world problem in the gaming industry.

---

## Technical Aspect
### Training Machine Learning Models:
1. **Data Collection**: Reviews are collected from the Steam platform dataset.
2. **Preprocessing**:
   - Tokenization, stop-word removal, and stemming/lemmatization.
   - Converting text to numerical features using methods like Bag-of-Words or TF-IDF.
3. **Model Training**:
   - Classifiers such as Logistic Regression, Naive Bayes, or Random Forest.
   - Hyperparameter tuning for optimal performance.
4. **Model Evaluation**:
   - Performance metrics include accuracy, F1 score, precision, and recall.

### Building and Hosting a Flask Web App:
1. A Flask-based web application allows users to input reviews and view sentiment predictions in real-time.
2. Deployment on Render for easy access.

---

## Installation
The code is written in Python 3.10. To install the required libraries, clone the repository and run:

```bash
# Clone the repository
gh repo clone Creator-Turbo/Steam-Review-Sentiment-Analysis

# Navigate to the project directory
cd Steam-Review-Sentiment-Analysis

# Install dependencies
pip install -r requirements.txt
