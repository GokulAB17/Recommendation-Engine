# -*- coding: utf-8 -*-
#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load Dataset
book_df = pd.read_csv('book.csv', encoding="unicode-escape")

#EDA and Data Preprocessing
book_df.head()

book_df.info()

#number of unique users
len(book_df["User.ID"].unique())
#2182 users

len(book_df["Book.Title"].unique())

plt.hist(book_df["Book.Rating"])
# maximum rating is from 7 to 10

#User to User Collaborating
# to make data frame in required format to do similarity 
user_book_df = book_df.pivot_table(index="User.ID",columns='Book.Title',values='Book.Rating').reset_index(drop=True)

user_book_df

len(user_book_df)

user_book_df.index = book_df["User.ID"].unique()

#Impute those NaNs with 0 values
user_book_df.fillna(0, inplace=True)

#Calculating Cosine Similarity between Users
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation

user_book_df.head()

user_sim = 1 - pairwise_distances( user_book_df.values,metric='cosine')

user_sim

#Store the results in a dataframe
user_sim_df = pd.DataFrame(user_sim)

user_sim_df

#Set the index and column names to user ids 
user_sim_df.index = book_df["User.ID"].unique()
user_sim_df.columns = book_df["User.ID"].unique()

user_sim_df.iloc[0:5, 0:5]

np.fill_diagonal(user_sim, 0)
user_sim_df.iloc[0:5, 0:5]

#Most Similar Users and get first 5 combinations
user_sim_df.idxmax(axis=1)[0:5]

book_df[(book_df['User.ID']==276744) | (book_df['User.ID']==276726)] # similar users

user_1=book_df[book_df['User.ID']==276744]

user_2=book_df[book_df['User.ID']==276726]

user_1["Book.Title"]# book recommend to user2

user_2["Book.Title"] # book recommend to user1

#Item to Item Collaborating
item_book_df = book_df.pivot_table(index="Book.Title",columns='User.ID',values='Book.Rating').reset_index(drop=True)

item_book_df

item_book_df.index = book_df["Book.Title"].unique()

item_book_df

#Impute those NaNs with 0 values
item_book_df.fillna(0, inplace=True)

item_book_df

item_sim = 1 - pairwise_distances( item_book_df.values,metric='cosine')

item_sim

item_sim_df=pd.DataFrame(item_sim)

#Set the index and column names to Book.Title 
item_sim_df.index = book_df["Book.Title"].unique()
item_sim_df.columns = book_df["Book.Title"].unique()

item_sim_df.iloc[0:5, 0:5]

np.fill_diagonal(item_sim, 0)
item_sim_df.iloc[0:5, 0:5]

#Most Similar items
item_sim_df.idxmax(axis=1)[0:5]

book_df[(book_df['Book.Title']=="Classical Mythology") | (book_df['Book.Title']=="Clara Callan")]

user_1=book_df[book_df['Book.Title']=="Classical Mythology"]

user_2=book_df[book_df['Book.Title']=="Clara Callan"]

user_2 #recommend Classical Mythology

user_1 #Recommend Clara Clan