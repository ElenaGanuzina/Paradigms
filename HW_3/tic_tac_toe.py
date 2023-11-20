"""
Основная парадигма - ООП: со временем при желании можно модифицировать и расширить(e.g. добавить вариант игры с ботом),
удобно тестировать.
Процеудурная - для удобства использования.
"""


class Cell:
    def __init__(self, value):
        self.value = value
        self.is_used = None

    def change_value(self, turn):
        if not self.is_used:
            if turn == 0:
                self.value = "x"
            elif turn == 1:
                self.value = "o"
            self.is_used = True
            return True
        else:
            print('\nThis cell is already used.')
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(value) for value in range(1, 10)]

    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(f" {self.cells[j + i * 3].value} ", end='')
            print()


class Player:
    def __init__(self, name):
        self.name = name
        self.winner = False
        self.variants = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                         [1, 4, 7], [2, 5, 8], [3, 6, 9],
                         [1, 5, 9], [3, 5, 7]]


class Game:
    def __init__(self, name_1, name_2):
        self.players = [Player(name_1), Player(name_2)]
        self.board = Board()
        self.is_over = False

    def step(self, turn):
        try:
            player_choice = int(input(f"It's {self.players[turn].name}'s turn: "))
            if self.board.cells[player_choice - 1].change_value(turn):
                self.board.show_board()
                for elem in self.players[turn].variants:
                    try:
                        elem.remove(player_choice)
                        if len(elem) == 0:
                            self.players[turn].winner = True
                    except ValueError:
                        pass
                return turn + 1
            else:
                return turn
        except IndexError:
            print('\nIncorrect cell number')
            return turn

    def game_over(self):
        if self.players[0].winner:
            self.is_over = True
            print(f"The game is over! {self.players[0].name} is the winner!")
        elif self.players[1].winner:
            self.is_over = True
            print(f"The game is over! {self.players[1].name} is the winner!")
        if all(cell.is_used for cell in self.board.cells):
            self.is_over = True
            print('The game is over! Draw!')


def game_round(name_1, name_2):
    game = Game(name_1, name_2)
    turn = 0
    game.board.show_board()
    while not game.is_over:
        turn = game.step(turn)
        turn = turn % 2
        game.game_over()


def lets_play():
    name_1 = input("Enter the 'X'-player name: ")
    name_2 = input("Enter the '0'-player name: ")
    game_round(name_1, name_2)

    while True:
        print("\nWould you like to play another round?"
              "\n1 - yes"
              "\n2 - no")
        proceed = int(input())
        if proceed == 1:
            name_1, name_2 = name_2, name_1
            game_round(name_1, name_2)
        elif proceed == 2:
            break
        else:
            print("Something went wrong! Choose again.")


if __name__ == '__main__':
    lets_play()
