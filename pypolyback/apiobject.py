#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pypolyback import config, log

class _ApiObject(object):
    """
    Api properties that will be avaliable on endpoints
    
    Properties:
        config: current config object
        debug: function to log message
        error: function to log error
        (will be added endpoint required util modules)
    """
    
    config = config.value
    debug = log.debug
    error = log.error

def mount():
    return _ApiObject()