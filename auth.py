import re, json
from werkzeug.security import check_password_hash
import requests
from flask import session

# Check if the email provided is valid
def validate_email(email):
   # Possible order of combinations of an email
   pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   if re.match(pat,email):
      # Valid email
      return True
   else:
      # Invalid email
      return False

# Check if the email does not belong to another user
def email_in_use(email):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Look if email matches one that is already in use
   for id in users['user']:
      if users['user'][id]['email'] == email:
         # If so, return True
         return True
   # If no match, then return False
   return False   

# Check if the username given is not used by other user
def same_username(username):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Look if username matches one that is already in use
   for id in users['user']:
      if users['user'][id]['username'] == username:
         # If so, return True
         return True
   # If no match, then return False
   return False   

# Check if the given password and email are both for one specific user
def valid_user_pswd_combination(email, password):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Look if email has the same password
   for id in users['user']:
      # Check if email matches a user and
      # if the password corresponds to that user id
      if (users['user'][id]['email'] == email and 
         check_password_hash(users['user'][id]['password'], password)):
         # If so, return True
         return True
   # If no match, then return False
   return False

# Create a session with the respective email username and user_id
def create_session(email):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Looping through users to find the email that matches
   for id in users['user']:
      # Create a session with that user
      if users['user'][id]['email'] == email:
         session['user_id'] = id 
         session['email'] = users['user'][id]['email']
         session['username'] = users['user'][id]['username']
         return 1
   return 0

# Check if there is a valid session
def valid_session():
   # Check if session has the property of 'user_id'
   if 'user_id' in session:
      # If so, a session was created
      return True
   # Otherwise there is no session 
   return False

# Removing the data from the current session
def log_out():
   # Check if there is a valid session to be erased
   if valid_session():
      session.pop('user_id', None)
      session.pop('email', None)
      session.pop('username', None)
   return

# Getting the username from current session
def get_username():
   # Return the username of the current session
   return session['username']

