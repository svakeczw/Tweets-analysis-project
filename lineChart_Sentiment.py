import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re


x = ['10/05', '11/05', '12/05', '13/05', '14/05', '15/05', '16/05', '17/05', '18/05', '19/05', '20/05', '21/05']
y = []
y1 = []
y2 = []

# polarity_for_date = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/polarity_for_date.csv")
polarity_for_date = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/polarity_for_date_0510-0521.csv")
plt.figure(figsize=(16, 9))

for index,row in polarity_for_date.iterrows():
    # date = re.sub(r'2020-',"",row["date"])
    date = re.sub(r'\/20',"",row["date"])
    date.replace('/5','/05')

    polarity = row["polarity"]
    # x.append(date)
    y.append(polarity)
    y1.append(0.1198)


for a,b in zip(x,y):
    plt.text(a, b, '%.4f' % b, ha='center', va= 'bottom',fontsize=10)

print(x)
print(y)



plt.title('Polarity trend from 10/05/2020 to 21/05/2020 in NSW')
plt.plot(x, y,label="polarity",c='black',ls='-',lw=2,marker='.',mec='r')
plt.plot(x,y1,label="average in May",c="blue",ls='--')
plt.xticks(rotation=-45)

# plt.plot(x, y2, label='y = cos(x)')
plt.legend(loc=0)
plt.savefig("/Users/zhangweichen/OneDrive - UTS/Reserach Project/twitter_project/dataset/polarityLineChart_for_0510-0521_2.png")
plt.show()

