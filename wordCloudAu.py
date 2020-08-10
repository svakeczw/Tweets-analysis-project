from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import re
import datetime as dt
import os


#Generate wordcloud


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
date_list = get_date_list('2020-04-01', '2020-05-30')#date range
for i in range(0, len(date_list)):

    file_path.append(get_file_path(date_list,i))


def datapreprocess(dataframe):
    raw_string = dataframe.to_string()
    data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
        'This', "").replace('is', "").replace(":","").replace('haigh',"").replace('snitched',"").replace('who',"").replace('Update for',"").replace('anyone',"").replace('not paying',"").replace('_MP',"").replace('If you',"").replace('What',"").replace('Ye',"")
    # data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('anyone',"").replace('Update for',"").replace('paying',"").replace('thi',"").replace('This is',"")
    data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}', "", data)
    data = data.replace('co',"")
    text_data = re.sub(r'\@[a-zA-Z]*[0-9]*', "", data)
    return text_data

#################################check file exists and read and process#################################
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)
for n in range(0, len(file_path)):
    path_open = file_path[n]
    date = date_list[n]
    if os.path.exists(path=path_open):
        print(path_open)
        data = pd.read_csv(path_open)
        all_tweets_df = all_tweets_df.append(data[["lga_name", "text", "lang"]], ignore_index=True)
        print("*********")
all_tweets_df = all_tweets_df.sort_values("lga_name")
print(all_tweets_df)
for tweetext in all_tweets_df:
    tweetext = all_tweets_df["text"]
    wordcloud_data = datapreprocess(tweetext)
    print(wordcloud_data)
    # print(tweetext)
print(wordcloud_data)
wc = WordCloud( width=800, height=600, mode='RGBA', background_color=None).generate(wordcloud_data)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/wordCloudPic/0501_0530_wc')
plt.show()
print("end")
