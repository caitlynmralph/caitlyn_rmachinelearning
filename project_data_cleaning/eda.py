# thanks to DLao @ Hong Kong (https://www.kaggle.com/laowingkin/netflix-movie-recommendation/notebook) for the data cleaning code

# importing essential packages
import numpy as np
import pandas as pd
import math
import re
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix
from surprise import Reader, Dataset, SVD, evaluate


# load data for 1st txt file
ratings_1 = pd.read_csv("combined_data_1.txt", header = None, names = ['CustomerID','Rating','Date'], usecols = [0,1,2])

# Make the rating as type float
ratings_1['Rating'] = ratings_1['Rating'].astype(float)

# printing the head to see if it worked
#print(ratings_1.head(n=5))

# get movie count by finding all the NA values
movie_count = ratings_1.isnull().sum()[1]
#print("Movie Count: " + str(movie_count))

# get customer count by subtracting number of unique customer ids by the count of the NA values represented by movie_count
customer_count = ratings_1['CustomerID'].nunique() - movie_count
#print("CustomerID Count: " + str(customer_count))

# get rating count by subtracting the total observation count by the count of the NA values represented by movie_count
rating_count = ratings_1['CustomerID'].count() - movie_count
#print("Rating Count: " + str(rating_count))

# exporting to csv
#ratings_1.to_csv("ratings_1", sep=',', encoding='utf-8')

movie_id = np.empty([rating_count, 1], dtype = int)
movie_title = np.empty([rating_count, 1], dtype = object)
release_year = np.empty([rating_count, 1], dtype = int) 
count = 0
movie_titles = pd.read_csv("movie_titles_cleaned.csv", header = None, names = ['MovieID','Release Year','MovieTitle'], usecols = [0,1,2])

for i in range(0, len(ratings_1)):
    if pd.isnull(ratings_1['Rating'][i]):
        movie_id_instance = ratings_1['CustomerID'][i]
    else:
        movie_id[count,:] = movie_id_instance[:-1]
        movie_title[count,:] = movie_titles['MovieTitle'][int(movie_id_instance[:-1]) - 1]
        release_year[count,:] = movie_titles['Release Year'][int(movie_id_instance[:-1]) - 1]
        count += 1

ratings_1_complete = ratings_1.dropna()

if (len(ratings_1_complete) == len(movie_id) and len(ratings_1_complete) == len(movie_title) and len(ratings_1_complete) == len(release_year)):
    print("We're so freaking good man")
    ratings_1_complete["MovieID"] = movie_id
    ratings_1_complete["MovieTitle"] = movie_title
    ratings_1_complete["Release Year"] = release_year
    ratings_1_complete.to_csv("ratings_1.csv", sep=',', encoding='utf-8')
    print(ratings_1_complete.head())

else:
    print("You messed up smh...")
    print("Difference of movie id: " + str(len(ratings_1_complete) - len(movie_id)))
    print("Difference of movie title: " + str(len(ratings_1_complete) - len(movie_title)))
    print("Difference of release year: " + str(len(ratings_1_complete) - len(release_year)))