def checkmate(board: str):
    lines = board.split("\n")
    size = len(lines)
    king_pos = None
    pieces = {"P", "B", "R", "Q", "K"}

    # หา King
    for i in range(size):
        for j in range(len(lines[i])):
            if lines[i][j] == "K":
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")  # ถ้าไม่มี King ให้คืน Error
        return

    kx, ky = king_pos

    # ตรวจสอบการโจมตีจาก Pawn
    if kx > 0:
        if ky > 0 and lines[kx - 1][ky - 1] == "P":
            print("Success")
            return
        if ky < size - 1 and lines[kx - 1][ky + 1] == "P":
            print("Success")
            return

    # ตรวจสอบการโจมตีจาก Rook & Queen (แนวนอนและแนวตั้ง)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = kx, ky
        while 0 <= x + dx < size and 0 <= y + dy < size:
            x += dx
            y += dy
            if lines[x][y] == "R" or lines[x][y] == "Q":
                print("Success")
                return
            if lines[x][y] in pieces:
                break  # เจอชิ้นหมากตัวอื่นขวางทาง

    # ตรวจสอบการโจมตีจาก Bishop & Queen (แนวทแยง)
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x, y = kx, ky
        while 0 <= x + dx < size and 0 <= y + dy < size:
            x += dx
            y += dy
            if lines[x][y] == "B" or lines[x][y] == "Q":
                print("Success")
                return
            if lines[x][y] in pieces:
                break

    print("Fail")  # ถ้าไม่มีตัวหมากที่สามารถโจมตี King ได้