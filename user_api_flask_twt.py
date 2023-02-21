
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
#from flask import request
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

@app.route('/<string:name>',methods = ['GET','POST'])
def get_user_details(name:str):
    #text = str(request.args.get('input'))
    userdata = sntwitter.TwitterProfileScraper(name).entity
    json_dump = jsonify(userdata)
    return json_dump

if '__name__'== '__main__':
    app.run()


