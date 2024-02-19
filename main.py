
class Display:
    def __init__(self):
        self.x = 1
        self.turn_to_play = "O"
        self.repeat = False
        self.listo = []
        self.spaces_play = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.has_X_won = False
        self.has_O_won = False
        self.template = \
            f""""
    |   {self.spaces_play[0]}   |    {self.spaces_play[1]}    |    {self.spaces_play[2]}      |
      ______   ______     ______
    |   {self.spaces_play[3]}  |     {self.spaces_play[4]}    |    {self.spaces_play[5]}         |
      ______   ______     ______
    |   {self.spaces_play[6]}   |    {self.spaces_play[7]}    |    {self.spaces_play[8]}    |
    """

    def whose_turn_to_play(self):
        if self.repeat == True:
            print(f"it is {self.turn_to_play} turn to play oo")
        elif self.turn_to_play == "O":
            self.turn_to_play = "X"
            print("It is X turn to play oo")
        elif self.turn_to_play == "X":
            self.turn_to_play = "O"
            print("It is O turn to play oo")

    def play(self):
        bigger_while = True
        should_i = True
        while bigger_while:
            try:
                to_play = int(input("Wat number do you want to play boss"))
                while should_i:
                    if to_play in self.listo:
                        print("You cant play in a space that has already been played in")
                        self.repeat = True
                        self.x -= 1
                        bigger_while = False
                        break

                    else:
                        for spaces in range(1, 10):
                            if spaces == to_play:

                                real_play = input(f"Input {self.turn_to_play}").upper()

                                self.spaces_play[spaces - 1] = real_play

                                self.template = f""""
        |   {self.spaces_play[0]}   |    {self.spaces_play[1]}    |    {self.spaces_play[2]}     |
          ______   ______    ______
        |   {self.spaces_play[3]}  |     {self.spaces_play[4]}     |   {self.spaces_play[5]}      |
          ______   ______     ______
        |   {self.spaces_play[6]}   |    {self.spaces_play[7]}    |    {self.spaces_play[8]}    |
        """

                    print(self.spaces_play)
                    print(self.template)

                    should_i = False
                    self.repeat = False
                    bigger_while = False

            except ValueError:
                print("Boss you fit only play number oo")
                bigger_while = False
                self.repeat = True
                self.x -= 1

            else:
                self.listo.append(to_play)




    def check_if_game_has_ended_and_x_won(self):

        if self.spaces_play[0] == "X" and self.spaces_play[1] == "X" and self.spaces_play[2] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[3] == "X" and self.spaces_play[4] == "X" and self.spaces_play[5] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[6] == "X" and self.spaces_play[7] == "X" and self.spaces_play[8] == "X":
            self.has_X_won = True
            return  True
        elif self.spaces_play[0] == "X" and self.spaces_play[3] == "X" and self.spaces_play[6] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[1] == "X" and self.spaces_play[4] == "X" and self.spaces_play[7] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[2] == "X" and self.spaces_play[5] == "X" and self.spaces_play[8] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[0] == "X" and self.spaces_play[4] == "X" and self.spaces_play[8] == "X":
            self.has_X_won = True
            return True
        elif self.spaces_play[2] == "X" and self.spaces_play[4] == "X" and self.spaces_play[6] == "X":
            self.has_X_won = True
            return True
    def check_if_game_has_ended_and_o_won(self):
        if self.spaces_play[0] == "O" and self.spaces_play[1] == "O" and self.spaces_play[2] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[3] == "O" and self.spaces_play[4] == "O" and self.spaces_play[5] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[6] == "O" and self.spaces_play[7] == "O" and self.spaces_play[8] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[0] == "O" and self.spaces_play[3] == "O" and self.spaces_play[6] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[1] == "O" and self.spaces_play[4] == "O" and self.spaces_play[7] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[2] == "O" and self.spaces_play[5] == "O" and self.spaces_play[8] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[0] == "O" and self.spaces_play[4] == "O" and self.spaces_play[8] == "O":
            self.has_O_won = True
            return True
        elif self.spaces_play[2] == "O" and self.spaces_play[4] == "O" and self.spaces_play[6] == "O":
            self.has_O_won = True
            return True

play_game = Display()





make_i_continue = True
while play_game.x <= 9 and make_i_continue:
    play_game.whose_turn_to_play()
    play_game.play()

    if play_game.check_if_game_has_ended_and_x_won():
        print("X has won")
        make_i_continue = False
    elif play_game.check_if_game_has_ended_and_o_won():
        print("O don win ooo")
        make_i_continue = False
    print("sack")
    play_game.x += 1
    print(play_game.x)
if play_game.has_O_won is False and play_game.has_X_won is False:
    print("Na draw game oooooo")


