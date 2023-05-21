#Lab 2
#1-	Connect to Twitter account and Extract first 100 tweets from it in a file

import tweepy
import pandas as pd
import csv
import re
import string
import preprocessor as p

consumer_key = "QvPhWYeUMHVcFtM4UjFk7gdrm"
consumer_secret = "XP0b3lT8FyX0drEYeb6qGiZbUfzXmfNcuHN34qgRWf2XZbsWhT"
access_key = "858886404591333376-5PUlvH7SIRkKXyWOQDdWLnPXQdR6vZC"
access_secret = "atBJYZ5jU3Ka8LeKwp7Df6VQQOFGtO0djAokxHoTUZmfj"
bearer_key="AAAAAAAAAAAAAAAAAAAAAICPlQEAAAAAFkHSzq2jnwMEpf8wmoNUDgKM%2Fzg%3De4kQBj97JAvkFeLsVoix7h6s8HVfQxRJtPduZ1gBF4lE4isUTm"



#make a connection with API v2
import requests

client = tweepy.Client( bearer_token=bearer_key,
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token=access_key,
                        access_token_secret=access_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)


#Defining a query
query = 'from:joonsquotes -is:retweet'
# retweets and limit of tweets to 100

# get max. 100 tweets
tweets = client.search_recent_tweets(query=query,tweet_fields=['author_id', 'created_at'],max_results=100)

#conversion to pandas dataframe
import pandas as pd

# Save data as dictionary
tweets_dict = tweets.json()

# Extract "data" value from dictionary
tweets_data = tweets_dict['data']

# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)

print(df)

#save
df.to_csv("namjoon_lyrics_tweets.csv")