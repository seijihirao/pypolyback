#!/usr/bin/env python
# -*- coding: utf-8 -*-

properties = {}

def init(api):
    api.message = api.config['test']
    api.debug('App started')

def get(req, api):
    req.message += 'get!'
    api.debug('Get request')
    
def post(req, api):
    req.message += 'post!'
    api.debug('Post request')

def any(req, api):
    req.message = api.message + ' in method '
    api.debug('Any request')

def write(req):
     return req.message