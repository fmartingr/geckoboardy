geckoboardy
===========

Geckoboardy helps you, dear developer, to create simple API endpoints for your
[geckoboard](http://www.geckoboard.com/) custom widgets.


License
=======

See LICENSE file.


Services
========

```
# local_services/<service name>.py
# or geckoboardy/services/<service name>.py if pull requesting
from geckoboardy.core import Endpoint, requires


# Class must be named Service
class Service(Endpoint):
    # Global service requiremets go in class definition
    get = ['username']
    post = []
    api_auth = False


    @requires(get=['server'])
    def api_method(self):
        # ...
        self.result['...'] = 'Result'

    @requires(api_auth=True)
    def api_method2(self):
        # ...
        self.result['...']  = 'Result 2'
```


Config
======

```
# File: config.py

# Default: True
DEBUG = False

# Default: 127.0.0.1:5000
SERVER_NAME = '127.0.0.1:1234' 

# Default: []
# Must be modules either under geckoboardy.services or local_services packages.
SERVICES = ['services', 'to', 'enable']
```

Server
======

Start the server with `geckoboardy_server`
