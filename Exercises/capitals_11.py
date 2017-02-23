import sys

def capitals(s):
   if len(s) > 1:
      return s[0].upper() + s[1:len(s)-1] + s[len(s)-1].upper()
   else:
      pass

def main():
   s = capitals(sys.argv[1])
   if s:
      print(s)

if __name__ == "__main__":
   main()
