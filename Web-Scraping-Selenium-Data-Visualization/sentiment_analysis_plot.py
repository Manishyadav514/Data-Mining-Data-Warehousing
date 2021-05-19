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


# fetching the path
current_path = str(Path().absolute())
path = current_path + "/Mined Data/Bangkok_Polarity_vs_Rating.csv"


hotel_name = []
rating = []
polarity_score = []

# Reading csv file
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        hotel_name.append(str(row[0])[7:10])
        rating.append(row[2])
        polarity_score.append(row[3])

import numpy as np
import matplotlib.pyplot as plt

X_axis = np.arange(len(hotel_name))

plt.bar(X_axis - 0.2, rating, 0.4, label='Rating')
plt.bar(X_axis + 0.2, polarity_score, 0.4, label='Polarity Score')

plt.xticks(X_axis, hotel_name)
plt.xlabel("Hotel Names")
plt.ylabel("Score out of 10")
plt.title("Graph of Polarity vs Rating")
plt.legend()
plt.show()
