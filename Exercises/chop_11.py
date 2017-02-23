import sys

def chop(s):
   return (s[1:len(s)-1])

def main():
   s = chop(sys.argv[1])
   if s:
        print(s)

if __name__ == "__main__":
   main()
