#!/usr/bin/env python
# coding: utf-8

# In[3]:


import configparser
import tweepy

# For reading Authantication
config = configparser.ConfigParser()
config.read('C://Users/NANDIT/twitter_config.ini')

# Helper function for printing the tweets scraped using specified #hashtags
def printtweetdata(n, ith_tweet):
    divide_str = "_*"*35
    print(f"Tweet {n}:")
    print(f"Username -- {ith_tweet[0]}")
    print(f"Description -- {ith_tweet[1]}")
    print(f"Location -- {ith_tweet[2]}")
    print(f"Following Count -- {ith_tweet[3]}")
    print(f"Follower Count -- {ith_tweet[4]}")
    print(f"Tweet Text -- {ith_tweet[5]}")
    print(f"Hashtags Used -- {ith_tweet[6]}")
    print(f'\n\t\t\t{divide_str}\n')

# Function for scraping the tweets using specified tweets 
def hashtag_scrape():
    words = input("Enter Twitter HashTag to search for start with '#' -- ")
    date_since = input("Enter Date since The Tweets are required in (yyyy-mm--dd) -- ")
    numtweet = int(input("Enter the number of tweets you want to scrape -- "))
    tweets = tweepy.Cursor(api.search, q=words, lang="en",
                           since=date_since, tweet_mode='extended').items(numtweet)
    list_tweets = [tweet for tweet in tweets]
    i = 1  
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        hashtags = tweet.entities['hashtags']
        
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
          
        ith_tweet = [username, description, location, following,
                     followers, text, hashtext]
          
        printtweetdata(i, ith_tweet)
        i = i+1
    print('Scraping has completed!')    

# Function that will scrape the user details using specified user-id
def get_user_info():
    user_id = input('Enter the user id you want to scrap -- ')
    try:        
        user = api.get_user(user_id)
        print(f'User-id -- {user.screen_name}')
        print(f'Name -- {user.name}')
        print(f'Location -- {user.location if user.location else "Not Specified"}')
        print(f'Number of Followers -- {user.followers_count}')
        print(f'Number of Followings -- {user.friends_count}')
        print(f'Description -- {"No Description" if len(user.description) == 0 else user.description}')
        print(f'Image URL -- {user.profile_image_url}')
        print(f'Is profile protected -- {"Yes" if user.protected else "No"}')
    except:
        print('This user id does not exist')
  
  
if __name__ == '__main__':
    consumer_key = config['twitter.com']['consumer_key']
    consumer_secret = config['twitter.com']['consumer_secret']
    access_key = config['twitter.com']['access_key']
    access_secret = config['twitter.com']['access_secret']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print("Welcome to Twitter-Bot made by Nandit Shah for scrapping the user data and tweets using #Hashtags")
    print("1. Select this option for scraping the tweets from using #Hashtags")
    print("2. Select this option for scraping user details using User-ID")
    print("3. Select this option to get exit of this Twitter-Bot")
    while True:
        option = input('Enter the option you want to select between (1-3) -- ')
        while option not in ['1','2','3']:
            option = input('Invalid Selection!!! Please select between (1-3) -- ')
        option = int(option)
        if option == 1:
            hashtag_scrape()
            continue
        elif option == 2:
            get_user_info()
            continue
        else:
            print('Thank you for using this Twitter-Bot hope you liked it')
            break

