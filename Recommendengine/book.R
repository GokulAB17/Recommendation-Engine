#Problem statement.
#Recommend a best book based on the ratings.


#Installing and loading the libraries
#install.packages("recommenderlab", dependencies=TRUE)
#install.packages("Matrix")
library("recommenderlab")
library(caTools)

#book rating data
books1 <- read.csv(file.choose())
View(books1)
books <- books1[-c(1,2)]
View(books1)
View(books)

#metadata about the variable
str(books)

#Rating distribution
hist(books$Book.Rating)


#the datatype should be realRatingMatrix inorder to build recommendation engine
books_matrix <- as(books, 'realRatingMatrix')
movie_recomm_model1 <- Recommender(books_matrix, method="POPULAR")


#Predictions for two users 
recommended_items1 <- predict(movie_recomm_model1, books_matrix[413:414], n=5)
as(recommended_items1, "list")



## Popularity model recommends the same movies for all users , we need to improve our model using # # Collaborative Filtering

#User Based Collaborative Filtering

movie_recomm_model2 <- Recommender(books_matrix, method="UBCF")

#Predictions for two users 
recommended_items2 <- predict(movie_recomm_model2, books_matrix[413:414], n=5)
as(recommended_items2, "list")


#Matrix factorization with LIBMF
movie_recomm_model3 <- Recommender(books_matrix, method="LIBMF")

#Predictions for two users 
recommended_items3 <- predict(movie_recomm_model3, books_matrix[413:414], n=5)
as(recommended_items3, "list")

#RANDOM recommendations
movie_recomm_model4 <- Recommender(books_matrix, method="RANDOM")

#Predictions for two users 
recommended_items4 <- predict(movie_recomm_model4, books_matrix[413:414], n=5)
as(recommended_items4, "list")


