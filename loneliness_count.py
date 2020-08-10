import pandas as pd
import re
import datetime as dt
import os
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt


#Open files and generate polarity of every surbub



all_tweets_df = pd.DataFrame()
polarity_for_date = pd.DataFrame()
x = []
y = []
#################################get file date#################################
def get_date_list(begin_date, end_date):
    date_list = []
    begin_date = dt.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += dt.timedelta(days=1)
    return date_list


#################################get file name#################################
def get_file_path(date_list, i):
    date = date_list[i]
    path = '/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/' + date + '.csv'
    # path = 'E:/OneDrive - UTS/Reserach Project/twitter_project/dataset/' + date + '.csv'
    return path


#################################get file path#################################
file_path = []
date_list = get_date_list('2020-04-03', '2020-05-29')#date range
for i in range(0, len(date_list)):

    file_path.append(get_file_path(date_list,i))


def datapreprocess(dataframe):
    raw_string = dataframe.to_string()
    data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
        'This', "").replace('is', "").replace(":", "").replace('haigh', "").replace('snitched', "").replace('who', "")
    data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}', "", data)
    text_data = re.sub(r'\@[a-zA-Z]*[0-9]*', "", data)
    return text_data

words = ['miss','alone','friend','lonely','depressed','confused']
word_count = pd.DataFrame()
#################################check file exists and read and process#################################
for n in range(0, len(file_path)):
    path_open = file_path[n]
    date = date_list[n]
    if os.path.exists(path=path_open):
        print(path_open)
        data = pd.read_csv(path_open)
        all_tweets_df = all_tweets_df.append(data[["lga_name","text","lang"]],ignore_index=True)
        print("*********")
all_tweets_df = all_tweets_df.sort_values("lga_name")
print(all_tweets_df["text"])
blob = TextBlob(datapreprocess(all_tweets_df["text"]))
words = ['miss','friends','HOME','alone','lonely','depressed','confused']
phrases = ['artificial intelligence','I just wanna']
word_count = pd.DataFrame()
phrase_count = pd.DataFrame()
for word in words:
    count_word = blob.words.count(word)
    word_count = word_count.append({"word":[word],"count":[count_word]},ignore_index=True)
    print("*********")
# for phrase in phrases:
#     count_phrase = blob.noun_phrases.count(phrase)
#     phrase_count = phrase_count.append({"phrase":[phrase],"count":[count_phrase]},ignore_index=True)
#     print("*********")
print(word_count)
# print(phrase_count)
# tweets = all_tweets_df
# for tweet in all_tweets_df:
#     tweets = all_tweets_df["text"]
#     print(tweet)
print("end")

