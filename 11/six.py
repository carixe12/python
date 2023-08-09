class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = " "
        self.is_occupied = False

    def occupy(self, symbol):
        if not self.is_occupied:
            self.symbol = symbol
            self.is_occupied = True
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.cells[i].symbol} | {self.cells[i+1].symbol} | {self.cells[i+2].symbol} |")
            print("-------------")

    def change_cell_state(self, cell_number, symbol):
        if cell_number < 1 or cell_number > 9:
            return False

        cell = self.cells[cell_number - 1]
        return cell.occupy(symbol)

    def check_game_ending(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combination in winning_combinations:
            symbols = [self.cells[i].symbol for i in combination]
            if symbols.count("X") == 3 or symbols.count("O") == 3:
                return True

        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        while True:
            cell_number = input(f"{self.name}, enter the cell number (1-9): ")
            if cell_number.isdigit():
                cell_number = int(cell_number)
                if 1 <= cell_number <= 9:
                    return cell_number
            print("Invalid input. Please enter a number from 1 to 9.")


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = None

    def play_turn(self):
        self.board.display()

        if self.current_player is self.player1:
            symbol = "X"
        else:
            symbol = "O"

        while True:
            cell_number = self.current_player.make_move()
            if self.board.change_cell_state(cell_number, symbol):
                break
            else:
                print("That cell is already occupied. Choose another cell.")

        if self.board.check_game_ending():
            self.board.display()
            print(f"{self.current_player.name} wins!")
            self.current_player.wins += 1
            return True

        return False

    def play_game(self):
        self.board = Board()
        self.current_player = self.player1

        while True:
            if self.play_turn():
                break

            if all(cell.is_occupied for cell in self.board.cells):
                self.board.display()
                print("It's a draw!")
                break

            if self.current_player is self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

        print("Current score:")
        print(f"{self.player1.name}: {self.player1.wins} wins")
        print(f"{self.player2.name}: {self.player2.wins} wins")

    @staticmethod
    def start_game():
        player1_name = input("Enter Player 1's name: ")
        player2_name = input("Enter Player 2's name: ")

        player1 = Player(player1_name)
        player2 = Player(player2_name)

        game = Game(player1, player2)

        while True:
            game.play_game()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break


if __name__ == "__main__":
    Game.start_game()