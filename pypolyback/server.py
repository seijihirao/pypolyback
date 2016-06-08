#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from twisted.internet import reactor

from pypolyback import log, routes, config

def start():
    """
    Starts server
    """
    
    #log
    if config.value['scope'] is not 'prod':
        log.start()
    else:
        #TODO: log.start() on sql
        pass
    
    #settings
    settings = {
        "debug": config.value['scope'] is not 'prod'
    }
    
    application = routes.prepare()
    
    reactor.listenTCP(config.value['server']['port'], application)
    
    #start
    reactor.run()