# -*- coding: utf-8 -*-
"""final_data_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gIbWDsHm4NemzWg0TcjliSuYMRWdfqBG

##Final Projesi
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

raw_data=pd.read_csv('top50.csv',encoding='latin-1')

df=pd.DataFrame(raw_data)

df=df.drop('Unnamed: 0',axis=1)

df.head(51)

"""###Soru2:"""

df.Genre.unique() #all genres

genres=df.groupby(['Genre']).mean()
print(genres)

"""Sorting by Genres"""

sorted_df = df.sort_values(by='Genre')
 sorted_df=sorted_df.reset_index(drop=True)
 sorted_df.head()

#sorted_df.index.name= 'Song_name'
#print(sorted_df.index.name)
#sorted_df.index=sorted_df.index+1
sorted_df['Song_number']=sorted_df.index+1
sorted_df.head()

"""### Soru 2 : """

song_number=sorted_df['Song_number'].values
danceability=sorted_df['Danceability'].values
print("Danceability datas \n",danceability,"\n", type(danceability))
print("Song Number datas \n",song_number,"\n", type(song_number) )

b=(song_number,danceability)
plt.bar(*b)
plt.xlabel("Song Number")
plt.ylabel("Danceability point")
plt.xticks(np.arange(0, len(song_number)+1, 5))
plt.yticks(np.arange(0, max(danceability), 5))
plt.show()

"""###Soru 3 :"""

genre_means=df.groupby(['Genre']).mean()
genres_energies=genre_means['Energy']
print(genres_energies)

genres_unique=df.Genre.unique()

b=(genres_unique,genres_energies)
plt.bar(*b)
plt.xlabel("Genres")
plt.ylabel("Energy")
plt.yticks(np.arange(0, 100, 10))
plt.xticks(rotation=90)
plt.show()