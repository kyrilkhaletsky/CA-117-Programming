import sys
import re

def main():

    name_regex = re.compile(r"(M(?:r|rs|s)(?:\.?)(?:[A-Za-z\s]*?))(?:\s[a-z]|\n|$|\.)")

    s = sys.stdin.read()

    namelist = name_regex.findall(s)
    for n in namelist:
        print(n)

if __name__ == '__main__':
    main()
