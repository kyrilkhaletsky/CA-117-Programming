import sys

date = {
   "January" : 1,
   "February" : 2,
   "March" : 3,
   "April" : 4,
   "May" : 5,
   "June" : 6,
   "July" : 7,
   "August" : 8,
   "September" : 9,
   "October" : 10,
   "November" : 11,
   "December" : 12
}

def main():
   for line in sys.stdin:
      details = line.strip()
      details = line.split()
      print (str(details[0])+"/"+str(date[details[1]])+"/"+str(details[2][2:]))

if __name__ == "__main__":
   main()
