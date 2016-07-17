#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pypolyback import config, log

class _ApiObject(object):
    """
    Api properties that will be avaliable on endpoints
    
    Properties:
        config: current config object
        supported_methods: supported http rest methods
        debug: function to log message
        error: function to log error
        (will be added endpoint required util modules)
    """
    
    config = config.value
   
    supported_methods = [
        'get', 
        'post',
        'put',
        'delete',
        'head',
        'options',
        'default'
    ]

    def debug(self, msg):
        log.debug(msg)
        
    def error(self, msg):
        log.error(msg)

def mount():
    return _ApiObject()