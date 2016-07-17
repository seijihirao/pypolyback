properties = {}

def init(api):
    api.message = api.config['test']

def get(req, api):
    req.message += 'get!'
    
def post(req, api):
    req.message += 'post!'

def any(req, api):
    req.message = api.message + ' in method '

def write(req):
     return req.message