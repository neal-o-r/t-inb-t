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


counter = where_are_we()

tweet, n = get_tweet(counter)

print(tweet)

update_position(counter+1, n+1)


