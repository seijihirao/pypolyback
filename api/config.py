import os
import json

def load(scope='default'):
    """
    loads choosen config file
    if scope is not define loads default (first try `local`, then `dev` and last `prod`)
    
    Args:
        scope: config file, without `.json`
    """
    
    if scope is 'default':
        for scope in ['local', 'dev', 'prod']:
            path = 'config/{}.json'.format(scope)
            if os.path.exists(path):
                config = load(scope)
                if config:
                    return config
                    
    else:
        path = 'config/{}.json'.format(scope)
        if os.path.exists(path):
            with open(path, 'r') as config:
                obj = json.loads(config.read())
                obj['scope'] = scope
                return obj
    raise EnvironmentError('No config file found')

#shortcut to current config
value = load()