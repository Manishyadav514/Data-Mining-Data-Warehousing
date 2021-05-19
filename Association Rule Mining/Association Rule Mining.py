# Group Name: BSoD---
    # Group Members
        # 1. Manish Yadav
        # 2. Deepak Chaurasiya
        # 3. Aman Antil
# -------------------------------------------------------------------------------------------------------------



################################################################################################################
# function to use CSV file as our dataset in a list format
import csv
def readCSVfile(file):
	csvFile = open(file, 'r')
	csvRead = csv.reader(csvFile, delimiter=',')
	next(csvRead)
	dataStore = [[row] for row in csvRead]
	csvFile.close()
	return dataStore
dataset = [dataList[0] for dataList in readCSVfile("data.csv")]
print("--------------------Here is our dataset:-----------------------------------------")
for a in dataset:
    print(a)



###############################################################################################################
# Apriori Rule
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)              # Convert list to dataframe with boolean values
df = pd.DataFrame(te_ary, columns=te.columns_)
print("-------------------Checking whether items are in dataset 0 to 7 ----------------------")
print(df)

# To find frequently occurring itemsets using apriori principle
from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
print("-------------------------frequent item sets those which qualify minimum support------------------------")
print(frequent_itemsets)


###########################################################################################################
# Association Rule Mining
from mlxtend.frequent_patterns import association_rules
print("-----------------Association Rule Mining-----------------------")
result = association_rules(frequent_itemsets, metric = "confidence", min_threshold=0.2)[["antecedents", "support", "confidence", "lift"]]
print(result)

print("-----------------prints the dataset whose confidence is more than the given value-----------------------")
print( result[result["confidence"] >=0.7])        # we can replace confidence with support and left in order to get data base on this criteria.




# http://rasbt.github.io/mlxtend/user_guide/preprocessing/TransactionEncoder/