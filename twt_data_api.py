
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
#from flask import request
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)


def get_data(query):
    data = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        # Number of posts or tweets you want to scrape
        # comment out if and break statement if you want to get all the tweets
        if i >= 50:
            break
        print(i, tweet, tweet.date, tweet.user.username, tweet.content)
        tmp_data = {"index_count":i,"tweet_link":tweet.url,
                    "username":tweet.user.username,"tweet_text":tweet.content,"date":tweet.date.date(),
                    "time":tweet.date.time(),"likes":tweet.likeCount}
        twitter_data = tmp_data
        data.append(twitter_data)
        final_data = {"data":data}
    return final_data

@app.route('/<string:name>',methods = ['GET','POST'])
def get_user_details(name:str):
    twitter_data=get_data(name)
    return jsonify(twitter_data)

if '__name__'== '__main__':
    app.run()
