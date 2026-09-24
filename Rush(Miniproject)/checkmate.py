PIECES = "PBRQK"

DIRECTIONS = [
    (1, 0, True), (-1, 0, True), (0, 1, True), (0, -1, True),
    (1, 1, False), (1, -1, False), (-1, 1, False), (-1, -1, False),
]


def find_attacker(board):
    """Return (piece, x, y) of a piece attacking the King, or None if safe.
    Raise ValueError if the board is invalid."""
    if not isinstance(board, str):
        raise ValueError("board must be a string")

    rows = board.splitlines()
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        raise ValueError("board must be a non-empty square")

    kings = [(x, y)
             for y, row in enumerate(rows)
             for x, char in enumerate(row)
             if char == "K"]
    if len(kings) != 1:
        raise ValueError("board must contain exactly one King")
    kx, ky = kings[0]

    # Pawn: attacks diagonally upward, so it sits diagonally below the King
    for dx in (-1, 1):
        x, y = kx + dx, ky + 1
        if 0 <= x < size and 0 <= y < size and rows[y][x] == "P":
            return ("P", x, y)

    for dx, dy, straight in DIRECTIONS:
        x, y = kx + dx, ky + dy
        while 0 <= x < size and 0 <= y < size:
            char = rows[y][x]
            if char in PIECES:
                if char == "Q" or (char == "R" and straight) \
                        or (char == "B" and not straight):
                    return (char, x, y)
                break  # first piece blocks the path
            x += dx
            y += dy
    return None


def checkmate(board, verbose=False):
    try:
        attacker = find_attacker(board)
    except ValueError:
        print("Error")
        return
    if attacker is None:
        print("Fail")
    elif verbose:
        piece, x, y = attacker
        print(f"Success ({piece} at column {x}, row {y})")
    else:
        print("Success")
