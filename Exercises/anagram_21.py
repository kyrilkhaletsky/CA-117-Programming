import sys

def anagram(line):

      details = line.split()
      
      a = sorted(details[0])
      b = sorted(details[1])
      
      return a == b

def main():
   for line in sys.stdin:
       print(anagram(line))

if __name__ == "__main__":
   main()


