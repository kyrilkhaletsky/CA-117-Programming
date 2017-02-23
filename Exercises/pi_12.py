import sys
import math

def pi(n):
   return ('{:.{}f}'.format(math.pi, n))

def main():
   n = pi(sys.argv[1])
   print(n)

if __name__ == "__main__":
   main()
