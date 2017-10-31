try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
import urllib.parse
import json

url = 'https://api.paymentwall.com/api/brick/charge/39081509375792_test/refund'
data_request = {}
headers = {'X-ApiKey': 't_b741b48268a12e89f9b4a349958ff8'}

data_request = urllib.parse.urlencode(data_request)
data_request = urllib.parse.unquote_to_bytes(data_request)
re = urllib_request.Request(url, data=data_request, headers=headers)
r = urllib_request.urlopen(re)
print(r.getcode())
print(r.geturl())
print(r.info())

string = r.read().decode('utf-8')
json_obj = json.loads(string)
print(json_obj)

# token = response['token']