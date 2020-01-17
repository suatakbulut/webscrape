"""
This is to search for tweets about a user-provided subject. 
Returns the user-given number of tweets. 
"""

import tweepy 
import csv

subject = input("Subject of the tweets you want:  ")   
number_of_tweets = int(input("Number of the desired results:  "))
print("Please verify that you are authorized for this: \n")

# For security reasons I am not writing my keys, instead I ask the user to provide with those information.
consumer_key  = input(" Please enter your consumer key: \n")
consumer_secret  = input(" Please enter your consumer secret: \n")
access_token  = input(" Please enter your access token: \n")
access_token_secret  = input(" Please enter your access token secret: \n")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create the file name
file_name = "Tweets_About_"+ subject.capitalize() + ".csv"

with open(file_name, 'w', newline='') as file:
    w = csv.writer(file)
    w.writerow(['timestamp', 'tweet_text', 'username', 'followers_count'])
    # loop through the related tweets
    for tweet in tweepy.Cursor(api.search, 
                       q = "turkey" + "-filter:retweets", 
                       lang="en", 
                       tweet_mode="extended").items(number_of_tweets):
        w.writerow([tweet.created_at, tweet.full_text.replace("\n", " ").encode("utf-8"), tweet.user.screen_name.encode("utf-8"), tweet.user.followers_count])
# Infor the user when the file is ready
print("\n" + file_name + " has been created. ") 