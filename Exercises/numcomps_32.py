import sys

def main():
   multiples3 = [n for n in range(1, 31) if n % 3 == 0]
   print ("Multiples of 3: {}".format(multiples3))
   
   multiples3_sq = [n**2 for n in range(1, 31) if n % 3 == 0]
   print ("Multiples of 3 squared: {}".format(multiples3_sq))

   multiples4_db = [n*2 for n in range(1, 31) if n % 4 == 0]
   print ("Multiples of 4 doubled: {}".format(multiples4_db))

   multiples3o4 = [n for n in range(1, 31) if n % 3 == 0 or n % 4 == 0]
   print ("Multiples of 3 or 4: {}".format(multiples3o4))

   multiples3n4 = [n for n in range(1, 31) if n % 3 == 0 and n % 4 == 0]
   print ("Multiples of 3 and 4: {}".format(multiples3n4))

   multiples3x = [n if n % 3 else "X" for n in range(1, 31)]
   print ("Multiples of 3 replaced: {}".format(multiples3x))   

if __name__ == "__main__":
   main()
