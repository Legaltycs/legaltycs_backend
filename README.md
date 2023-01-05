# Proyecto legaltycs backend

<!--toc:start-->
- [Proyecto legaltycs backend](#proyecto-legaltycs-backend)
  - [Descripción](#descripción)
  - [Endpoints](#endpoints)
    - [Login user [ /api/login ]](#login-user-apilogin)
    - [Register user [ /api/register ]](#register-user-apiregister)
    - [Test authenticate route [ /api/test ]](#test-authenticate-route-apitest)
  - [Ejecución en entorno de desarrollo :rocket:](#ejecución-en-entorno-de-desarrollo-rocket)
<!--toc:end-->

## Descripción

## Endpoints

### Login user [ /api/login ]
- Body
```
{
    "username": "",
    "password": ""
}
```
### Register user [ /api/register ]
- Body
```
{
    "username": "",
    "password": "",
    "lastname": "",
    "name": ""
}
```
### Test authenticate route [ /api/test ]
Proporcione un Bearer Token

Repuesta sin token
```
{
    "menssage": "You do not have access without a valid token"
}
```
Repuesta con token
```
{
    "mensaje": "Entre"
}
```


## Ejecución en entorno de desarrollo :rocket:

- Ingrese a la carpeta del proyecto donde se encuentre el archivo main y abra un terminal

- Ejecutar los siguientes comandos en orden

```
$ pip install virtualenv
$ python -m venv .venv
$ .venv\Scripts\activate
$ pip install -r requirements.txt 

```
- Para desactivar el entorno virtual tiene que ejecutar el comando

```
$ deactivate

```
- Cree un archivo .env an la carpeta raiz del proyecto con los siguientes atributos

```
SECRET=CLAVESECRETA
HOST=localhost
USER=root
PASS=root
DB=legaltycs
```
- Cree una base de datos mysql con el nombre "legaltycs" y ejecute la siguiente query

``` sql
create table user(
	  username varchar(20),
    password varchar(255),
    name varchar(255),
    lastname varchar(255),
    PRIMARY KEY (username)
);
```
- Ejecute el servicio con el comando
```
$ python main.py
```
