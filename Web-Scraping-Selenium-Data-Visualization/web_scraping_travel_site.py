import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re
import string
import time



# initializing chrome driver
driver = webdriver.Chrome("D:/project/DMDW-Data-Management-Data-Warehousing/Web-Scraping-Selenium/DMDW_BSoD_VDS/chromedriver.exe")
# driver search for the given url
driver.get("https://booking.com")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ss")))
print(element.text)



# Search Keyword
place = input('Name of the city : ')
#send kewyword to saerch bar
driver.find_element_by_xpath("//*[@id='ss']").send_keys(place)
# Target the search button an click
driver.find_element_by_class_name("sb-searchbox__button").click()
# Wait until it completes the search
hotels = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sr_property_block_main_row")))
print("Keep moving formward, we are searching...")



urls = []         # initializing empty array
# find elements by the given class
hotels = driver.find_elements_by_class_name('sr-hotel__title')
# increment the array with hotels urls
for hotel in hotels :
    url = hotel.find_element_by_class_name("hotel_name_link").get_attribute("href")
    urls.append(url)
time.sleep(5)
# prints number of urls
print("Number of hotels found : ", len(urls) )
print(urls)



# function to get hotel reviews
from selenium.webdriver.support.ui import Select
det = {}                  # initializing empty dictionary
def Hotel_Reviews():
    review_count = 100             # number of reviews we want
    reviews_list = []              # initialize empty array to store reviews and scores
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#guest-featured_reviews__horizontal-block > div > div.hp-featured_reviews-bottom > button"))).click()
    # to sort the review
    select = Select(driver.find_element_by_id('review_sort'))
    # select by value
    select.select_by_value('f_recent_desc')
    # search reviews untill the review count reaches to 100
    check = True
    while check:
        try:
            for review in driver.find_elements_by_class_name('review_list_new_item_block'):
                reviews = dict()
                try:
                    reviews['score'] = review.find_element_by_class_name('bui-review-score__badge').text
                except:
                    reviews['score'] = ""
                try:
                    reviews['comments'] = review.find_element_by_class_name('c-review-block__title').text
                except:
                    reviews['comments'] = ""
                reviews_list.append(reviews)
        except:
            return 0
        if len(reviews_list) >= review_count:
            check = False
        else:
            try:
                driver.find_element_by_class_name('pagenext').click()
                time.sleep(3)
            except:
                check = False
    return(reviews_list)
#det['review'] = Hotel_Reviews()
#print(det)



def Hotel_Details(url):
    #driver = webdriver.Chrome("D:/DMDW-Data-Management-Data-Warehousing-main/Web-Scraping-Selenium/chromedriver_win32/chromedriver.exe")
    driver.get(url)
    time.sleep(5)
    try:
        details = {}
        details['name'] = driver.find_element_by_class_name('hp__hotel-name').text
        details['rating'] = driver.find_element_by_class_name('bui-review-score__badge').text
        # fetching hotel reviews
        try:
            details['reviews'] = Hotel_Reviews()
        except:
            details['reviews'] = "NA"
    except:
        return 0
    return details



from tqdm import tqdm
# tqdm keeps track of the progress
All_Details = []
# range is 20 becasue we want details of 20 hotels
for i in tqdm(range(20)):
    All_Details.append([Hotel_Details(urls[i])])


# To write the details of hotels in csv file
import csv
# default path to file to store data
path_to_file = place + ".csv"
# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for i in range(len(All_Details)):
    print(All_Details[i][0])
    name = All_Details[i][0]['name']
    rating = All_Details[i][0]['rating']
    review = All_Details[i][0]['reviews']
    csvWriter.writerow([ name, rating, review])