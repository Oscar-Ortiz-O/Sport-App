import re
import json

def validate_email(email):
   # Possible order of combinations of an email
   pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   if re.match(pat,email):
      # Valid email
      return True
   else:
      # Invalid email
      return False

def email_in_use(email):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Look if email matches one that is already in use
   for id in users['user']:
      if users['user'][id]['email'] == email:
         # If so, return True
         return True
   # If no matche, then return False
   return False   

def same_username(username):
   # Open the database file
   with open('data/database.json', 'r') as openfile:
      users = json.load(openfile)
   # Look if email matches one that is already in use
   for id in users['user']:
      if users['user'][id]['username'] == username:
         # If so, return True
         return True
   # If no matche, then return False
   return False   










