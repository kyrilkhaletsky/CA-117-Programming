import sys

class Contact(object):
   
   def __init__(self,name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return "{} {} {}".format(self.name, self.phone, self.email)

# c = Contact("joe" "087 654311", "joe@yahoo.com")
# print(c)


class ContactList(object):
   
   def __init__(self, d = None):
      if d == None:
         d = {}
      self.d = d
         
   def add_contact(self, c):
      self.d[c.name] = c

   def del_contact(self, name):
      if name in self.d:
         del self.d[name]

   def get_contact(self, name):
      if name in self.d:
         return self.d[name].__str__()

   def __str__(self):
      pass

