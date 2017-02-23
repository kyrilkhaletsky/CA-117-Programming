import sys

def main():
   try:
      f = open(sys.argv[1], "r")
      maxmark = 0
      newname = ""
      for line in f:
         details = line.split()
         mark = int(details[0])
         name = " ".join(details[1:])
         if mark > maxmark:
            maxmark = mark
            newname = name
      print("Best student: " + newname + "\n" + "Best mark: " + str(maxmark))
   except ValueError:
      print("Invalid mark " + details[0] + " encountered. Skipping.")

if __name__ == "__main__":
   main()
