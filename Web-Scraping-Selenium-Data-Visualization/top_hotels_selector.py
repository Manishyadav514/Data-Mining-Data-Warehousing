import csv
from pathlib import Path
import os
print( os.getcwd())
# fetching the path
current_path = str(Path().absolute())
path = current_path + "/Mined Data/Bangkok_Polarity_vs_Rating.csv"


hotel_name = []
rating = []
polarity_score = []

# Reading csv file
def Get_Test_List(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        test_list = []
        for row in reader:
            a = []
            a.append(row[0])
            a.append(row[2])
            a.append(row[1])
            test_list.append(tuple(a))
    return test_list

test_list = Get_Test_List(path)
top_hotels = sorted(test_list, key=lambda x: x[1], reverse=True)[:10]
print("top 10 hotels: ", top_hotels)


# To write the details of hotels in csv file
import csv
write_location = 'bangkok_top_hotels_rating' + '.csv'
with open(write_location, 'a', encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerows(top_hotels)