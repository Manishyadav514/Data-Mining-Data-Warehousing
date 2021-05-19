import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
from dataclasses import make_dataclass
import copy


#---------------------------------------------------------------------------------------------------------------------------
# function to read data from a csv file
def readCSVfile(file):
	csvFile = open(file, 'r')
	csvRead = csv.reader(csvFile, delimiter=',')
	next(csvRead)
	dataStore = [[row[0], [float(row[1]), float(row[2])]] for row in csvRead]
	csvFile.close()
	return dataStore
# Function to create random centroid
def centroid():
    d = []
    for i in range(k):
        a = [np.random.randint(0, 100), np.random.randint(0, 100)]
        d.append(a)
    return d
# function to calculate distance
def calcDistance(x1, y1,x2,y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5
#---------------------------------------------------------------------------------------------------------------------------
# deriver function
list_of_points = [dataList[1] for dataList in readCSVfile("min data.csv")]          # It extract datapoints from csv file and add them in a list
Point = make_dataclass("Point", [("x", int), ("y", int)])                           # It construct DataFrame from dataclass mp
data = pd.DataFrame([Point(a[0], a[1]) for a in list_of_points])                      # dataframe
k = 3
centroids = centroid()
# plotting random centroid and given values
color_list = ["r", "y", "b", "g"]
def plot(data, centroids):
    fig = plt.figure(figsize=(7, 3))
    plt.scatter(data['x'], data['y'], color='k')
    for i in range(k):
        plt.scatter(*centroids[i], color = color_list[i])
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()
plot(data, centroids)






#---------------------------------------------------------------------------------------------------------------------------
# function to calculate distance of each points from the centroid
def KMeans(df, centroids):
   for i in range(k):
       # it calculates the distance from centroid and add in dataframe
       data['distance_from_{}'.format(i)] = (calcDistance(data['x'], data['y'], centroids[i][0], centroids[i][1]))
   centroid_distance_cols = ['distance_from_{}'.format(i) for i in range(k)]
   data['cluster'] = data.loc[:, centroid_distance_cols].idxmin(axis=1)
   data['cluster'] = [int(x.lstrip("distance_from_")) for x in data["cluster"]]
   data['color'] = [color_list[a] for a in data["cluster"] ]
   return df

data = KMeans(data, centroids)
print(data.head(10))                                      # it prints 10 points and there distances from centroids
fig = plt.figure(figsize=(7, 3))
plt.scatter(data['x'], data['y'], color=data['color'], alpha=0.5, edgecolor='k')
for i in range(k):
   plt.scatter(*centroids[i], color=color_list[i])
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()






#-------------------------------------------------------------------------------------------------------------------
# function to update the centroid
old_centroids = copy.deepcopy(centroids)
def updateCentroid(centroids):
   for i in range(len(centroids)):
       centroids[i][0] = np.average(data[data['cluster'] == i]['x'])               # average of x co-ordinate of points in i cluster
       centroids[i][1] = np.average(data[data['cluster'] == i]['y'])               # average of y co-ordinate of points in i cluster
   return centroids

centroids = updateCentroid(centroids)
fig = plt.figure(figsize=(7, 3))
ax = plt.axes()
plt.scatter(data['x'], data['y'], color=data['color'], alpha=0.5, edgecolor='k')
for i in range(k):
   plt.plot(*centroids[i], color=color_list[i], marker=".", markersize = 20)
   plt.plot(*old_centroids[i], color="k", marker=".", markersize= 10)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()



#-------------------------------------------------------------------------------------------------------------------
# will repeat the K-means algorithm until we get no changes in further iteration
number_of_iteration = int(input("Enter the number of interation you wanna perform : "))
i = 0
while True:
   older_cluster = data['cluster'].copy(deep=True)
   centroids = updateCentroid(centroids)
   data = KMeans(data, centroids)
   if older_cluster.equals(data['cluster']) or (i > number_of_iteration):
       break
   i +=1
fig = plt.figure(figsize=(7, 3))
plt.scatter(data['x'], data['y'], color=data['color'], alpha=0.5, edgecolor='k')
for i in range(len(centroids)):
   plt.plot(*centroids[i], color=color_list[i], marker=".", markersize = 20)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()