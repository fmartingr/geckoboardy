from itertools import chain
from flask import jsonify


#
# DECORATORS
#
def requires(get=[], post=[], api_auth=False):
    """
    Set the service method post, get and auth requirements.
    """
    def decorator(method):
        def wrapper(cls, *args, **kwargs):
            for k in chain(get, cls.get):
                if k not in cls.data['get']:
                    cls._error = True
                    break

            # Check POST parameters
            for k in chain(post, cls.post):
                if k not in cls.data['post']:
                    cls._error = True
                    break

            # Check API Auth
            if (api_auth or cls.api_auth) and cls.data['auth'] is None:
                cls._error = True

            method(cls, *args, **kwargs)
        return wrapper
    return decorator


#
# Endpoint base class
#
class Endpoint(object):
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

    def response(self):
        if self._error:
            self.result = dict(error="Requeriments not met.")

        return jsonify(self.result), 500

    def call(self, method_name):
        try:
            method = getattr(self, method_name)
            if not self._error:
                method()
        except AttributeError:
            self.result['error'] = 'Method not found.'
