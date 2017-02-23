import sys

def main():
   f = sys.stdin.readlines()
   count = 0

   for line in f:
      details = line.split()
      count = count + (len(details))
   print(count)

if __name__ == "__main__":
   main()
