#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
from twisted.internet import reactor

from pypolyback import log, routes, config

def start():
    """
    Starts server
    """
    
    #log
    if config.value['log']:
        log.start()
    else:
        #TODO: log.start() on sql
        pass

    #settings
    settings = {
        "debug": config.value['scope'] is not 'prod',
        "static_path": os.path.dirname(__file__)
    }
    
    if 'mail' in config.value:
        settings['email_settings'] = config.value['mail']

    application = routes.prepare()
    
    reactor.listenTCP(config.value['server']['port'], application)
    
    #start
    reactor.run()