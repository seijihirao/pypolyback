properties = {}

def init(api):
    api.message = api.config['test']

def post(req, api):
    req.message += 'post!'

def get(req, api):
    req.message += 'get!'

def any(req, api):
    req.message = api.message + ' in method '

def write(api):
     return api.message