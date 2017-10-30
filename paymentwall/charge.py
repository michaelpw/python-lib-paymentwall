from paymentwall.base import Paymentwall
from paymentwall.apiobject import ApiObject

class Charge(ApiObject, Paymentwall):
    def __init__(self, id=''):
        ApiObject.__init__(self, id=id, obj='charge')

    def get_id(self):
        return self.id

    def is_captured(self):
        return self.json_response['captured']

charge = Charge()
data_request = {
    'token': 'ot_402f05849fe82515418aed3dbc112769',
    'browser_ip': '111.22.33.44',
    'browser_domain': 'https://paymentwall.com',
    'amount': 1,
    'currency':'USD',
    'description':'Test Order',
    'email':'test@gmail.com',
    'customer[firstname]':'Test',
    'customer[lastname]':'User'
}
Paymentwall.set_secret_key('t_b741b48268a12e89f9b4a349958ff8')
charge.create(params=data_request)
print(charge.get_response())