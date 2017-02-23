import sys
import random

iterations = 1000000

def main():
   my_numbers = set()
   for n in sys.argv[1:]
      my_numbers.add(int(n))
   
   matches = {3:0, 4:0, 5:0, 6:0}

   for n in range(iterations):
      random_selection = set(random.sample(range(1,48), 6))
      match = len(random_selection.intersection(my_numbers))
      if match < 3:
         continue
      matches[match] += 1
   for (k,v) in sorted(matches.items()):
      odds = round(iterations/v) if v else "?"
      print("Match {}\"s : {:5d} ({} to 1)".format(k,v,odds))

if __name__ == "__main__":
   main()
