#!/usr/bin/env python
# -*- coding: utf-8 -*-

utils = [
    'example_util'
]

def get(req, api):
    """
    Execute `python2 appp.py`
    E entre, pelo seu browser em `localhost:8888/example_endpoint`
    Deverá abrir uma página escrita `{"response":"sucesso!"}`
    """
    
    return api.example_util.write()

def post(req, api):
    """
    Execute `python2 appp.py`
    E faça uma requisição http post em `localhost:8888/example_endpoint`
    Deverá ser retornado `{"response":"sucesso!"}`
    """
    
    return api.example_util.write()