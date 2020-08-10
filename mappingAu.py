import folium
import pandas as pd


location_df = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/nsw_lga_centroid_radius_128_new.csv")
# polarity_df = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/polarity_data_0403_0429_final.csv")
polarity_df = pd.read_csv("/Users/zhangweichen/OneDrive - UTS/Reserach Project/polarity_data_0401_0529_final.csv")
final_df = location_df.merge(polarity_df,on="lga_name",how="right")
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_column',1000)
# print(final_df)

m = folium.Map([-33.867139, 151.207114], zoom_start=8)


def addAveagecircle():
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        popup='Polarity:' + str(row['polarity']),
        tooltip=row['lga_name'],
        # radius=abs(row['polarity'] * 5000),
        radius=radius,
        color=marker_color,
        fill=True,
        fill_color=fill_color,
    ).add_to(m)

def addlowerLevelcircle():
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        popup='Polarity:' + str(row['polarity']),
        tooltip=row['lga_name'],
        radius=radius,
        color=marker_color,
        fill=True,
        fill_color=fill_color,
    ).add_to(m)


def addUpperLevelCircle():
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        popup='Polarity:' + str(row['polarity']),
        tooltip=row['lga_name'],
        # radius=row['polarity']*5000,
        radius=radius,
        color=marker_color,
        fill=True,
        fill_color=fill_color,
    ).add_to(m)

for index, row in final_df.iterrows():
    if -0.11 < row['polarity'] < 0:
        marker_color = 'darkred'
        fill_color = 'darkred'
        radius = 1500
        addlowerLevelcircle()
    elif row['polarity'] >= 0:
        # if row['polarity'] == 0:
        #     marker_color = 'yellow'
        #     fill_color = 'yellow'
        #     addZeroCircle()
        if 0 <= row['polarity'] < 0.1725:
            marker_color = 'blue'
            fill_color = 'blue'
            radius = 100
            addAveagecircle()
        if 0.1725 <= row['polarity'] <= 1:
            marker_color = 'purple'
            fill_color = 'purple'
            radius = 800
            addUpperLevelCircle()
        # if 0.5 < row['polarity'] <= 1:
        #     marker_color = 'green'
        #     fill_color = 'green'
        #     radius = 500
        #     addcircle()


m.save('mapping_0403_0429_ThreeLevel2.html')
print("end")