import requests
import json

url = 'https://api.paymentwall.com/api/brick/token'
data_request = {
    'public_key': 'YOUR_PUBLIC_KEY',
    'card[number]':'4242424242424242',
    'card[exp_month]':'11',
    'card[exp_year]':'21',
    'card[cvv]':'123',
}
#headers = {'X-ApiKey': 'YOUR_PRIVATE_KEY'}

r = requests.post(url, data=data_request) # send post request
response = json.loads(r.text) # get response in json
print(response)