import sys

l = ["e", "v", "i", "l"]

def main():
   for line in sys.stdin:
      charlist = [c for c in line.strip().lower() if c in l]
      if charlist == l:
          print(line.strip())


if __name__ == "__main__":
   main()
   
   
