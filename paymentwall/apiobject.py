from paymentwall.httpaction import Httpaction
from paymentwall.base import Paymentwall
import json

class ApiObject(Paymentwall, Httpaction):
    API_BRICK_SUBPATH = 'brick'
    API_OBJECT_CHARGE = 'charge'
    API_OBJECT_SUBSCRIPTION = 'subscription'
    API_OBJECT_ONE_TIME_TOKEN = 'token'
    BRICK_ENDPOINTS = (API_OBJECT_CHARGE, API_OBJECT_SUBSCRIPTION, API_OBJECT_ONE_TIME_TOKEN)

    my_id = ''
    json_response = {}

    def __init__(self, id='', obj=''):
        self.my_id = id
        self.obj = obj

    def get_endpoint_name(self):
        if self.obj:
            return self.API_OBJECT_CHARGE if self.obj == 'charge' else self.obj == 'subscription'
        else:
            return ''

    def get_api_url(self):
        return self.BASE + '/' + self.API_BRICK_SUBPATH + '/' + self.get_endpoint_name()

    def get_api_header(self):
        return {'X-ApiKey': self.get_secret_key()} if not self.API_OBJECT_ONE_TIME_TOKEN else {}

    def build_query(self, params):
        query = ''
        for key, value in params.items():
            query = query + '&' + key + '=' + value
        return query

    def convert_response(self, resp):
        raw_response = resp.decode('utf-8')
        return json.loads(raw_response)

    def do_api_action(self, action='', params={}, method='POST'):
        action_url = self.get_api_url() + self.id + action
        http_action = Httpaction(action_url, params=params, header=self.get_api_header()) if method == 'POST' else Httpaction(action_url + self.build_query(params), params={}, header={})
        response = http_action.api_request().read()
        self.set_response(self.convert_response(response))

    def set_response(self, response):
        if response:
            self.json_response = response
            return
        else:
            return 'Empty response'

    def get_response(self):
        return self.json_response

    def get_public_data(self):
        response = self.get_response()
        result = {}
        if response['type'] and response['type'] == 'Error':
            result = {
                'success': 0,
                'error': {
                    'message': response['error'],
                    'code': response['code']
                }
            }
        elif response['secure']:
            result = {
                'success': 0,
                'secure': response['secure']
            }
        elif response['success']:
            result['success'] = 1
        else:
            result = {
                'success': 0,
                'error': {
                    'message': 'Internal error'
                }
            }
        return result

    def create(self, params):
        # print(self.get_api_url())
        # print(params)
        # print(self.get_api_header())
        print(self.get_api_url())
        http_action = Httpaction(self.get_api_url(), params, self.get_api_header())
        response = http_action.api_request().read()
        self.set_response(self.convert_response(response))