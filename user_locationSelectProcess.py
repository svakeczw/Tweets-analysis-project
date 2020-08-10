import numpy as np
import pandas as pd
import os
import datetime as dt
from datetime import timedelta

#list_1 = np.array([1,1,1,3,3,3,5,5,52,2,2,54,5,7,75,4,234])
#list_df = pd.DataFrame(data=list_1)
#print(list_df)


#Select unique user from different location


empty_data = {"lga_name": [], "user_id": []}
previous_df = pd.DataFrame(empty_data)
#################################process user id#################################
def user_process(data_set):
    df1 = pd.DataFrame({"user_id":data["user_id"].unique()})
    df2 = data_set[["lga_name","user_id"]]
#    print(df1)
    new_df = pd.merge(df1, df2, on='user_id')
    #previous_df = new_df
    #print(new_df)
    #print(previous_df)
#    new_df.to_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/newsample.csv")
    return new_df


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
    path = 'E:/OneDrive - UTS/Reserach Project/twitter_project/tweetsdata/' + date + '.csv'
    return path


#################################get file path#################################
file_path = []
list = get_date_list('2020-04-03', '2020-04-30')#date range
for i in range(0, len(list)):

    file_path.append(get_file_path(list,i))


#################################check file exists and read and process#################################

for n in range(0, len(file_path)):
    path_open = file_path[n]
    if os.path.exists(path=path_open):
        print(path_open)
        data = pd.read_csv(path_open)
        #        print(data)
        #        print("*************************************************")
        #        user_process(data)
        previous_df = previous_df.append(user_process(data),ignore_index=True)
        print(previous_df)
final_df = previous_df
final_df = final_df.sort_values(by="lga_name",axis=0)
#print(previous_df)
print(final_df)
#final_df.to_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/tweetsdata/user_lists.csv")
print("**************")
userlistdata = pd.read_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/tweetsdata/user_lists.csv")
final_list = user_process(userlistdata).drop_duplicates()
print(final_list)
final_list.to_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/tweetsdata/userid_lists.csv")

#print(np.unique(list_1))
#a = np.unique(list_1)
#print(a)
#userid_list = np.array([])
#data = pd.read_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/2020-04-03.csv")



#useridlist_df = pd.DataFrame({"lga_name":data["lga_name"].unique(),"user_id":data["user_id"].unique()})
#userdata = pd.merge(data,useridlist_df,how="inner")
#print(userdata)
#new = data.loc[data["user_id"]==useridlist_df["user_id"]]
#new = data[['lga_name', 'user_id']][(data["user_id"].unique())]


#print(df2)

#print(new_df)
#new_df.drop_duplicates(["user_id","lga_name"],keep="first")
#print(new_df)
#new_df.to_csv("E:/OneDrive - UTS/Reserach Project/twitter_project/df.csv")
#data.fillna(0, inplace = True)
#print(data)
#df1 = data[["lga_name","user_id"]]
#print(df1)
