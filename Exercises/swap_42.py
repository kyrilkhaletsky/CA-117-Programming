import sys

my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
new_dict = dict()

def swap_keys_values(my_dict):
   for (k, v) in my_dict.items():
      new_dict[v] = k
   return (new_dict)


def main():
   print(swap_keys_values(my_dict))


if __name__ == "__main__":
   main()
