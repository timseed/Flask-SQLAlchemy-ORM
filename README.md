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

This is where the Global flask Settings are set. Please note that this is also where the db location is stored.



     
     
   
    



# ToDo
   - Simple Html Page
   - Add Some Users
   - Testing
   - Documentation
   
   