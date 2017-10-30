try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
import urllib.parse
import json

url = 'https://api.paymentwall.com/api/brick/token'
data_request = {
    'public_key': 't_5e62bbff32d16a2dfb0dff0c496be9',
    'card[number]':'4242424242424242',
    'card[exp_month]':'11',
    'card[exp_year]':'21',
    'card[cvv]':'123'
}
#headers = {'X-ApiKey': 'YOUR_PRIVATE_KEY'}

data_request = urllib.parse.urlencode(data_request)
data_request = urllib.parse.unquote_to_bytes(data_request)
re = urllib_request.Request(url, data=data_request)
r = urllib_request.urlopen(re)
print(r.getcode())
print(r.geturl())
print(r.info())

string = r.read().decode('utf-8')
json_obj = json.loads(string)
print(json_obj)

# token = response['token']