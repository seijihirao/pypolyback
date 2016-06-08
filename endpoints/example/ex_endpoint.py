#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypolyback import async

utils = [
    'example_util'
]

@async
def get(req, api):
    """
    Execute `python2 app.py`
    E entre, pelo seu browser em `localhost:8888/example/ex_endpoint`
    Deverá abrir uma página escrita `sucesso!`
    
    Output:
        string
    """
    
    result = yield api.example_util.write(req)
    
    req.send(result)

def post(req, api):
    """
    Execute `python2 app.py`
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
    
    req.send({
        'message': api.example_util.write(req),
        'request': message
    })