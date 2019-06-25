import re

def phoneNumberValidation(number):
   pattern = '^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
   if re.match(pattern,str(number)):
       return True
   else:
       return False

#phoneNumberValidation(8106410134)

def emailValidator(email):
   pattern = "^[0-9a-z][0-9a-z-.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
   if re.match(pattern,email):
       return True
   return False