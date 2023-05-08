import unittest
from auth import *

class TestValidateEmail(unittest.TestCase):
   def test_validate_email(self):
      #Test case 1: Invalid email
      self.assertEqual(validate_email('luis34'), False)

      #Test case 2: Valid email
      self.assertEqual(validate_email('luis@gmail.com'), True)
        
class TestEmailInUse(unittest.TestCase):
   def test_email_in_use(self):
      #Test case 1: Email in use
      self.assertEqual(email_in_use('luis@gmail.com'), True)

      #Test case 2: Email not in use
      self.assertEqual(email_in_use('luis34@gmail.com'), False)

class TestSameUsername(unittest.TestCase):
   def test_same_username(self):
      #Test case 1: Username in use
      self.assertEqual(same_username('LuisP'), True)

      #Test case 2: Username not in use
      self.assertEqual(same_username('edupicha'), False)

class TestValidUserPswdCombination(unittest.TestCase):
   def test_valid_user_pswd_combination(self):
      #Test case 1: Valid combination
      self.assertEqual(valid_user_pswd_combination('luis@gmail.com','Palo2020'), True)
      
      #Test case 2: Invalid email
      self.assertEqual(valid_user_pswd_combination('luis34@gmail.com','Palo2020'), False)

      #Test case 3: Invalid password
      self.assertEqual(valid_user_pswd_combination('luis@gmail.com','Abc123'), False)

if __name__ == '__main__':
    unittest.main()
