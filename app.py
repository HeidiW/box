# importing the requests library
import requests
import json

while True:
 # url to get the list of event entries
 url = "https://api.box.com/2.0/events"
 payload = {'stream_position': 'now'}

#headers with user authorization token to authenticate api calls
#developer keys will expire within 60 minutes. You will want to go to Box Developers > Configuration to generate your own key
headers = {'Authorization': 'Bearer DEVELOPER_KEY'}
# options request to event url to get list of events
r1 = requests.options(url, headers=headers)
events = r1.json()
#extract stream_url from the retured event entry
stream_url = events['entries'][0]['url']


print('real time url '+ stream_url)
print('long polling...')
# sending get request and saving the response as response object
# get request to stream endpoint
r = requests.get(stream_url, headers=headers)
# extracting data in json format
data = r.json()
print(data['message'])
print('long polling...')
print('reconnect')
