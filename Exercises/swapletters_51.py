import sys

def main():
   l = []
   s = sys.argv[1]
   for k in s:
      l.append(k)

   newlist = []
   if len(l) % 2 == 0:
      i = 1
      while i < len(l):
         newlist.append(l[i])
         newlist.append(l[i-1])
         i += 2
      print("".join(newlist))
         
   else:
      i = 1
      while i < len(l):
         newlist.append(l[i])
         newlist.append(l[i-1])
         i += 2
      newlist.append(l[-1])
      print("".join(newlist))

if __name__ == "__main__":
   main()
