import tweepy

# Set up the Twitter API client
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

# Retrieve tweets and their replies
tweet = api.get_status(id='TWEET_ID')
replies = api.search(q='to:' + tweet.user.screen_name, since_id=tweet.id, tweet_mode='extended')
