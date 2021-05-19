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
file_name = "Bangkok_Hotels_Details.json"
link_to_data = current_path + "/Mined Data/" + file_name


def analyse_sentiment(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    negative = score['neg']
    positive = score['pos']
    neutral = score['neu']
    compound = score['compound']
    return compound

details = []
priority_Score = []

with open(link_to_data) as f:
	data_content = json.loads(f.read())

print("We are still calculating polarity score... ")
for j in range(len(data_content)):
    total_polarity_score = 0
    temp_list = list()
    for review in data_content[j]['comments']:
        current_review = review['comments'].lower()     # upper case letter to lower case conversion
        review_comments = current_review.translate(str.maketrans('', '', string.punctuation))        # Remove special character
        current_polarity_score = analyse_sentiment(review_comments)        # polarity score of the current review
        total_polarity_score += current_polarity_score  # total polarity score
        temp_list.append(abs(current_polarity_score))
        score = statistics.median(temp_list)*10
    #details.append( [data_content[j]["name"], score] )    # add details in list
    details.append([data_content[j]["name"], data_content[j]["location"], data_content[j]["rating"], statistics.median(temp_list) * 10])
print("New hotel details with their names, locations, rating, polarity score :", details )


# writing file in csv
import csv
write_location = 'bangkok_polarity_vs_rating' + '.csv'
with open(write_location, 'a', encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerows(details)

