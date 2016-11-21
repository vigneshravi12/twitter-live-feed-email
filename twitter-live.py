from twython import Twython # pip install twython
import json

ACCESS_KEY = '88262286-Vus6KBnXnGy4CsDc3pyGss1vq6urkGnffZS1P2TyX'
ACCESS_SECRET = 'pfIM9sEJgFWJpwKdGI8BuE8ea022xIGQITAPTjBuB4oel'
CONSUMER_KEY = 'u45n3htjGHqeOavltLHGad6Xl'
CONSUMER_SECRET = 'wOYb06s7AR4cLVJFpoCilicgMUBKXEmENoF0gaiE88SJp9qRo6'
count = 15
cssMediaString = '''@media screen and (-webkit-min-device-pixel-ratio: 0) {

.tweet .copy:before {
  white-space: pre-wrap;
}'''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
# user_timeline = twitter.get_user_timeline(screen_name="tedc16",
# count=5)
# request(endpoint, method='GET', params=None, version='1.1')
user_timeline = twitter.request("https://api.twitter.com/1.1/search/tweets.json?q=mic&lang=en&count="+str(count), method='GET',version='1.1')

statuses = user_timeline['statuses']
# print statuses
with open('data.json', 'w') as outfile:
    json.dump(statuses, outfile)
with open('tweets.css','w') as cssFile:
	cssFile.write(cssMediaString)
	tweetsCount = 1
	for tweet in statuses:
	    # print tweet['text']
	    cssFile.write('''
	    	#tweet-'''+str(tweetsCount)+''' .avatar {
	    		background: url("'''+tweet['user']['profile_image_url'].encode('utf-8')+'''");
			}
			''')
	    cssFile.write('''\
			#tweet-'''+str(tweetsCount)+''' .name::before {
				content: "'''+tweet['user']['name'].encode('utf-8')+'''";
			}
			''')
	    cssFile.write('''
			#tweet-'''+str(tweetsCount)+''' .handle::after {
				content: "'''+tweet['user']['screen_name'].encode('utf-8')+'''";
			}
			''')
	    cssFile.write('''
	    	#tweet-'''+str(tweetsCount)+''' .copy::before {
	    		content: "'''+tweet['text'].encode('utf-8')+'''";
	    	}
	    	''')
	    cssFile.write('''
	    	#tweet-'''+str(tweetsCount)+''' .timestamp::after {
	    		content: "'''+tweet['user']['created_at'].encode('utf-8')+'''";
	    	}
	    	''')
	    tweetsCount+=1
	for i in range(tweetsCount,16):
		cssFile.write('''\
			#tweet-'''+str(i)+''' {
				display: none;
			}
			''')
   #  for i in range(tweetsCount,15):
   #  	cssFile.write('''
   #  		#tweet-'''+str(i)+'''{
   #  			display: none;
   #  		}
			# ''')
	cssFile.close()
