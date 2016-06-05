import os
import json

def _load(scope):
    """
    loads choosen config file
    
    Args:
        scope: config file, without `.json`
    """
    path = 'config/{}.json'.format(scope)
    if os.path.exists(path):
        with open(path, 'r') as config:
            obj = json.loads(config.read())
            obj['scope'] = scope
            return obj
            
    return False

def load():
    """
    loads config file (first try `local`, then `dev` and last `prod`)
    """
    for scope in ['local', 'dev', 'prod']:
        config = _load(scope)
        if config:
            return config
    
    raise EnvironmentError('No config file found')

#shortcut to current config
value = load()