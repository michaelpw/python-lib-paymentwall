try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request
try:
    import urllib.parse as urllib_parse
except ImportError:
    import urllib as urllib_parse
import json

class Httpaction():
    def __init__(self, baseurl, params, header):
        self.baseurl = baseurl
        self.params = params
        self.header = header

    def get_base_url(self):
        return self.baseurl

    def get_request_params(self):
        return self.params

    def get_header_params(self):
        return self.header

    def api_request(self):
        self.params = urllib_parse.unquote_to_bytes(urllib_parse.urlencode(self.params))
        request_object = urllib_request.Request(self.baseurl, data=self.params, headers=self.header)
        request = urllib_request.urlopen(request_object)
        return request

# url = 'https://api.paymentwall.com/api/brick/charge'
# data_request = {
#     'token': 'ot_3a0e6296186d669e8a7b24401ab00d9a',
#     'browser_ip': '111.22.33.44',
#     'browser_domain': 'https://paymentwall.com',
#     'amount': 1,
#     'currency':'USD',
#     'description':'Test Order',
#     'email':'test@gmail.com',
#     'customer[firstname]':'Test',
#     'customer[lastname]':'User'
# }
# data_header = {'X-ApiKey': 't_b741b48268a12e89f9b4a349958ff8'}
# test = Httpaction(url, data_request, data_header)
# response = test.api_request().read().decode('utf-8')
# response = json.loads(response)
# print(response)




