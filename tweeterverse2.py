#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "Gvgd0vrVtzW75Q1csdQz8bjW1"
consumer_secret = "gHINMru3BhCB4q6mXsqcKYtEu4znbwLZB2IJrsl1aV4YfgrQIo"
access_key = "149805011-DHUge40SiysWWQ1ZSkOQygADyDMoMpsC4y1hp5zb"
access_secret = "aH6huBgBoorlcLBj8nvsEUA2aQm3mi7znU7fuFSYGtPYs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

# uses the function to query a Twitter user. Try s = get_profile("CitronResearch")
s = get_profile("CitronResearch")
print "Name: " + s.name
print "Location: " + s.location
print "Description: " + s.description
print "Id: " + s.id_str

def get_tweets(screen_name):
    try:
        tweets = api.user_timeline(screen_name, count=3200)
    except:
        tweets = "broken"
    return tweets

list = []
t = get_tweets("CitronResearch")
for tweet in t:
    print tweet.retweet_count
    list.append(tweet.retweet_count)
    
for tweet in t:
    if tweet.retweet_count == max(list):
        mostpoptweet = tweet.text
print "The most popular tweet is " + mostpoptweet