import pandas as pd
import re
import datetime as dt
import os
from textblob import TextBlob


#Open files and generate polarity of every surbub



empty_data = {"text": []}
previous_df = pd.DataFrame(empty_data)
ld_df = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/nsw_lga_centroid_radius_128_new.csv")
lname = ld_df["lga_name"]
polarity_df = pd.DataFrame()
all_tweets_df = pd.DataFrame()


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
    return path


#################################get file path#################################
file_path = []
date_list = get_date_list('2020-04-01', '2020-05-29')#date range
for i in range(0, len(date_list)):

    file_path.append(get_file_path(date_list,i))


def datapreprocess(dataframe):
    raw_string = dataframe.to_string()
    data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
        'This', "").replace('is', "").strip().lstrip().replace(':',"")
    data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}', "", data)
    text_data = re.sub(r'\@[a-zA-Z]*[0-9]*', "", data)
    return text_data

def datapreprocess2(dataframe):
    text_data = dataframe.to_string()
    # raw_string = dataframe.to_string()
    # data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
    #     'This', "").replace('is', "").replace(":", "").replace('haigh', "").replace('snitched', "").replace('who', "")
    # data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}', "", data)
    # text_data = re.sub(r'\@[a-zA-Z]*[0-9]*', "", data)
    return text_data


#################################check file exists and read and process#################################
# pd.set_option('display.max_colwidth', 1000)
for n in range(0, len(file_path)):
    path_open = file_path[n]
    date = date_list[n]
    if os.path.exists(path=path_open):
        print(path_open)
        data = pd.read_csv(path_open)
        all_tweets_df = all_tweets_df.append(data[["lga_name","text","lang"]],ignore_index=True)
        print("*********")
all_tweets_df = all_tweets_df.sort_values("lga_name")
print(all_tweets_df)

for n in range(0,len(lname)):
    tweets = all_tweets_df.loc[all_tweets_df["lga_name"] == lname[n]]
    tweets_data = datapreprocess(tweets["text"])
    # tweets_data = datapreprocess2(tweets["text"])
    print((tweets_data))
    print("lname is: " + lname[n])
    blob_all = TextBlob(tweets_data)
    print(blob_all)
    all = blob_all.sentiment
    polarity_data = blob_all.polarity
    print("polarity data for " + lname[n] + " is: " + str(polarity_data))
    print("**********")
    polarity_df = polarity_df.append({"lga_name":lname[n],"polarity":polarity_data},ignore_index=True)

print(polarity_df)
# polarity_df.to_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/polarity_data_0403_0429_final2.csv")
# polarity_df.to_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/polarity_data_0501_0529_final.csv")
polarity_df.to_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/polarity_data_0401_0529_final.csv")
print("************************")
print("end")
