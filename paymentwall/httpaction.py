try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request
try:
    import urllib.parse as urllib_parse
except ImportError:
    import urllib as urllib_parse

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



