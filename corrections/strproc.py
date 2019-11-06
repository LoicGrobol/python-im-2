import re
import sys


def main(inpt):
    with open(inpt) as in_stream:
        for l in in_stream:
            l = l.strip("\n")
            if "spam" in l:
                print("a")
            elif re.match(r".{,4}z$", l):
                print("b")
            elif re.search(r"(\w+\.\w+@\w+\.\w+)", l):
                match = re.search(r"(\w+\.\w+@\w+\.\w+)", l)
                print(match.group(1))
            elif l[:3] == l[-3:]:
                print("d")
            elif l == l[::-1]:
                print("e")
            else:
                print("NOPE")


if __name__ == "__main__":
    main(sys.argv[1])