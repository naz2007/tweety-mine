#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import csv

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

# uses the function to query a Twitter user. Try s = get_profile("dr_nazia")
s = get_profile("CitronResearch")
print "Name: " + s.name
print "id: " + s.id_str
print "Location: " + s.location
print "Description: " + s.description
def get_tweets(screen_name):
    alltweets = []
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=200)
        print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        print oldest
        print len(tweets)
        while len(tweets) > 0:
            tweets = api.user_timeline(screen_name, count=200, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1
            print "...%s tweets downloaded so far" % (len(alltweets))
    except:
        user_profile = "broken"
    return alltweets
# uses the function to query a Twitter user. Try s = get_profile("dr_nazia")
# profiles = ["cd_conrad", "justinbieber","rosiebarton","realDonaldTrump"]

# with open ('tweets.csv', 'wb') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["id","user","created_at","text"])
#     for profile in profiles:
#         t = get_tweets(profile)
#         for tweet in t:
#             writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
list1 = []
t = get_tweets("CitronResearch")
for tweet in t:
    list1.append(tweet.retweet_count)

for tweet in t:
    if tweet.retweet_count == max(list1):
        text1 = tweet.text

with open ('tweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweet in t:
        if "FTC" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
    t2 = get_tweets("Shopify")
    for tweet in t2:
        if "citron" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
print "most popular tweet of citron research is: \"" + text1 + " \" with a retweet count of " +str(max(list1))