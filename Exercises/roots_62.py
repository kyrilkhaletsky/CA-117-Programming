import sys
import math

def roots(a,b,c);
   if b**2 >= 4*a*c:
      x1 = (-b + math.sqrt(b**2 - 4*a*c))/ (2*a)
      x2 = (-b - math.sqrt(b**2 - 4*a*c))/ (2*a)
      return("r1 = "+str(x1) +", r2 = " + str(x2))

def main():
   for line in sys.stdin:
      tokens = line.strip().split()
      a = int(tokens[0])
      b = int(tokens[1])
      c - int(tokens[2])
      print(a,b,c)
      print(roots(a,b,c)

if __name__ == "__main__":
   main()
