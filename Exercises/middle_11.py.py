import sys

def middle(s):
   if len(s) % 2 == 0:
      return "No middle character!"
   else:
      return (s[len(s) // 2])

def main():
   s = middle(sys.argv[1])
   print (s)

if __name__ == "__main__":
   main()
