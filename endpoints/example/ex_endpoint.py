#!/usr/bin/env python
# -*- coding: utf-8 -*-

utils = [
    'example_util'
]

def get(req, api):
    """
    Execute `python2 appp.py`
    E entre, pelo seu browser em `localhost:8888/example/ex_endpoint`
    Deverá abrir uma página escrita `sucesso!`
    
    Output:
        string
    """
    
    return api.example_util.write('sucesso!')

def post(req, api):
    """
    Execute `python2 appp.py`
    E faça uma requisição http post em `localhost:8888/example/ex_endpoint`
    passando o objeto documentado como entrada
    Deverá ser retornado `{"message": input.message, "status":"sucesso!"}`
    
    Input:
        message: string
        
    Output:
        message: string
        status: string
    """
    
    message = req.params['message']
    
    return api.example_util.write({
        'message': message,
        'status': 'sucessso!'
    })