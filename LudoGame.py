
class Player:
    "The constructor of the player playing the Ludo Game"

    def __init__(self):
        "The method of the Player class. Takes no parameters. Initializes the required data members.\
        All data members are private."

        # self.position = The player start position (A, B, C, or D)
        # Start and end Space of the player (Hardcoded)
        # self._step_count_of_token_p = -1
        # self._step_count_of_token_q = -1
        # is_stacked = false

    def get_completed(self):
        win = True

        #to notify when the game will end

        # return true or false

    def get_token_p_step_count(self):
        " to get value of self._step_count_of_token_p outside its class"

        # return of self._step_count_of_token_p

    def get_token_q_step_count(self):
        " to get value of self._step_count_of_token_q outside its class"

        # return of self._step_count_of_token_q

    def get_space_name(self,token_steps):
        " determine the location of a token"

        # return space the token has landed on as a string
            # H - homeyard
            # R - ready to go
            # E - end

    def increase_token_steps(self, token_name, step_count):
        " to move a token the amount on the dice for that player"

class LudoGame:
    " Constructs the game being played "

    def __init__(self):
        "The constructor of the LudoGame class. Takes no parameters. Initializes the required data members.\
        All data members are private."
        # self._list_of_players = []

    def get_player_by_position(self, position):
        "to determine if there is a player on a space"

        # return the player_object of the player on that space on the board
        # "Player not found!" - there is no player in that position

    def move_token(self, player_object, token_name, steps_token):
        "moves one token on the board, updates the total steps, kicks out other opponent's tokens and stacking "

        # return Nothing

    def play_game(self, player_list, turn_list):
        "Creates all player objects and stores them in self._list_of_players. Takes the number rolled and decides\
        based on a priority list which piece for the player should be moved"

        # return List_of_strings - the current spaces of all the tokens for each player after the turn
