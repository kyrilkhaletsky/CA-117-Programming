import sys

nums = []
for k in sys.stdin:
   k = int(k.strip())
   nums.append(k)


def mean():
   n = 0
   for k in nums:
      n = n + k
   return("Mean: {:.1f}".format(n / len(nums)))
      
def mode():
   modes = {}
   modes2 = {}
   for i in nums:
      modes[i] = nums.count(i)
   print(modes)
   for (k,v) in modes.items():
      modes2[v] = k
   return("Mode: {:.1f}".format(modes2[max(modes2)]))
      
   

def median():
   sort = sorted(nums)
   if len(sort) % 2 == 0:
      med = ((sort[len(sort)//2]) + (sort[(len(sort)//2) - 1]))
      med = med / 2
   else:
      med = (sort[len(sort) % 2 + 1])
   return("Median: {:.1f}".format(med))
      

def main():
   print(median())
   print(mode())
   print(mean())

if __name__ == "__main__":
   main()
