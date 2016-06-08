#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import imp
import json
import cyclone.web
from twisted.internet.defer import inlineCallbacks as async

from pypolyback import apiobject

global_api =  apiobject.mount()

class DynamicHandler(cyclone.web.RequestHandler):
    """
    Dummy cycloce Web Handler that will be used as a mold for endpoints 
    
    Properties:
        api: api properties that will be avaliable on endpoints, documented on `apiobject.py`
        pypoly_utils_get: list of `get` functions in the called util, they will be called before each endpoint `get` request
        pypoly_utils_post: list of `post` functions in the called util, they will be called before each endpoint `post` request
        pypoly_utils_any: list of `any` functions in the called util, they will be called before each endpoint request
    """
    
    def __init__(self):
        """
        Initialize properties.
        api with the mounted object
        pypoly_utils with an empty list each
        """
        self.pypoly_utils_get = []
        self.pypoly_utils_post = []
        self.pypoly_utils_any = []
        self.api = global_api
    
    def _cyclone_init(self, application, request, **kwargs):
        """
        __init__ passed to cyclone
        """
        super(DynamicHandler, self).__init__(application, request, **kwargs)
        self._params = None
        
        return self
    
    @property
    def params(self):
        """
        Gets argument in list of dicts

        The returned value is always unicode.
        
        Returns:
            value: parameter value. If the argument is not present, returns an empty list.
        """
        
        if self._params is None:
            try:
                self._params = json.loads(self.request.body)
            except:
                self._params = {}
                print self.request.arguments
                for key in self.request.arguments:
                    if len(self.request.arguments[key]) is 1:
                        self._params[key] = self.request.arguments[key][0]
                    else:
                        self._params[key] = self.request.arguments[key]
                                
        return self._params
    
    def respond(self, result):
        """
        Transform dicts in json and writes them using `cyclone.web.RequestHandler.write` method
        """
        if isinstance(result, dict):
            self.write(json.dumps(result, separators=(',', ':')))
        elif result:
            self.write(result)
    
    def pypoly_get(req, api, *args, **kwargs):
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
        for util_func in self.pypoly_utils_any:
            util_func(self, self.api, *args, **kwargs)
            
        for util_func in self.pypoly_utils_get:
            util_func(self, self.api, *args, **kwargs)
            
        result = yield self.pypoly_get(self, self.api, *args, **kwargs)
        self.respond(result)
    
    def pypoly_post(req, api, *args, **kwargs):
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
        for util_func in self.pypoly_utils_any:
            util_func(self, self.api, *args, **kwargs)
            
        for util_func in self.pypoly_utils_post:
            util_func(self, self.api, *args, **kwargs)
            
        result = yield self.pypoly_post(self, self.api, *args, **kwargs)
        self.respond(result)

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
            
            #calls util init function 
            if hasattr(utils[util], 'init'):
                utils[util].init(global_api)
                
            #add post function
            if hasattr(utils[util], 'post'):
                handler.pypoly_utils_post += [utils[util].post]
                
            #add get function
            if hasattr(utils[util], 'get'):
                handler.pypoly_utils_get += [utils[util].get]
                
            #add any function
            if hasattr(utils[util], 'any'):
                handler.pypoly_utils_any += [utils[util].any]
            
        #add post function
        if hasattr(file_module, 'post'):
            handler.pypoly_post = file_module.post
            
        #add get function
        if hasattr(file_module, 'get'):
            handler.pypoly_get = file_module.get
            
        routes += [('/' + file_path['url'], lambda *args, **kwargs: handler._cyclone_init(*args, **kwargs))]
    
    return cyclone.web.Application(routes)