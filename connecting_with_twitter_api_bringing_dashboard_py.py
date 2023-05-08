# -*- coding: utf-8 -*-
"""Connecting with Twitter API. Bringing Dashboard.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ux9kBunVHldiCwri5YxKq6gwGHOz2c-_
"""

get_ipython().system('pip install tweepy')
get_ipython().system('pip install geocoder')

import tweepy
import pandas as pd
import geocoder

cos_key="mx5EJBuHZK2gaMm8FtuPhx0Rf"
cos_secret="cZHZeSTebSSkDAmLpYA9YzF9U77JtsbWdNiaDi18ecsMq4Flw0"
acs_tokn="4500086892-BUcwnowx8QfEpBbG6ks0UXG1KrVs8kFRqbdDTAQ"
acs_tokn_secret="ZNQbCKYiYrb1b0404tWDHoLQUTsebMYx10OYUzULpAGhO"

auth1=tweepy.OAuthHandler(cos_key,cos_secret)
auth1.set_access_token(acs_tokn,acs_tokn_secret)
api=tweepy.API(auth1)

woid = 23424848

trds = api.get_place_trends(id = woid, exclude = "hashtags")
print("The top trends for the location are :")
for value in trds:
    for trend in value['trends']:
        print(trend['name'])

get_ipython().system('pip install textblob')
get_ipython().system('pip install pycountry')

from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import nltk
import pycountry
import re
import string

from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

import nltk
nltk.downloader.download('vader_lexicon')

def percentage(part,whole):
    return 100 * float(part)/float(whole)

key = input("Please enter keyword or hashtag to search: ")
nofTweet = int(input ("Please enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search_tweets,q=key).items(nofTweet)
pve = 0
nve = 0
nutral = 0
polarity = 0
tweet_list = []
nutral_list = []
nve_list = []
pve_list = []

for tweet in tweets:
#print(tweet.text)
    tweet_list.append(tweet.text)
    analyze = TextBlob(tweet.text)
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    scor = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = scor['neg']
    neu = scor['neu']
    pos = scor['pos']
    comp = scor['compound']
    polarity += analyze.sentiment.polarity

if neg > pos:
        nve_list.append(tweet.text)
        nve += 1
    elif pos > neg:
        pve_list.append(tweet.text)
        pve += 1
    elif pos == neg:
        nutral_list.append(tweet.text)
        nutral += 1

positive = percentage(pve, nofTweet)
negative = percentage(nve, nofTweet)
neutral = percentage(nutral, nofTweet)
polarity = percentage(polarity, nofTweet)

positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(nutral_list)
negative_list = pd.DataFrame(nve_list)
positive_list = pd.DataFrame(pve_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))

lebl = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
siz = [positive, neutral, negative]
clrs = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(siz,colors=clrs, startangle=90)
plt.style.use('default')
plt.legend(lebl)
plt.title("Sentiment Analysis Result for keyword= "+key+"" )
plt.axis("equal")
plt.show()