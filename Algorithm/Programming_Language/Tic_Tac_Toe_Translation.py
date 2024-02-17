import random
from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, size):
        self.num_moves = 0
        self.board = [["({},{})".format(i, j) for j in range(size)] for i in range(size)]
        self.current_player = "  X  "
        self.size = size
        self.X_score = [0, 0, 0]
        self.O_score = [0, 0, 0]

    @abstractmethod
    def legal_move(self, x, y):
        pass

    @abstractmethod
    def make_move(self, x, y):
        pass

    @abstractmethod
    def game_over(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

    @abstractmethod
    def reset_game(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class TicTacToe(Game):

    # Constructor for TicTacToe
    def __init__(self, size):
        super().__init__(size)
        if size < 3 or size > 9:
            print("Illegal size entered, setting size to 3")
            size = 3

        self.size = size
        self.board = [["({},{})".format(i, j) for j in range(self.size)] for i in range(self.size)]
        self.num_moves = 0
        self.current_player = "  X  "
        self.X_score = [0, 0, 0]
        self.O_score = [0, 0, 0]

    # Method to reset the game board
    def reset_game(self):
        self.board = [["({},{})".format(i, j) for j in range(self.size)] for i in range(self.size)]
        self.num_moves = 0

    # Method to determine if the input coordinates are a legal move
    def legal_move(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return False
        if self.board[x][y] in ["  X  ", "  O  "]:
            return False
        return True

    # Method to make a move
    def make_move(self, x, y):
        self.board[x][y] = self.current_player
        self.num_moves += 1
        self.current_player = "  O  " if self.current_player == "  X  " else "  X  "

    # Method for manual play
    def play_game(self):
        print("*******************************\n\n")
        print(self.__str__())
        row_val = -1
        col_val = -1
        try:
            row_val = int(input("Please enter the row you wish to move in: "))
            col_val = int(input("Please enter the column you wish to move in: "))
        except ValueError:
            print("One of the values you entered was not an integer. Please try again")
            self.play_game()
            return

        if not self.legal_move(row_val, col_val):
            print("You have entered an invalid row or column value")
            print("Please enter a value between 0 and", self.size - 1)
            self.play_game()
        else:
            self.make_move(row_val, col_val)
            result = self.game_over()
            if result == "  X  ":
                print("X has won the game!")
                self.X_score[0] += 1
                self.O_score[1] += 1
            elif result == "  O  ":
                print("O has won the game!")
                self.X_score[1] += 1
                self.O_score[0] += 1
            elif self.num_moves == (self.size * self.size):
                print("The game has ended in a tie!")
                self.X_score[2] += 1
                self.O_score[2] += 1
            else:
                self.play_game()

    # A method to randomly play the game
    def random_play_game(self, num_games):
        num_games = max(10, min(num_games, 1000))
        print(f"Simulating {num_games} number of random Tic-Tac-Toe games!")
        for _ in range(num_games):
            self.reset_game()
            game_won = False
            while not game_won:
                rand_x = random.randint(0, self.size - 1)
                rand_y = random.randint(0, self.size - 1)
                if self.legal_move(rand_x, rand_y):
                    self.make_move(rand_x, rand_y)
                result = self.game_over()
                if result in ["  X  ", "  O  "]:
                    game_won = True
                    print(f"{result.strip()} has won the game!")
                    if result == "  X  ":
                        self.X_score[0] += 1
                        self.O_score[1] += 1
                    else:
                        self.X_score[1] += 1
                        self.O_score[0] += 1
                elif self.num_moves == (self.size * self.size):
                    print("The game has ended in a tie!")
                    self.X_score[2] += 1
                    self.O_score[2] += 1
                    game_won = True

        print("**************************\nTHE GAMES ARE OVER!\n\n")
        print(f"After {num_games} games, we have the following records:")
        records = "Player\tWins\tLosses\tTies\n"
        records += f"X\t{self.X_score[0]}\t{self.X_score[1]}\t{self.X_score[2]}\n"
        records += f"O\t{self.O_score[0]}\t{self.O_score[1]}\t{self.O_score[2]}"
        print(records)

        # Method to check if the game is over

    def game_over(self):
        # Check horizontal and vertical lines
        for i in range(self.size):
            if len(set(self.board[i])) == 1:  # Check row
                return self.board[i][0]
            if len(set([self.board[j][i] for j in range(self.size)])) == 1:  # Check column
                return self.board[0][i]

        # Check diagonals
        if len(set([self.board[i][i] for i in range(self.size)])) == 1:
            return self.board[0][0]
        if len(set([self.board[i][self.size - i - 1] for i in range(self.size)])) == 1:
            return self.board[0][self.size - 1]

        # If there's no winner and the board is full, it's a tie
        if all(all(cell in ["  X  ", "  O  "] for cell in row) for row in self.board):
            return "Tie"

        return None  # Game is still ongoing

        # String representation of the current game board

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " | ".join(row) + "\n"
            board_str += "----" * self.size + "\n"
        return board_str


# This is my extra function which will act as a small GUI type thing to bring some extra functionality
# If this file is executed directly, we can start a game of TicTacToe letting user choose the length of the board
if __name__ == "__main__":
    game_size = input("Enter the size of the TicTacToe board (3-9): ")
    try:
        game_size = int(game_size)
    except ValueError:
        print("Invalid input. Defaulting to size 3.")
        game_size = 3
    tictactoe = TicTacToe(game_size)
    tictactoe.play_game()  # Start a game played by human
    # tictactoe.random_play_game(100)  # Uncomment to simulate 100 random games


class TicTacToeTwo(TicTacToe):
    def __init__(self, size, num_consecutive):
        super().__init__(size)
        self.num_consecutive = num_consecutive if 3 <= num_consecutive <= size else 3

    def game_over(self):
        # Checking rows for victory
        for i in range(self.size):
            counter = 1
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1] != ' ':
                    counter += 1
                else:
                    counter = 1

                if counter == self.num_consecutive:
                    return self.board[i][j]

        # Checking columns for victory
        for j in range(self.size):
            counter = 1
            for i in range(self.size - 1):
                if self.board[i][j] == self.board[i + 1][j] != ' ':
                    counter += 1
                else:
                    counter = 1

                if counter == self.num_consecutive:
                    return self.board[i][j]

        # Checking diagonal
        counter = 1
        for i in range(self.size - 1):
            if self.board[i][i] == self.board[i + 1][i + 1] != ' ':
                counter += 1
            else:
                counter = 1

            if counter == self.num_consecutive:
                return self.board[i][i]

        # Checking anti-diagonal
        counter = 1
        for i in range(self.size - 1):
            if self.board[i][self.size - i - 1] == self.board[i + 1][self.size - i - 2] != ' ':
                counter += 1
            else:
                counter = 1

            if counter == self.num_consecutive:
                return self.board[i][self.size - i - 1]

        # No winner found
        return "No winner!"




print("Welcome to Tic Tac Toe!")
print("We will be demoing two games, regular Tic Tac Toe, and a condensed version!")
print("The condensed version will allow you to win in runs of 2-n, where n is the size of the board!")

# Assuming the TicTacToe and TicTacToeTwo classes have been properly defined above
game_one = TicTacToe(4)

print("First we will validate the make move method and toString. Then we will call the play game and random play methods")
print(game_one)
game_one.make_move(0, 0)
game_one.make_move(1, 2)
game_one.make_move(3, 3)
print(game_one)

print("We will now reset the board and play the game once via user input")
game_one.reset_game()
# Uncomment the following lines if the play_game method is implemented and you want to run it.
# game_one.play_game()
# print("***************************\n********************\n")
# print(game_one)

print("Now to play random games!")
game_one.random_play_game(200)
game_two = TicTacToeTwo(4, 3)

# Uncomment the following line if the play_game method is implemented for TicTacToeTwo and you want to run it.
# game_two.play_game()
game_two.random_play_game(200)
print(game_one)
print(game_two)

# This block is the entry point of a Python program.
if __name__ == '__main__':
    # Call the main functionality here if it's defined in a function.
    pass
