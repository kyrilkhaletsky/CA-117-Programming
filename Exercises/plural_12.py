import sys

def plural(s):

   es_endings = ["ch", "sh", "x", "s", "z", "o"]
   vowels = "aeiou"

   if s[-2:] in es_endings or s[-1] in es_endings:
      return s + "es"
   if s[-1] == "y" and s[-2] not in vowels:
      return s[:-1] + "ies"
   if s[-2] == "f":
      return s[:-2] + "ves"
   if s[-1] == "f":
      return s[:-1] + "ves"
   else:
      return s + "s"


def main():
   s = plural(sys.argv[1])
   print(s)


if __name__ == "__main__":
   main()
