# This class serves as the TicTacToe board simply holding the game state.
# It also holds the method for performing minmax algorithm on itself, determining the best next move for either player
class TicTacToeBoard:
    def __init__(self):
        self.game_state = [[None, None, None], [None, None, None], [None, None, None]]  # start with a default board

    def isEmpty(self):  # returns True if board is empty, False if not
        for i in xrange(3):
            for j in xrange(3):
                if self.game_state[i][j]:
                    return False
        return True

    def check_end(self):  # this function determines whether the current game state is won by x or o, a draw, or None
        # check  horizontals
        for i in xrange(3):
            if self.game_state[i][0] == self.game_state[i][1] and self.game_state[i][0] == self.game_state[i][2]:
                if self.game_state[i][0]:
                    return self.game_state[i][0]
        # check verticals
        for i in xrange(3):
            if self.game_state[0][i] == self.game_state[1][i] and self.game_state[0][i] == self.game_state[2][i]:
                if self.game_state[0][i]:
                    return self.game_state[0][i]
        # check diagonals
        if self.game_state[0][0] == self.game_state[1][1] and self.game_state[0][0] == self.game_state[2][2]:
            if self.game_state[0][0]:
                return self.game_state[0][0]
        if self.game_state[2][0] == self.game_state[1][1] and self.game_state[2][0] == self.game_state[0][2]:
            if self.game_state[2][0]:
                return self.game_state[2][0]
        # check for draw or unfinished
        for i in xrange(3):
            for j in xrange(3):
                if self.game_state[i][j] is None:
                    return None
        return "Draw"

    def print_board(self):  # prints board
        for i in xrange(3):
            string_to_print = ""
            for j in xrange(3):
                if self.game_state[i][j]:
                    string_to_print += self.game_state[i][j] + " "
                else:
                    string_to_print += "- "
            print string_to_print

    # Adds "mark" (x or o) to board coordinates i,j. Returns 1 if successful, returns None if invalid coordinates
    def add(self, i, j, mark, printboard = True):
        try:
            i, j = int(i), int(j)  # in case i and j are not integers
            if self.game_state[i][j] is not None:
                print "Coordinates (" + str(i) + ", " + str(j) + ") are already filled"
                return None
            self.game_state[i][j] = mark
            if printboard:
                self.print_board()
            return 1
        except:
            print "Please enter valid coordinates (0-2)"
            return None

    # creates NEW deepcopy of board object and adds "mark" (x or o) to the new board's coordinates i,j
    def new_board(self, i, j, mark):
        new = TicTacToeBoard()
        for k in xrange(3):
            for l in xrange(3):
                new.game_state[k][l] = self.game_state[k][l]
        new.add(i, j, mark, False)
        return new

    # This function returns the minmax score for this particular TicTacToeBoard object
    # Perspective (turn taking player) determines whose score we are trying to maximize (x or o)
    # Perspective (turn taking player) will not change throughout the recursion
    # Turn determines if it is "x" or "o"'s turn. used to determine which mark to add on next board iterations
    # If calling function on a board, make sure first_call is set to True to return the coordinates of the maximum
    # score move
    def minmax(self, turn, perspective, first_call=False):
        result = self.check_end()  # check if current board is in an end state
        if result:  # if in an end state
            if result == perspective:  # if turn taking player has won, return 10
                return 10
            elif result == "Draw":  # if draw, return 0
                return 0
            else:  # if turn taking player has lost,
                return -10
        else:  # if not in an end state
            scores_list = []  # create empty list for scores list
            # reverse_turn contains the opposite of current turn. for passing to next minmax turns
            if turn == "x":
                reverse_turn = "o"
            else:
                reverse_turn = "x"
            for i in xrange(3):
                for j in xrange(3):
                    if not self.game_state[i][j]: # empty grid
                        new = self.new_board(i, j, turn)  # create new board with move
                        scores_list.append((new.minmax(reverse_turn, perspective), i, j))
            if turn == perspective:  # if it is perspective player's turn
                score = max(scores_list)
            else:  # if it is opposing player's turn
                score = min(scores_list)
            return score if first_call else score[0]


# This class is simply a data structure for holding the data for a Tic Tac Toe player.
# Holds name, type (human or computer player), and mark (X or O on board)
class Player:
    def __init__(self, name, mark="x", type=0):  # type 0 for human player, anything else for AI
        self.name = str(name)
        if type is 0:
            self.type = "human"
        else:
            self.type = "ai"
        if mark is "x":
            self.mark = "x"
        else:
            self.mark = "o"


# This class facilitates a game of TicTacToe and holds the method for starting a game between two players.
class TicTacToeGame:
    def __init__(self, player1=Player("Player 1", "o", 0), player2=Player("Reii", "x", 1)):
        self.board = TicTacToeBoard()
        self.player1 = player1
        self.player2 = player2
        self.next_player = self.player1  # first player is self.player1
        self.end = False  # flag to acknowledge game end

    def switch_player(self):
        if self.next_player is self.player1:
            self.next_player = self.player2
        else:
            self.next_player = self.player1

    def move(self):  # call to move next turn
        if self.next_player.type == "human":
            while True:
                crd1 = raw_input("Enter first coordinate: ")
                crd2 = raw_input("Enter second coordinate: ")
                if self.board.add(crd1, crd2, self.next_player.mark):
                    break

        else:  # if AI
            # check if board is empty. If it is, place marker anywhere. If it is not, run minmax()
            if self.board.isEmpty():
                self.board.add(1 , 1, self.next_player.mark)
            else:
                result = self.board.minmax(self.next_player.mark, self.next_player.mark, True)
                self.board.add(result[1], result[2], self.next_player.mark)

        # check end state
        if self.board.check_end():
            self.end = True
            if self.board.check_end() == "x" or self.board.check_end() == "o":
                print "Game over. " + self.next_player.name + " wins."
            else:
                print "Game drawn."
        self.switch_player()

    # This method sets the two players. Call this when starting the game.
    def set_players(self):
        setting = raw_input("Choose a setting for player 1. (Enter 0 for human, 1 for computer): ")
        while True:
            if setting != "0" and setting != "1":
                setting = raw_input("Please choose a setting for player 1. (Enter 0 for human, 1 for computer): ")
            else:
                break
        name = raw_input("Choose a name for player 1: ")
        while True:
            if not name:
                name = raw_input("Enter a name: ")
            else:
                break
        self.player1 = Player(name, "o", int(setting))

        setting = raw_input("Choose a setting for player 2. (Enter 0 for human, 1 for computer): ")
        while True:
            if setting != "0" and setting != "1":
                setting = raw_input("Please choose a setting for player 2. (Enter 0 for human, 1 for computer): ")
            else:
                break
        name = raw_input("Choose a name for player 2: ")
        while True:
            if not name:
                name = raw_input("Enter a name: ")
            else:
                break
        self.player2 = Player(name, "x", int(setting))
        self.next_player = self.player1


    def start(self):  # call to start game
        self.set_players()
        print "Game started between " + self.player1.name + " (" + self.player1.type + ") and " + self.player2.name+ " (" + self.player2.type + ")."
        self.board.print_board()
        while not self.end:
            print ""
            print self.next_player.name + " (" + self.next_player.type + ") moving..."
            self.move()


if __name__ == "__main__":
    TicTacToeGame().start()