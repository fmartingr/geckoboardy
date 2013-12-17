from importlib import import_module
from flask import Flask, request
from geckoboardy import conf


# Flask app
app = Flask(__name__)
app.config.update(
    DEBUG=conf.DEBUG,
    SERVER_NAME=conf.SERVER_NAME
)


# Some debug info
print('Services loaded: {}'.format(", ".join(conf.SERVICES)))


# Main route
@app.route("/<string:service>/<string:method>/", defaults={'path': ''},
           methods=['GET', 'POST'])
@app.route("/<string:service>/<string:method>/<path:path>",
           methods=['GET', 'POST'])
def widget(service, method, path):
    """
    Unique URL handler
    @service: service module to load
    @method: method for that service class to call
    @path: optional path splitted by slashes for custom URL params
    """
    auth = request.authorization

    if service in conf.SERVICES:
        try:
            try:
                module = import_module(
                    'geckoboardy.services.{}'.format(service))
            except ImportError:
                module = import_module('local_services.{}'.format(service))
            endpoint = module.Service(
                auth=auth, get=request.args,
                post=request.form, request=request.json,
                params=path.split('/'))
            endpoint.call(method)
            return endpoint.response()
        except ImportError:
            return "Could not import service {}".format(service), 500
    else:
        # Service not allowed
        return "Service {} not allowed.".format(service), 403
