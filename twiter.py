from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Import Dependencies

# PATH = "C:\Program Files\drivers\chromedriver_103.exe"
# driver = webdriver.Chrome(PATH)
# driver.get("https://twitter.com/login")
driver.get("https://twitter.com/bbcbangla")

UserTags = []
TimeStamps = []
Tweets = []
Replys = []
reTweets = []
Likes = []

articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
while True:
    for article in articles:
        UserTag = driver.find_element(
            By.XPATH, ".//div[@data-testid='User-Names']").text
        UserTags.append(UserTag)

        TimeStamp = driver.find_element(
            By.XPATH, ".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)

        Tweet = driver.find_element(
            By.XPATH, ".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)

        Reply = driver.find_element(
            By.XPATH, ".//div[@data-testid='reply']").text
        Replys.append(Reply)

        reTweet = driver.find_element(
            By.XPATH, ".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)

        Like = driver.find_element(
            By.XPATH, ".//div[@data-testid='like']").text
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(
        By.XPATH, "//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break


print(len(UserTags),
      len(TimeStamps),
      len(Tweets),
      len(Replys),
      len(reTweets),
      len(Likes))
print(Tweets)
