## v0.12.6
Minor fixes

## v0.12.5
Added static path, making it possible to read static files

## v0.12.4
Fixed default cors value on dev config when initializating project

## v0.12.3
Using argparse lib on commandline

## v0.12.2
Fixed pypolyback commandline...again

## v0.12.1
Fixed pypolyback commandline

# v0.12.0
Added `pypolyback init` command line to init project folders and files

Updated old `pypolyback` command line to `pypolyback start` or `pypolyback serve`  

# v0.11.0
Removed `server/disable_cors` from config

Added `server/cors` instead 

## v0.10.2
Added `vars` dictionary to `api` object 

# v0.10.0
Added `mail` to config

## v0.9.1
Fixed `Access-Control-Allow-Origin` for everyone. If not disabled on `config`.

# v0.9.0
Added `log` property to `config` file

## v0.8.2
Fixed long description on `pip`.

## v0.8.1
Fixed long description on `pip`. Also added an instruction to upload to `pip`.

# v0.8.0
Added support for http methods 
* put
* delete
* head
* options
* default

# v0.7.0
Added logs for loaded endpoints and utils.

## v0.6.1
Fixed bug when making multiple requests to same endpoint resulted on param being reseted 

# v0.6.0
Added `async` annotation

## v0.5.4 
Added long description to `pip`

## v0.5.3 
Fixed a bug where pypoly class was being called

## v0.5.2
Fixed a bug on lib name (`pypoly-back` -> `pypolyback`)

## v0.5.1
Removed bugged long description on pip

# v0.5.0
Created installable and added  to pip

# v0.4.0
Added special functions to utils
* init
* get
* post
* any

# v0.3.0
Added param and response functions to `req` endpoint parametter

Also, `return` now returns as a response

You can receive and pass `json` now

# v0.2.0
Added utils

# v0.1.0
Created project