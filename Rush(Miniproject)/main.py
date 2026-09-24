import sys
from checkmate import checkmate


def main():
    args = sys.argv[1:]
    verbose = "-v" in args
    files = [arg for arg in args if arg != "-v"]

    for path in files:
        try:
            with open(path, "r") as f:
                board = f.read()
        except (OSError, UnicodeDecodeError):
            print("Error")
            continue
        checkmate(board, verbose)


if __name__ == "__main__":
    main()
