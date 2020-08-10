from textblob import TextBlob
import pandas as pd
import re

# text = "I am so happy today what a happy day. I feel sad today."
# blob = TextBlob(text)
# # 分句
# # bloblist = blob.sentences
# print(blob)
#
# # 第一句的情感分析
# first = blob.sentences[0].sentiment
# print(first)
# # 第二句的情感分析
# second = blob.sentences[1].sentiment
# print(second)
# # 总的
# all = blob.sentiment
# print(all)


#Open files and generate sentiment of each twweet of each date


tweet_df = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/2020-04-03.csv")
# for tweetext in tweet_df:
#     tweetext = tweet_df["text"]
#     string = tweetext.to_string()
#     data = re.sub(r'^@.*\:',"",string)
#     data = re.sub(r'@.*\:',"",data)
#     data = re.sub(r'^\@[a-zA-Z]*[0-9]*', "", data)
#     data = re.sub(r'\@[a-zA-Z]*[0-9]*',"",data)
#     data = data.replace('RT',"").replace('https',"").replace('NaN',"").replace('thi',"").replace('wa',"").replace('This',"").replace('is',"")

# t_text = "@harpandsword @warhors93740460 @annafifield Today is the day to commemorate the ancestors and the dead, please do n‚Ä¶ https://t.co/GCtVqBq1wk"
def datapreprocess(data_df):
    raw_string = data_df.to_string()
    data = raw_string.replace('RT', "").replace('https', "").replace('NaN', "").replace('thi', "").replace('wa', "").replace(
        'This', "").replace('is', "")
    # data = re.sub(r'^@.*\:',"",data)
    # data = re.sub(r'@.*\:',"",data)
    # data = re.sub(r'^\@[a-zA-Z]*[0-9]*', "", data)
    data = re.sub(r'\@[a-zA-Z]*[0-9]*',"",data)


    print(data)
    text_data = re.sub(r'\/\/t\.co\/[A-Za-z0-9]{0,10}',"", data)
    return text_data
pd.set_option('display.max_colwidth', 1000)
# print(datapreprocess(tweet_df["text"]))
data = datapreprocess(tweet_df["text"])
# print(type(data))
with open("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/text.text", "w") as f:
   f.write(data)
with open("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/text.text", "r") as f:

    for text in f:
        blob = TextBlob(text)
        print(blob.sentiment)

print("end")
f.close()
with open("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/text.text", "r") as d:
    str = d.read()
    blob_all = TextBlob(str)
    print(blob_all.sentiment)
    print("end all")
    d.close()


# print(type(data))
# blob = TextBlob(data)
# all = blob.sentiment
# print(all)

