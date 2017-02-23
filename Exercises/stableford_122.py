import sys

points = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

def sorter(t):
   return t[1]

def sorter2(t):
   return t[0]

def calculator(handicap, hole_index):
   calculated = handicap // 18 + (handicap % 18 >= hole_index)
   return calculated

def main():
   pars = sys.stdin.readline().split()
   index = sys.stdin.readline().split()
   pars_index ={}
   handicaps = {}
   name = {}
 
   i = 0
   while i < len(index):
      pars_index[i+1] = pars[i], index[i]
      i += 1
     
   for line in sys.stdin:
      details = line.strip().split()
      handicaps[" ".join(details[0:-19])] = details[-19], details[-18:]
      sortnames = (sorted(handicaps.items(), key = sorter2))

   for i in range(0, len(sortnames)):
      total = 0
      score = 0
      players = sortnames[i]
      for j in range(0, len(players[1][1])):
         if players[1][1][j] == "X":
            continue
         elif int(players[1][1][j]) - int(pars[j]) - calculator(int(players[1][0]), int(index[j])) > 2:
            score += 0
         else:
            score += points[int(players[1][1][j]) - int(pars[j]) - calculator(int(players[1][0]), int(index[j]))]
      name[players[0]] = score

   newname = sorted(name.items(), key = sorter, reverse = True)
   length = 0
   for k in newname:
      if len(k[0]) > length:
         length = len(k[0])
   for person in newname:
      print("{:>{}} : {:>2}".format(person[0], length, person[1]))

if __name__ == "__main__":
   main()
