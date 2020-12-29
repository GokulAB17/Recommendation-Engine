
import pandas as pd
import numpy as np

movies_df = pd.read_csv(r'C:\Users\Administrator.Gokulbhasi\Desktop\DataScience\Assignments\Recommendengine\Movie.csv')


movies_df[0:5]
#number of unique users in the dataset
len(movies_df.userId.unique())

user_movies_df = movies_df.pivot(index='userId',
                                 columns='movie',
                                 values='rating').reset_index(drop=True)

user_movies_df

user_movies_df.index = movies_df.userId.unique()

user_movies_df

#Impute those NaNs with 0 values
user_movies_df.fillna(0, inplace=True)

user_movies_df
y=pairwise_distances( user_movies_df.values,metric='cosine')
#Calculating Cosine Similarity between Users
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation

user_sim = 1 - pairwise_distances( user_movies_df.values,metric='cosine')

user_sim

#Store the results in a dataframe
user_sim_df = pd.DataFrame(user_sim)

#Set the index and column names to user ids 
user_sim_df.index = movies_df.userId.unique()
user_sim_df.columns = movies_df.userId.unique()


user_sim_df.iloc[0:5, 0:5]

np.fill_diagonal(user_sim, 0)
user_sim_df.iloc[0:5, 0:5]

#Most Similar Users
user_sim_df.idxmax(axis=1)[0:5]

movies_df[(movies_df['userId']==6) | (movies_df['userId']==168)]

user_1=movies_df[movies_df['userId']==6]

user_2=movies_df[movies_df['userId']==11]

user_2.movie

user_1.movie

pd.merge(user_1,user_2,on='movie',how='outer')
