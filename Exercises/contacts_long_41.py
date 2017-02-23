import sys

f = open(sys.argv[1], "r")
number = {}

for w in f:
   details = w.split()
   number[details[0]] = details[1], details[2]

for w in sys.stdin:
   spec = w.split()
   if spec[0] in number:
     t = number[spec[0]]
     print ("Phone:", t[0])
     print ("Email:", t[1]) 
   else:
     print("No such contact")
