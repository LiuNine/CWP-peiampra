import sys
import re


def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    matches = re.findall(keyword, search_string)
    count = len(matches)

    if count == 0:
        print("none")
    else:
        print(count)


if __name__ == "__main__":
    main()