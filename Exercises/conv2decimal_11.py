import sys

a = sys.argv[1]
n = sys.argv[2]

def convert(a, n):
   total = 0
   i = 0
   n = int(n)
   while i < len(a):
      a = str(a)
      total = total + int(a[i]) * n ** (len(a) - i - 1)
      i += 1
   return total

def main():
   decimal = convert(a, n)
   print (decimal)

if __name__ == "__main__":
   main()
