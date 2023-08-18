#!/usr/bin/python3

import requests
import os
import json
import csv

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

#Create the URL for Twitter API request
def create_url(user_id,next_page_id,retweet,reply):
    tweet_fields = "tweet.fields=id,text,created_at"
    count_per_page = "max_results=100"
    
    if retweet is False and reply is False:
        exclude = "exclude=retweets,replies"
    elif retweet is True and reply is False:
        exclude = "exclude=replies"
    elif retweet is False and reply is True:
        exclude = "exclude=retweets"
    else:
        exclude = ""
    
    if next_page_id == "" or next_page_id == "none":
        pagination_token = ""
    else:
        pagination_token = f"pagination_token={next_page_id}"
    
    url = f"https://api.twitter.com/2/users/{user_id}/tweets?{tweet_fields}&{count_per_page}&{exclude}&{pagination_token}"
    
    return url

#Method required for Twitter API bearer token authentication.
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r

#Make a request to a Twitter API endpoint
def request_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    return response

#Remove not wanted data
def clean_data(data):
    for tweet in data:
        del tweet["edit_history_tweet_ids"]
        tweet["id"] = "https://twitter.com/anyuser/status/"+tweet["id"]
    return data
    

#Save Tweets to a CSV file
def data_to_csv(data):
    with open('tweets.csv', 'w') as f:
        keys = ['id', 'created_at', 'text']
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

#Main function to lookup and save Tweets based on specified options
def main(user_id,retweet,reply):
    next_page_id = "none"
    tweets=[]

    while next_page_id != "":
        url = create_url(user_id,next_page_id,retweet,reply)
        response = request_to_endpoint(url)
        
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print("JSON decoding error:", e)
        
        if "data" in data:
            tweets.extend(data["data"])
        if "next_token" in data["meta"]:
            next_page_id = data["meta"]["next_token"]
        else:
            next_page_id = ""
        
    clean_tweets = clean_data(tweets)
            
    data_to_csv(clean_tweets)


if __name__ == "__main__":
    main(user_id="",retweet=False,reply=False)
