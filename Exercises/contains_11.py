import sys
 
a = sys.argv[1]
b = sys.argv[2]

a = sorted(a)
b = sorted(b)

x = 0

i = 0
while i < len(a):
   if a[i] == b[i]:
      x = 1
   else:
      x = 0
   i += 1

if x == 1 or len(a) == 1:
   print(True)
else:
   print(False)

