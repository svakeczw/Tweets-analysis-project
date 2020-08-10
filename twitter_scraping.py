import json
import tweepy
import pandas as pd
import numpy as py
from tweepy.parsers import JSONParser
import time
import csv
import sys
import os
import datetime


def init():
    # Step 1 - Authenticate
    consumer_key= ''
    consumer_secret= ''

    access_token=''
    access_token_secret=''
    #ZhzhKBHOwZW7uPhXUSADH20do
    #lEeWGeJ5RTZrb7EIXcndGefsvZeVL34Z9l9gq1jXIUSNDfCjxi
    #842703751374757888-GWHJrHmOoR39xXK8pjWzzkHOj8Aye2U
    #0SvLvrBoMDcOBOiaq6p1jwLBy3XmS5uhiOdnSvTIlI8Zb

    #dthtd5rgyGg256oEXIWO1UemY
    #euVVlzb9FCnManEwqgNuByuF0PKjeBxh3yi7CEDW9ZVos4xrhc
    #842548074413142017-vWBcip10tABfjdUPX1EkC3BqubQewRv
    #ccX7sulAWR47Y5EN0qc2ER7K3A2t9mDjrsysOBD9F7foy



    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth,wait_on_rate_limit=True)
    #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    return api



def write_csv(tweets,lga_data,lga_index,deduplicate_set):

    date=datetime.date.today().strftime('%Y-%m-%d')
    if not os.path.exists('{}.csv'.format(date)):
        headers=['lga_name', 'tweet_id','text','datetime','user_id','lang']
        with open('{}.csv'.format(date), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    with open('{}.csv'.format(date), 'a') as f:
        writer = csv.writer(f)
        for t in tweets:
            if t._json['id'] not in deduplicate_set:
                deduplicate_set.add(t._json['id'])
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(t._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                writer.writerow([lga_data['lga_name'][lga_index],t._json['id'],t._json['full_text'],ts,t._json['user']['id'],t._json['lang']])

# tweetsdata = pd.DataFrame(columns=('lga_name', 'tweet_id','text','datetime','user_id'), index=[])
def crawl_tweets(tweet_api):

    lga_data = pd.read_csv('./nsw_lga_centroid_radius_128_new.csv')
    lan_list = lga_data['latitude'].tolist()
    lan_list_str = [str(i) for i in lan_list]
    lon_list = lga_data['longitude'].tolist()
    lon_list_str = [str(i) for i in lon_list]
    radius_list = lga_data['lga_radius'].tolist()
    radius_list_str = [str(i) for i in radius_list]
    #LC_PLY_ID_list = data['LC_PLY_PID'].tolist()
    #LC_PLY_ID_list_str = [str(i) for i in LC_PLY_ID_list]
    NSW_LGA_list = lga_data['lga_name'].tolist()
    NSW_LGA_list_str = [str(i) for i in NSW_LGA_list]

    old_date=datetime.date.today().strftime('%Y-%m-%d')
    deduplicate_set=set() # deduplicate set

    while(True):
        print(lga_data.shape[0])

        if old_date != datetime.date.today().strftime('%Y-%m-%d'):
            old_date = datetime.date.today().strftime('%Y-%m-%d')
            deduplicate_set=set()

        for n in range(lga_data.shape[0]):

            geocode = lan_list_str[n]+","+lon_list_str[n]+","+radius_list_str[n]+"km"
            print(geocode)

            print("lga_index:{},{}".format(n,lga_data['lga_name'][n]))
            tweets =tweet_api.search(q='%20',tweet_mode='extended', since=old_date,count=2000,pages=15,geocode=geocode)

            write_csv(tweets,lga_data,n,deduplicate_set)

        print("sleep")
        time.sleep(3600*2)

if __name__=="__main__":
    tweet_api = init()
    crawl_tweets(tweet_api)





