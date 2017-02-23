import sys

f = open(sys.argv[1], "r")
number = {}

for w in f:
   details = w.split()
   number[details[0]] = details[1]

for w in sys.stdin:
   spec = w.split()
   if spec[0] in number:
     print ("Phone: {}".format(number[spec[0]]))
   else:
     print("No such contact")
