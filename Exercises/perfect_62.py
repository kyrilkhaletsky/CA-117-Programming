import sys

def sumFac(n):
   total = 0
   i = 1
   for i in range(1, n // 2 + 1):
      if n % i == 0:
         total = total + i
      i += 1
   return total

def isPerfect(n):
   return n == sumFac(n)


def main():
   for n in sys.stdin:
      n = int(n)
      print(isPerfect(n))

if __name__ == "__main__":
   main()
      
      
