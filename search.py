import tweepy
import Twitter_api_test


client = tweepy.Client(bearer_token=Twitter_api_test.BEARER_TOKEN)

query = "taylor -is retweet"

response = client.search_recent_tweets(query=query, max_results=10)

response2 = client.search_recent_tweets(query=query, max_results=10, expansions=["geo.place_id"])

print(response2)

print(response)

for tweet in response.data:
    # if places[tweet.geo["place_id"]]:
    #     place = places[tweet.geo["place_id"]]
    print(tweet.id)
    # print(place.full_name)

file_name = "tweets.txt"
query2 = "investments -is:retweet"
filehandler = open('tweets.txt','w')
with open(file_name, "a+") as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query2, max_results=10).flatten(limit=100):
        # print(tweet.id)
        filehandler.write("%\n" %tweet.id)

users = client.get_users_tweets(id=Twitter_api_test.USER_ID, tweet_field=["lang"])
for user in users:
        print(user)