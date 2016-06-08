#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
from twisted.python import log

def start(where=sys.stdout):
    """
    Starts logging  
    
    Args:
        where: where to log (default=sys.stdout)
    """
    log.startLogging(where)
    
def debug(message):
    """
    Publish a message to the global log publisher.
    
    Args:
        message: the log message
    """
    log.msg(message)
    
def error(message, excpection=Exception):
    """
    Publish an error to the global log publisher.
    
    Args:
        message: the error message
        exception: the exception type (default=Exception)
    """
    log.err(exception, message)