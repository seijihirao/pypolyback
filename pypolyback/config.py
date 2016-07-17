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

                #Default Values

                fill_default_value(obj, 'log', False)

                fill_default_value(obj, 'server', {})    
                fill_default_value(obj['server'], 'port', 8888)
                fill_default_value(obj['server'], 'disable_cors', False)

                return obj
    raise EnvironmentError('No config file found')

def fill_default_value(obj, key, default):
    if key not in obj:
        obj[key] = default

#shortcut to current config
value = load()