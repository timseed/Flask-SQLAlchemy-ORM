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


# ToDo
   - Simple Html Page
   - Add Some Users
   - Testing (Limited Done)
   - Documentation   
   
   
   