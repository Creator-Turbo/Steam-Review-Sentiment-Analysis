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
**Link to Demo:** [Steam Review Sentiment Analysis](https://steam-review-sentiment-analysis.onrender.com) 

## Steam Review Sentiment Analysis

![Steam Sentiment Analysis](https://i.imgur.com/O6Q1lGv.png)


---

## Overview
The **Steam Review Sentiment Analysis** project focuses on analyzing user reviews from the Steam platform to classify them as positive  or negative. Using natural language processing (NLP) and machine learning techniques, the project provides insights into user feedback and gaming trends.
Add all algo

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
The Code is written in Python 3.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

# To clone the repository

```bash

gh repo clone Creator-Turbo/Steam-Review-Sentiment-Analysis

```
# Install dependencies: (all lib)
```bash
pip install -r requirements.txt
```



## Run
To train the Machine leaning models:
 To run the Flask web app locally
```bash
python app.py

```
# Deployment on Render

## To deploy the Flask web app on Render:
Push your code to GitHub.<br>
Go to Render and create a new web service.<br>
Connect your GitHub repository to Render.<br>
Set up the environment variables if required (e.g., API keys, database credentials).<br>
Deploy and your app will be live!



## Directory Tree 
```
.
├── data
│   ├── steam_reviews.csv
├── model
│   ├── sentiment_model.pkl
├── static
│   ├── style.css
├── templates
│   ├── index.html
├── app.py
├── train_model.py
├── requirements.txt
├── README.md

```

## To Do

- Define the project goal,"
 prepare the data, and train the model.
- Set up monitoring tools to track its performance.
- Automate the pipeline, document the process, test the system, and ensure continuous improvement.




## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. We welcome contributions!




## Technologies Used
Python 3.10<br> 
scikit-learn<br>
TensorFlow <br>
Flask (for web app development)  <br>
Render (for hosting and deployment)  <br>
pandas (for data manipulation) <br>
numpy (for numerical operations)  <br>
matplotlib (for visualizations) <br>



![](https://forthebadge.com/images/badges/made-with-python.svg)


[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/260px-Scikit_learn_logo_small.svg.png" width=170>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*RWkQ0Fziw792xa0S" width=170>](https://pandas.pydata.org/docs/)
  [<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDzf1RMK1iHKjAswDiqbFB8f3by6mLO89eir-Q4LJioPuq9yOrhvpw2d3Ms1u8NLlzsMQ&usqp=CAU" width=280>](https://matplotlib.org/stable/index.html) 
 [<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
 [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://aws.amazon.com/s3/) 







## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|


**Bablu Kumar Pandey**


- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
* **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)



## Credits

Special thanks to the contributors of the scikit-learn library for their fantastic machine learning tools.
