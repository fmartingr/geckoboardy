from geckoboardy.core import Endpoint, requires


class Service(Endpoint):
    # Globals
    get = ['ju3']
    post = []
    api_auth = True

    @requires(get=['username'])
    def get_test(self):
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
