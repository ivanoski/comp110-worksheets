class OxoBoard:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        # create a 2D array of a 3 X 3 grid
        self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    def get_square(self, x, y):
        #this function returns the value of a square in the array
        return self.board [x][y]


    def set_square(self, x, y, mark):
        #This function sets a square in the array
        if get_square(x, y) == 0:
            self.board[x][y] = mark
            return True
        else:
            return False


    def is_board_full(self):

        fullTiles = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                squareContent = get_square(i, j)
                if squareContent != 0:
                    fullTiles += 1
                    if fullTiles == 9:
                        return True
                else:
                    return False



    def get_winner(self, latestX, latestY, currentPlayer):

        total = latestX + latestY
        checkDiagnols = 0
        rowCount = 0
        coloumnCount = 0

        # Check if we need to check diagnols by checking if the sum of the x and y tiles is even

        if total % 2 == 0:
            checkDiagnols == 1

        ### CHECK HORIZONTAL AND VERTICAL 3 IN A ROW ###

        for i in range(2):


            Square = get_square(i, latestY)
            if Square == currentPlayer:
                rowCount += 1
                if rowCount == 3:
                    return currentPlayer
                    break


            Square = get_square(latestX, i)
            if Square == currentPlayer:
                coloumnCount += 1
                if coloumnCount == 3:
                    return currentPlayer
                    break

        ###### CHECK DIAGNOLS ######

        # here i try to speed up the process by eliminating useless checks

        if checkDiagnols == 1:
            if latestX and latestY == 1:
                checkDiagnol_1 = 1
                checkDiagnol_2 = 1
            elif total == 2:
                checkDiagnol_2 = 1
            else:
                checkDiagnol_1 = 1



            if checkDiagnol_1 == 1:

                for i in range(2):
                    count = 0
                    square = get_square(i, i)
                    if square == currentPlayer:
                        count += 1
                        if count == 3:
                            return currentPlayer
                            break

            if checkDiagnol_2 == 1:

                for i in range(2):
                    count = 0
                    square = get_square(i, 2 - i)
                    if square == currentPlayer:
                        count += 1
                        if count == 3:
                            return currentPlayer
                            break
        return 0









    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard(3, 3)
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner(x, y, current_player)
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
