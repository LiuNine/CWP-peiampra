import sys


def downcase_it(s):
    return s.lower()


def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            print(downcase_it(arg))


if __name__ == "__main__":
    main()