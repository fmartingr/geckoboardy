from geckoboardy.core import Endpoint, requires


class Service(Endpoint):

    @requires(get=['username'])
    def get_test(self):
        print('le')
        self.result['text'] = 'Success!'

    @requires(post=['username'])
    def post_test(self):
        self.result['text'] = 'Success!'

    @requires(api_auth=True)
    def auth_test(self):
        self.result['text'] = 'Success!'

    @requires(api_auth=True, get=['foo'], post=['bar'])
    def all_test(self):
        self.result['text'] = 'Success!'
