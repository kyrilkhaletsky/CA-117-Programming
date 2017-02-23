import sys

def palin(s):
   s = s.lower()
   for l in s:
      if l.isalpha():
         pass
      else:
         s = s.replace(l, "")
      
   if s[::-1] == s:
      return True
   else:
      return False
   

def main():
   s = palin(sys.argv[1])
   print(s)

if __name__ == "__main__":
   main()

