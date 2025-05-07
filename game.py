board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "],
        ]

player = "X"

def display_board():
    for line in board:
        print("|".join(line))
        print("-"*5)

def play(line, column):
    if (
        not 0 <= line <= 2 or
        not 0 <= column <= 2 or
        board[line][column] != " "
    ):
        print("invalid play")
        return player
    board[line][column] = player
    return "O" if player == "X" else "X"

def winner():
    for line in range(3):
        if (
            board[line][0] != " " and
            board[line][0] == board[line][1] and 
            board[line][0] == board[line][2]
        ):
            print(f"{board[0][0]} it's the winner!!!")
            return True

    for column in range(3):
            if (
                board[0][column] != " " and
                board[0][column] == board[1][column] and 
                board[0][column] == board[2][column]
            ):
                print(f"{board[0][0]} it's the winner!!!")
                return True
            
    if (
        board[1][1] != " " and
        ( 
            (
                board[0][0] == board[1][1] and
                board[0][0] == board[2][2]
            ) or
            (
                board[0][2] == board[1][1] and
                board[1][1] == board[2][0]
            )
        )
    
    ):
        print(f"{board[1][1]} it's the winner!!!")
        return True
        
    return False

def draw():
    for line in range (3):
        for column in range (3):
            if board[line][column] == " ":
                return False
    print("draw!!!")
    return True

while True :
    print(f"player of the moment: {player}")
    try:
        line = int(input("type the line: "))
        column = int(input("type the column: "))
        player = play(line,column)
    except (ValueError, IndexError):
        print("type a number between 0-2")
    display_board()
    if winner():
        break
    if draw() or draw():
        break 
