import sys


def main(inpt):
    with open(inpt) as in_stream:
        for l in in_stream:
            print(l.strip())


if __name__ == "__main__":
    main(sys.argv[1])