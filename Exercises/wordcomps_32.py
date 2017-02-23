import sys

words = [words.strip() for words in sys.stdin]

vowels = ["a", "e", "i", "o", "u"]

def main():
   let17 = [w for w in words if len(w) == 17]
   print("Words containing 17 letters: {}".format(let17))

   more17 = [w for w in words if len(w) > 17]
   print("Words containing 18+ letters: {}".format(more17))

   
   
   

if __name__ == "__main__":
   main()
