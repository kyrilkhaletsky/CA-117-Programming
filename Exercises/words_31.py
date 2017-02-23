import sys
import string

l = []
d = {}

for k in sys.stdin:
   details = k.split()
   for w in details:
      w = w.lower().strip(string.punctuation)
      l.append(w)

for c in l:
   if c in d:
      d[c] = d[c] + 1
   else:
      d[c] = 1

for c in d:
   print("{}: {}".format(c, d[c]))
