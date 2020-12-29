#Problem statement.

#Recommend a best book based on the ratings.

import pandas as pd
#import Dataset 
bk = pd.read_csv(r"book.csv",encoding="ANSI")
bk.shape #shape
bk.columns
bk=bk.drop(["Unnamed: 0"],axis=1)#genre columns
len(bk["User.ID"].unique())
len(bk["Book.Title"].unique())

#EDA
bk["Book.Title"].isnull().sum() 
bk["Book.Rating"].isnull().sum()
bk["User.ID"].isnull().sum()

import numpy as np
import matplotlib.pyplot as plt
plt.hist(bk["Book.Rating"])

from sklearn.preprocessing import scale
bk_Rating=np.matrix(pd.get_dummies(scale(bk["Book.Rating"])))

# For now we will be using cosine similarity matrix

from sklearn.metrics.pairwise import linear_kernel
cosine_sim_matrix = linear_kernel(bk_df,bk_df)

# creating a mapping of bk name to index number 
bk_index = pd.Series(bk.index,index=bk['Book.Title']).drop_duplicates()

def get_bk_recommendations(Name,topN):
    
   
    #topN = 10
    # Getting the movie index using its title 
    bk_id = bk_index[Name]
    
    # Getting the pair wise similarity score for all the bk's with that 
    # bk
    cosine_scores = list(enumerate(cosine_sim_matrix[bk_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores,key=lambda x:x[1],reverse = True)
    
    # Get the scores of top 10 most similar bk's 
    cosine_scores_10 = cosine_scores[0:topN]
    
    # Getting the bk index 
    bk_idx  =  [i[0] for i in cosine_scores_10]
    bk_scores =  [i[1] for i in cosine_scores_10]
    
    # Similar movies and scores
    bk_similar_show = pd.DataFrame(columns=["name","Score"])
    bk_similar_show["name"] = bk.loc[bk_idx,"Book.Title"]
    bk_similar_show["Score"] = bk_scores
    bk_similar_show.reset_index(inplace=True)  
    bk_similar_show.drop(["index"],axis=1,inplace=True)
    print (bk_similar_show)
    return (bk_similar_show)

    
# Enter your bk and number of bk's to be recommended 
y=get_bk_recommendations("El Senor De Los Anillos: LA Comunidad Del Anillo (Lord of the Rings (Spanish))",topN=5)

#Prints top5 recommended books for the same