#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import imp
import json
import cyclone.web
from twisted.internet.defer import inlineCallbacks as async

from pypolyback import log, apiobject

global_api = apiobject.mount()

class DynamicHandler(cyclone.web.RequestHandler):
    """
    Dummy cycloce Web Handler that will be used as a mold for endpoints 
    
    Properties:
        api: api properties that will be avaliable on endpoints, documented on `apiobject.py`
        pypoly_utils_get: list of `get` functions in the called util, they will be called before each endpoint `get` request
        pypoly_utils_post: list of `post` functions in the called util, they will be called before each endpoint `post` request
        pypoly_utils_any: list of `any` functions in the called util, they will be called before each endpoint request
    """
    
    def set_default_headers(self):
        """
        Set http header behaviour

        Access-Control-Allow-Origin: everyone
        """
        if not self.api.config['server']['disable_cors']:
            self.set_header('Access-Control-Allow-Origin', '*')

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
                for key in self.request.arguments:
                    if len(self.request.arguments[key]) is 1:
                        self._params[key] = self.request.arguments[key][0]
                    else:
                        self._params[key] = self.request.arguments[key]
                                
        return self._params
    
    def send(self, result):
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
        if self.pypoly_get_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_get:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_get(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
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
        if self.pypoly_post_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_post:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_post(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
    def pypoly_put(req, api, *args, **kwargs):
        """
        Function executed on http put that will be overriden by `put` function on your endpoint 
        
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
    def put(self, *args, **kwargs):
        """
        Function executed on http put
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        if self.pypoly_put_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_put:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_put(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
    def pypoly_delete(req, api, *args, **kwargs):
        """
        Function executed on http delete that will be overriden by `delete` function on your endpoint 
        
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
    def delete(self, *args, **kwargs):
        """
        Function executed on http delete
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        print self
        if self.pypoly_delete_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_delete:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_delete(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
    def pypoly_head(req, api, *args, **kwargs):
        """
        Function executed on http head that will be overriden by `head` function on your endpoint 
        
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
    def head(self, *args, **kwargs):
        """
        Function executed on http head
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        if self.pypoly_head_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_head:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_head(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
    def pypoly_options(req, api, *args, **kwargs):
        """
        Function executed on http options that will be overriden by `options` function on your endpoint 
        
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
    def options(self, *args, **kwargs):
        """
        Function executed on http options
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        if self.pypoly_options_implemented:
            for util_func in self.pypoly_utils_any:
                util_func(self, self.api, *args, **kwargs)
                
            for util_func in self.pypoly_utils_options:
                util_func(self, self.api, *args, **kwargs)
                
            yield self.pypoly_options(self.api, *args, **kwargs)
        else:
            yield self.default(*args, **kwargs)
    
    def pypoly_default(req, api, *args, **kwargs):
        """
        Function executed on http default that will be overriden by `default` function on your endpoint 
        
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
    def default(self, *args, **kwargs):
        """
        Function executed if a request does not match any implemented methods
        
        Args:
            *args: don't really know
            **kwargs: don't really know
        """
        for util_func in self.pypoly_utils_any:
            util_func(self, self.api, *args, **kwargs)
            
        for util_func in self.pypoly_utils_default:
            util_func(self, self.api, *args, **kwargs)
            
        yield self.pypoly_default(self.api, *args, **kwargs)



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
        
        log.debug('Loading endpoint: [' + log.bcolors.HEADER + file_path['url'] + log.bcolors.ENDC + ']')
        
        file_module = imp.load_source(file_path['url'].replace('/', '-'), file_path['file'])

        supported_methods = global_api.supported_methods

        handler_props = {
            'async': async,
            
            '_params': None,
            
            'api': global_api
        }

        ##
        # INITIALIZING METHOD PROPERTIES
        #
        for method in supported_methods:
            handler_props['pypoly_' + method + '_implemented'] = False
            handler_props['pypoly_utils_' + method] = []

        handler_props['pypoly_utils_any'] = []
        

        ##
        # ADDING METHOD FUNCTIONS
        #
        for method in supported_methods:
            if hasattr(file_module, method):
                handler_props['pypoly_' + method] = getattr(file_module, method)
                handler_props['pypoly_' + method + '_implemented'] = True
        
        ##
        # ADDING UTILS TO API PARAM
        #
        if hasattr(file_module, 'utils'):
            for util in file_module.utils:
                if not util in utils:
                    utils[util] = imp.load_source(util, os.path.join('utils', util + '.py'))
                    utils[util].async =  async
                setattr(handler_props['api'], util, utils[util])
                
                #calls util init function 
                if hasattr(utils[util], 'init'):
                    utils[util].init(global_api)
                
                #adds rest functionst
                for method in supported_methods:
                    if hasattr(utils[util], method):
                        handler_props['pypoly_utils_' + method] += [getattr(utils[util], method)]

                #adds 'any' function
                if hasattr(utils[util], 'any'):
                    handler_props['pypoly_utils_any'] += [utils[util].any]
        
        Handler = type(file_path['url'].replace('/', '').replace('.', ''), (DynamicHandler, ), handler_props)
        
        routes += [('/' + file_path['url'], Handler)]
        
        #Logging loaded endpoints
        log.debug('Endpoint Loaded: [' + log.bcolors.OKBLUE + file_path['url'] + log.bcolors.ENDC + ']')
    
    #Logging loades utils
    for root, subdirs, files in os.walk('./utils'):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                util = os.path.splitext(file)[0]
                if util in utils:
                    log.debug('Util Loaded: [' + log.bcolors.OKBLUE + util + log.bcolors.ENDC + ']')
                else:
                    log.debug('Util not Loaded: [' + log.bcolors.WARNING + util + log.bcolors.ENDC + ']')
    
    return cyclone.web.Application(routes)