import tweepy as tw

def where_are_we():

	with open("position.txt", 'r') as f:

		counter = int(f.read())

	return counter

def reset_counter():

	with open("position.txt", 'w') as f:

		f.write('0')

def update_position(counter, len_of_tweets):

	with open("position.txt", 'w') as f:

		f.write(str(int(counter % len_of_tweets)))

def get_tweet(counter):

	with open("tweets.txt", 'r') as f:

		tweets = f.readlines()

		
	return tweets[counter].rstrip('\n'), len(tweets)


def now_tweet(tweet):

	with open("api.keys", 'r') as f:

		keys = f.readlines()
	

	for i, key in enumerate(keys):
		keys[i] = key.rstrip('\n')
	

	auth = tw.OAuthHandler(keys[0], keys[1])
	auth.set_access_token(keys[2], keys[3])

	api = tw.API(auth)


	api.update_status(tweet)



counter = where_are_we()

tweet, n = get_tweet(counter)

now_tweet(tweet)

update_position(counter+1, n)


