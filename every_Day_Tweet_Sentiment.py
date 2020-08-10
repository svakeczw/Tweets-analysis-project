import pandas as pd
import re
import datetime as dt
import os
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt


#Open files and generate polarity of every surbub



tweets = pd.DataFrame()
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
date_list = get_date_list('2020-04-01', '2020-04-29')#date range
for i in range(0, len(date_list)):

    file_path.append(get_file_path(date_list,i))


def datapreprocess(dataframe):
    text_data = dataframe.to_string()
    # raw_string = dataframe.to_string()
    # data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
    #     'This', "").replace('is', "").replace(":", "").replace('haigh', "").replace('snitched', "").replace('who', "")
    # data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}', "", data)
    # text_data = re.sub(r'\@[a-zA-Z]*[0-9]*', "", data)
    return text_data


#################################check file exists and read and process#################################
pd.set_option('display.max_colwidth', 1000)
for n in range(0, len(file_path)):
    path_open = file_path[n]
    date = date_list[n]
    if os.path.exists(path=path_open):
        print(path_open)
        data = pd.read_csv(path_open)

        # tweets.to_csv('/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/processed_data_0504.csv')
        #     tweet = datapreprocess(data["text"])
        #     tweets = tweets.append({"text":tweet},ignore_index=True)
        print("*********")
        tweets_data = datapreprocess(data["text"])
        # print(tweets_data)

        bolb_all = TextBlob(tweets_data)
        # print(tweet)
        # print(tweets)
        # print(bolb_all)
        polarity = bolb_all.polarity
        print("Polarity for " + date + " is: " + str(polarity))
        polarity_for_date = polarity_for_date.append({"date":date,"polarity":polarity},ignore_index=True)
#
# print(polarity_for_date)
# polarity_for_date.to_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/polarity_for_date_0410-0421.csv")
# polarity_for_date.to_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/tweetsdata/polarity_for_date1.csv")
polarity_for_date.to_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/polarity_for_date_0401-0429.csv")
print("end")

# for x,y in polarity_for_date:
#     x = x.append[polarity_for_date["date"]]
#     y = y.append[polarity_for_date["polarity"]]
#
#
#
# plt.plot(x, y1, label='y = sin(x)')
# plt.plot(x, y2, label='y = cos(x)')
# plt.legend()
# plt.show()
