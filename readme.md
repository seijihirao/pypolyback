# PYPOLY BACK
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
    * `pip install MySQL-python`
    
## Utilização

### Pastas
    /api - arquivos internos da api
    /config - arquivos json de configuração
    /endpoints - endpoints do backend
    /support - arquivos de scripts para auxílio
    app.py - executável do servidor

### API
Aqui estão contidas os arquivos da api, que gerenciam todo o funcionamento por trás dos endpoints

### CONFIG
Aqui estão os arquivos com variáveis de configuração usados no aplicativo.

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
class Main(cyclone.web.RequestHandler):
    def [method](self):
        [process]
``` 
Onde `[method]` é o tipo de requisição, podendo ser:
* post
* get
* put
* patch
* delete

E `[process]` é o que você deseja que o endpoint faça

Lembrando de importar as bibliotecas necessárias.

> A documentação completa está contida no site http://cyclone.io/documentation/

### SUPPORT (Nome sujeito a mudança)

Arquivos de python com código reutilizável, para serem usados em múltiplos endpoints.

### APP.py

Executável do servidor!

Abra um terminal e execute `python2 app.py`

Então abra seu navegador ou uma requisição http e entre em localhost:`[porta]`/`[página]`

Onde `[porta]` é a porta no seu arquivo de configuração (`8888` se nada foi mudado)

E `[página]` é a url do seu arquivo, como explicado na sessão #endpoint

## EXEMPLO

Para tentar ter uma pequena sensação de que as coisas estão funcionando crie uma pasta `test` na pasta `endpoint`, depois um arquivo `helloworld.py` na pasta `test`

Coloque no arquivo:
```python
import cyclone.web

class Main(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        
``` 

Agora abra seu navegador na página `localhost:8888/test/helloworld`

## AGRADECIMENTOS

https://youtu.be/oAhvQoLpvsM

## OBSERVAÇÃO

Tanto a framework quanto essa página estão ainda em fase de desenvolvimento e, por tanto, sujeitos a mudança.