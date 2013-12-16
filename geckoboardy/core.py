from flask import jsonify


class Endpoint(object):
    # Requirements
    get = []
    post = []
    api_auth = False

    # Error handling
    _error = False

    # Request data
    data = {}

    # Response dict
    result = {}

    def __init__(self, *args, **kwargs):
        self.data['get'] = kwargs.pop('get')
        self.data['post'] = kwargs.pop('post')
        self.data['request'] = kwargs.pop('request')
        self.data['auth'] = kwargs.pop('auth')
        self.data['params'] = kwargs.pop('params')

        self.check_requeriments()

    def check_requeriments(self):
        # Check GET parameters
        for k in self.get:
            if k not in self.data['get']:
                self._error = True
                break

        # Check POST parameters
        for k in self.post:
            if k not in self.data['post']:
                self._error = True
                break

        # Check API Auth
        if self.api_auth and self.data['auth'] is None:
            self._error = True

    def summary(self):
        self.result = dict(item=[{"text": "Test"}])

    def response(self):
        if self._error:
            self.result = dict(error="Requeriments not met.")

        return jsonify(self.result)

    def call(self, method_name):
        try:
            method = getattr(self, method_name)
            if not self._error:
                method()
        except AttributeError:
            self.result['error'] = 'Method not found.'
