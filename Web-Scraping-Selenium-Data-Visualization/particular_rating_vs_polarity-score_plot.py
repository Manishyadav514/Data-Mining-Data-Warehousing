from collections import defaultdict, Counter
import json
import string
from pathlib import Path
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics
import csv
import nltk


# path of the file
current_path = str(Path().absolute())
link_to_data = current_path + "/Mined Data/Bangkok_Hotels_Details.json"


def analyse_sentiment(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    negative = score['neg']
    positive = score['pos']
    neutral = score['neu']
    compound = score['compound']
    return compound


with open(link_to_data) as f:
	data_content = json.loads(f.read())
i = 0
ratings = []
polarity_scores = []
for review in data_content[i]['comments']:
    current_review = review['comments'].lower()  # upper case letter to lower case conversion
    review_comments = current_review.translate(str.maketrans('', '', string.punctuation))  # Remove special character
    score = analyse_sentiment(review_comments)  # polarity score of the current review
    ratings.append(float(review['score']))
    polarity_scores.append(score*10)
print("ratings : " ,ratings)
print("Polarity Scores : ", polarity_scores)

hotel_name = data_content[i]['name']


# plotting reviews and ratings on the graph
import numpy as np
import matplotlib.pyplot as plt

X_axis = np.arange(len(ratings))

plt.bar(X_axis - 0.2, ratings, 0.4, label='Rating')
plt.bar(X_axis + 0.2, polarity_scores, 0.4, label='Polarity Score')

#plt.xticks(X_axis, hotel_name)
plt.xlabel(hotel_name)
plt.ylabel("Score out of 10")
plt.title("Graph of Polarity vs Rating for each hotel")
plt.legend()
plt.show()