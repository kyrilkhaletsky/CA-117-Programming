import sys

def password(s):
   l = 0
   u = 0
   n = 0
   misc = 0

   i = 0
   while i < len(s):
      if s[i].isupper():
         u = 1
      elif s[i].islower():
         l = 1
      elif s[i].isnumeric():
         n = 1
      else:
         misc = 1
      i += 1
   return (u + l + n + misc)


def main():
   s = password(sys.argv[1])
   print (s)

if __name__ == "__main__":
   main()
