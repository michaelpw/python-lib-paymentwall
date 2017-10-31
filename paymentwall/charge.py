from paymentwall.apiobject import ApiObject

class Charge(ApiObject):
    def __init__(self, id=''):
        if id:
            ApiObject.__init__(self, id=id, obj='charge')
        else:
            ApiObject.__init__(self, obj='charge')

    def get_id(self):
        return self.id

    def is_test(self):
        return self.get_response()['test']

    def is_captured(self):
        return self.get_response()['captured']

    def is_successful(self):
        return self.object_response()

    def is_under_review(self):
        return self.get_response()['risk'] == 'pending'

    def is_refunded(self):
        return self.get_response()['refunded']

    def refund(self):
        return self.do_api_action(action='refund')

    def capture(self):
        return self.do_api_action(action='capture')

    def void(self):
        return self.do_api_action(action='void')

# charge = Charge()
# data_request = {
#     'token': 'ot_766453f684e8e6281e7fafaed17ff158',
#     'browser_ip': '111.22.33.44',
#     'browser_domain': 'https://paymentwall.com',
#     'amount': 1,
#     'currency':'USD',
#     'description':'Test Order',
#     'email':'test@gmail.com',
#     'customer[firstname]':'Test',
#     'customer[lastname]':'User'
# }
# Paymentwall.set_secret_key('t_b741b48268a12e89f9b4a349958ff8')
# charge.create(data_request)
# print(charge.get_response())
# print(charge.get_public_data())

# charge = Charge('13351509377912_test')
# charge.capture()
# print(charge.get_response())