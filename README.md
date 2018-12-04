# Flask SQL-Alchemy and ORM

I need to try and get a grip of a basic project which has the following items

  - Flask
  - SqlAlchemy-ORM
  - Flask-Restful API
  
This is the basic framework/boilerplate that I am using. 

It does the following

  - Create an Sqlite3 database
  - Populates with 1 Table
  - Runs a Flask Restful-Api 
  - Provides 2 Entry Points
    - http://localhost:5000/
    - http://localhost:5000/users

# Project Folder Meaning

## Controllers

I am creating a File per DbTable. Each file should have the following Classes

   - Users
     - Show All Users
     - PUT
       - Place the code for Creating a new User
     - UPDATE
       - Place the code for Updating an existing User
     
   - User
     - GET
       - Place the code for listing 1 specific User
     - DELETE
       - Place the code for deleting 1 specific User
       
## Database

Create the global objects

  - db
    - The Database Handle
  - Base
    - Used by the ORM to create/check the Database
  - db_session
    - Used for the Sessions
    
## Db

This is the folder that the database is defined in. It can be switched to any other location. 

## Models

These are the table definitions. 

Please note the Database table class need to be of type Base.

Plus each class needs a __tablename__ entry.

Example:

```python
class user(Base):
    __tablename__ = 'users'
```
    
## Server

This is where the Global flask Settings are set. Please note that this is also where the db location is specified.

There are currently 3 standard Configs.

  - Production
  - Test
  - Development
  
The App will look at an ENV Value i.e. $FLASK_ENV

To Specify a Specific Run-Time Env please report the Env like this.

```bash
export FLASK_ENV=PRODUCTION
```

If an Env is not found then the app defaults to **DEVELOPMENT** env.


## Views

These are the HTML Objects that may (or may not be needed).

It seesm to a convention within Flask that the static html pages go into a directory called **static**, and the dynamic pages, and placed in a directory called **template**.

Presently none of these are included. This is intentional.


### Logging

There is a sample Logging file in server, this is implemented using **daiquiri**  - which is a nicer form of logging in Python.

At the moment the log file is placed in the /application folder - This is Ok for
Testing and development purposes but will need to be corrected for production/Docker.
     
It is *strongly* recommended that you create separate Logging config files, each for the varying Run/Levels.


# Restful Api's

The previous code assumed that we are wrapping a Database, Web Service - and probably HTML - to propduce a standard-ish Web App, You are not however compelled to use this as a WebServer, instead you may with to create a RESTFUL Api - one which could have HTML, or which may not. There is nothing in the previous Models/Controllers that stops Flask, SqlAlchemy/ORM etc from being a Restful API - it is just that there are slightly better ways of doing it. 

## Standard Flask and Restful-Api - the main issues.

When I say there are issues, this is a little over-exagerated, as their as simply better and easier ways of doing a REST-API. Inside the testing module for "standard Flask" (application/server/test/testserver.py) we  had to write some code like this.

```python

        self.assertEqual(200, res.status_code)
        ret_obj  = json.loads(res.data.decode())
        self.assertEqual(self.bucketlist, ret_obj)
```

We had to manually convert the Request that we sent back and for this I used the Flask Response Class i.e.

```python
    return jsonify({"Name":"default"})
```

This data was received as a ByteArray - despite me trying to force it to being a json Object (the jsonify).

This is an example of how life can be made easier if we are going to develo Restful API's

## Flask-Restful

It is quite painless to make your FlaskProject Flask-Restful, it involves importing **from flask_restful import Api**

And Adding an Api creation after the app is initialized (Look in the /application/server.py).

To create a restful-Class, please look at the /application/controllers/UserRESTAPI.py.

### UserRestAPI

This module has a simple definition for 2 API Endpoints. It has a Global Dictionary to store the data items, but this could also be the Database/ORM we have previously defined. 

  - GET
  - PUT

As the GET is the simplest of the two - and depending on your RESTAPI - you may only want to share a READ_Only view of your data. In which case this is the only End-Point that you are going to implement. 

#### GET

This is called from a CURL Request like this

```bash
curl -X GET  -i http://127.0.0.1:5000/REST/1
```

Note: The 'Route' end is **/REST/**"


### Flask-RestPlus


 


# ToDo
   - Simple Html Page
   - Add Some Users
   - Testing (Limited Done)
   - Documentation   
   
   
   