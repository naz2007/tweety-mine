#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "Gvgd0vrVtzW75Q1csdQz8bjW1"
consumer_secret = "gHINMru3BhCB4q6mXsqcKYtEu4znbwLZB2IJrsl1aV4YfgrQIo"
access_key = "149805011-DHUge40SiysWWQ1ZSkOQygADyDMoMpsC4y1hp5zb"
access_secret = "aH6huBgBoorlcLBj8nvsEUA2aQm3mi7znU7fuFSYGtPYs"

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

# uses the function to query a Twitter user. Try s = get_profile("dr_nazia")
s = get_profile("dr_nazia")
print "Name: " + s.name
print "Location: " + s.location
print "Description: " + s.description
print "id: " + s.id_str