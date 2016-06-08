# PYPOLY BACK - v1.1
Bem vindo ao Pypoly Back! A framework usada no backend do site da Discipuluz!

## Linguagem
[Python 2.7](https://docs.python.org/2/tutorial/index.html)

## Bibliotecas
* [twisted](https://twistedmatrix.com/trac/) - Ferramenta de eventos de redes (Low Level)
* [tornado](http://www.tornadoweb.org/en/stable/) - Framework de apps web (High Level)
* [cyclone](http://cyclone.io/documentation/) - Implementação do Tornado como um protocolo do Twisted
* [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html) - Driver de MySQL

## Instalação
1. Instale o python 2.7
    * Windows - [Link](https://www.python.org/download/releases/2.7/)
    * Ubuntu - `sudo apt-get install python2`
    * Fedora - `sudo yum install python2`
    * Arch - `sudo pacman -S python2`
2. Instale o PIP - gerenciador de bibliotcas do python
    * Windows - [Link](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
    * Ubuntu - `sudo apt-get install pip2`
    * Fedora - `sudo yum install pip2`
    * Arch - `sudo pacman -S pip2`
3. Instale as bibliotecas usando o PIP
    * `pip install twisted`
    * `pip install tornado`
    * `pip install cyclone`
    
## Utilização

### Pastas
    /api - arquivos internos da api (Essa pasta só existirá se você não importou a biblioteca `pypoly-back` pelo pip)
    /config - arquivos json de configuração
    /endpoints - endpoints do backend
    /utils - arquivos de scripts para auxílio
    app.py - executável do servidor

### API
Aqui estão contidas os arquivos da api, que gerenciam todo o funcionamento por trás dos endpoints

### CONFIG
Aqui estão os arquivos com variáveis de configuração usados no aplicativo.
Eles serão disponibilizados para o endpoint por meio do parâmetro `api.config`

Estão contidos 2 arquivos:
* `prod.json` - arquivo de configuração do site oficial
* `dev.json` - arquivo de configuração usado no desenvolvimento

E é recomendado que seja adicionado um outro:
* `local.json` - arquivo local de configuração

### ENDPOINTS
Esta será a pasta principal de desenvolvimento.

Todo arquivo adicionado aqui já é automaticamente um endpoint

Por exemplo, o arquivo `endpoints/test/helloworld.py` gerará um endpoint `/test/helloworld`

O código do arquivo endpoint será:
```python

utils = [
    '[util1]'
    '[util2]'
]

def [method](req, api):
    [process]
``` 

Onde `[method]` é o tipo de requisição, podendo ser:
* post
* get
* put
* patch
* delete

`[process]` é o que você deseja que o endpoint faça

`[util1]` e `[util2]` são os nomes dos arquivos (sem o `.json`) dos scripts feitos na pasta *utils*

`req` é o request do cyclone, com as propriedades a mais:
* params - argumentos recebidos pela requisição, dicionário onde as chaves são os nomes do argumentos
* respond - função para retornar um dicionário na requisição

> A documentação completa do `req` está contida no site http://cyclone.io/documentation/web.html

`api` é o objeto que contém as funciionalidades da api, como:
* config - dicionário da config usada no escopo atual
* debug - função para logar uma mensagem
* error - função para logar um erro

> A documentação completa do `api` não existe :D

### UTILS

Arquivos de python com código reutilizável, para serem usados em múltiplos endpoints.

Ele será um código comum, mas com alguns métodos especiais, sendo esses:

init(api)

    A função que será executada no início da compilação.
    Ou seja, apenas uma vez, que será quando o programa for executado.
    
`[method]`(req, api) - Sendo `[method]` o tipo de requisição
    
    A função que será executada antes que qualquer requisição ao método escolhido do endpoint.
    Note que qualquer resultado deve ser retornado ou guardado na variável `req`, por serem as únicas variáveis locais da requisição.
    
any(req, api)
    
    A função que será executada antes todas as requisições ao endpoint.
    Observação: esse método será executado antes dos de método específico.


### APP.py

Executável do servidor!

Abra um terminal e execute `python2 app.py`

Então abra seu navegador ou uma requisição http e entre em `localhost:[porta]/[página]`

Onde `[porta]` é a porta no seu arquivo de configuração (`8888` se nada foi mudado)

E `[página]` é a url do seu arquivo, como explicado na sessão #endpoint

## EXEMPLO

Para tentar ter uma pequena sensação de que as coisas estão funcionando dê uma olhada no arquivo `endpoints/example/ex_endpoint.py` 

Ele deve estar assim:
```python
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
``` 

Agora siga as instruções para testar e ver como funciona o endpoint.

## AGRADECIMENTOS

https://youtu.be/oAhvQoLpvsM

## OBSERVAÇÃO

Tanto a framework quanto essa página estão ainda em fase de desenvolvimento e, por tanto, sujeitos a mudança.