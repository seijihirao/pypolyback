#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import imp
import json
import cyclone.web
from twisted.internet.defer import inlineCallbacks as async

from api import apiobject

class DynamicHandler(cyclone.web.RequestHandler):
    """
    Dummy cycloce Web Handler that will be used as a mold for endpoints 
    """
    
    def __init__(self):
        """
        Mounts api object
        """
        self.api = apiobject.mount()
    
    def _cyclone_init(self, application, request, **kwargs):
        """
        __init__ passed to cyclone
        """
        super(DynamicHandler, self).__init__(application, request, **kwargs)
        return self
    
    def response(self, result):
        """
        Transform dicts in json and writes them using `cyclone.web.RequestHandler.write` method
        """
        if isinstance(result, dict):
            self.write(json.dumps(result, separators=(',', ':')))
        elif result:
            self.write(result)
    
    def endpoint_get(req, api, *args, **kwargs):
        """
        Function executed on http get that will be overriden by `get` function on your endpoint 
        
        Args:
            req: self, cyclone.web.RequestHandler
            api: object mounted on `apiobject.py` and incremented with util modules
            *args: don't really know
            **kwargs: don't really know
        
        Raises:
            NotImplemented: if endpoint get is called and not implemented
        """
        raise NotImplemented
        
    @async
    def get(self, *args, **kwargs):
        """
        Function executed on http get
        
        Args:
            *args: don't really know
            **kwargs: don't really know 
        """
        
        result = yield self.endpoint_get(self, self.api, *args, **kwargs)
        self.response(result)
    
    def endpoint_post(req, api, *args, **kwargs):
        """
        Function executed on http post that will be overriden by `post` function on your endpoint 
        
        Args:
            req: self, cyclone.web.RequestHandler
            api: object mounted on `apiobject.py` and incremented with util modules
            *args: don't really know
            **kwargs: don't really know
        
        Raises:
            NotImplemented: if endpoint post is called and not implemented
        """
        raise NotImplemented
        
    @async
    def post(self, *args, **kwargs):
        """
        Function executed on http post
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        result = yield self.endpoint_post(self, self.api, *args, **kwargs)
        self.response(result)

def prepare():
    """
    Mount routers and add them to cyclone application 
    
    Returns:
        application (cyclone.web.Application): cyclone application with endpoint routers mounted 
    """
    
    file_paths = []
    
    #read all endpoint files
    for root, subdirs, files in os.walk('./endpoints'):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                file_paths += [{
                    'url': os.path.splitext(os.path.relpath(os.path.join(root, file), 'endpoints/'))[0],
                    'file': os.path.join(root, file)
                }]
    
    routes = []
    
    utils = {}
    
    #populate routes
    for file_path in file_paths:
        file_module = imp.load_source(file_path['url'].replace('/', '-'), file_path['file'])
        handler = DynamicHandler()
        
        #add utils to api param
        for util in file_module.utils:
            if not util in utils:
                utils[util] = imp.load_source(util, os.path.join('utils', util + '.py'))
            setattr(handler.api, util, utils[util])
            
        #add post function
        if hasattr(file_module, 'post'):
            handler.endpoint_post = file_module.post
            
        #add get function
        if hasattr(file_module, 'get'):
            handler.endpoint_get = file_module.get
            
        routes += [('/' + file_path['url'], lambda *args, **kwargs: handler._cyclone_init(*args, **kwargs))]
    
    return cyclone.web.Application(routes)