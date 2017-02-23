import sys

def substring(a, b):
   if b in a:
      return True
   else:
      return False

def main():
   a = sys.argv[1]
   b = sys.argv[2]
   print(substring(a, b))

if __name__ == "__main__":
   main()
