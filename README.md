# PYPOLY BACK - v0.12
Wellcome to Pypoly Back! A simple backend restful framework!

## LANGUAGE
[Python 2.7](https://docs.python.org/2/tutorial/index.html)

## LIBRARIES
* [twisted](https://twistedmatrix.com/trac/) - Web event-handling Framework (Low Level)
* [cyclone](http://cyclone.io/documentation/) - Http framework (High Level)

---

## INSTALATION
1. Install python 2.7
    * Windows - [Link](https://www.python.org/download/releases/2.7/)
    * Ubuntu - `sudo apt-get install python2`
    * Fedora - `sudo yum install python2`
    * Arch - `sudo pacman -S python2`
2. Install PIP - Python libraries manager
    * Windows - [Link](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
    * Ubuntu - `sudo apt-get install pip2`
    * Fedora - `sudo yum install pip2`
    * Arch - `sudo pacman -S pip2`
3. Install this framework using PIP
    * `pip2 install pypolyback`
    
---


## INITIALIZATING PROJECT

```
$ pypolyback --init
```

---

## USING

### DIRECTORIES
    /pypolyback (*) - api internal files
    /config - json configuration files
    /endpoints - backend endpoints
    /utils - helper script files
    
>Note (*): The dir pypolyback will only exists if you didn't install `pypolyback`'s library from pip  

### API
Here is present all api files that work behind the endpoints

### CONFIG
Here are the configuration files used in the app.
They will be send to the endpoint via param `api.config`

There are 3 special filenames:
* `prod.json` - The oficial configuration file 
* `dev.json` - The development configuration file
* `local.json` - The local configuration file (ignore in git)

>Note: They really work as following: the api tries to load `local.json`, then `dev.json`, then `prod.json`. So in the oficial release you will only have `prod.json`

The current config special properties are the following:
```json
{
    "log": bool, //optional. default=False
    "server": {
        "port": int, //optional. default=8888
        "cors": string or False //optional. default=False
    },
    "mail": {
        "host": string,
        "port": int, //optional. default=25 or 587 for TLS 
        "tls": bool, //optional. default=False
        "username?": string, //optional. no default
        "password?": string //optional. no default
    }
}
```

### ENDPOINTS
This will be your main dev dir

All files added here will be an endpoint automatically

i.e.: the file `endpoints/test/helloworld.py` will generate an endpoint `/test/helloworld`

The file's code will be the following:
```python

utils = [
    '[util1]',
    '[util2]'
]
[@async]
def [method](req, api):
    [process]
``` 

Where `[method]` is the http request type:
* post
* get
* put
* delete
* head
* options
* default - executed when a request is made for any of the above, but it is not implemented 

`[process]` is what you wan the endpoint to do (your code) 

`[util1]` and `[util2]` are the *utils* scripts (without `.py`)

`req` is *cyclone*'s request, with these properties included:
* params - arguments received from request, an object (primitive, list or dictionary)
* send - function to respond the request with an object

> `req`'s complete documentatios in present on cyclone's site http://cyclone.io/documentation/web.html

`api` is the object that contains all api functionalities:
* config - Configuration dictionary used in the actual scope
* debug - function to log messages
* error - function to log errors

`[@async]` is an optional annotation, that makes this method asynchronous.

Note: if async is used you will need to import  it (`from pypolyback import async`)

> `async` complete doc is the same as twisted's `inlineCallback` https://twistedmatrix.com/documents/current/api/twisted.internet.defer.html#inlineCallbacks

### UTILS

Python files with reusable code, to be called on endpoints.

It will be a normal cod, but with some special funcions:

init(api)

    The function that will be executed on server startup
    Only one time.
    
`[method]`(req, api) - `[method]` being the type of http request
    
    The function that will be called before every request to the function with the same name on the endpoint.
    Any result should be stored on the variable `req`, because it is the only local variable on the request.
    
any(req, api)
    
    The function that will be executed before any request.
    Note: thids function will be executed before the later.


### APP.py

>This file is not needed if you installed from pip

An executable to start your server

## EXAMPLE

To have a feeling of how things are working take a look at the file `endpoints/example/ex_endpoint.py`

It should be like this:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypolyback import async

utils = [
    'example_util'
]

@async  #método asíncrono
def get(req, api):
    """
    Start the server
    Then go, from your browser, in `localhost:8888/example/ex_endpoint`
    There shoud open a page with the content `Success in method get!`
    
    Output:
        string
    """
    
    result = yield api.example_util.write(req) #coletando dados de forma asíncrona
    
    req.send(result) #retornando os dados

def post(req, api):
    """
    Start the server
    Then make a post http request to `localhost:8888/example/ex_endpoint`
    Sending the documented object as input 
    It should be returned `{"message": input.message, "status":"Sucess in method post!"}`
    
    Input:
        message: string
        
    Output:
        message: string
        request: string
    """
    
    message = req.params['message'] #coletando dados da requisição
    
    #retornando os dados
    req.send({
        'message': api.example_util.write(req),
        'request': message
    })
``` 

Now follow instructions to test it and see how the endpoint works

---

### STARTING THE SERVER

There are 2 ways to start the server

1. Execute `pypolyback --start` from terminal on your root project folder (Recomended)

2. Call the method `start()` from module `pypolyback.server` (Only recomended if you need to do something before starting the server)

---

## OBSERVATION

Both the framework and this page are in development, so, subjected to changes.