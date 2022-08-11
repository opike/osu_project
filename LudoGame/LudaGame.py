import sys

class Player:
    """The constructor of the player playing the Ludo Game"""
    __position = None
    __tokens = None
    __pre_home_square_step_count = None
    __post_ready_to_go_step_count = None

    def __init__(self, position_param):
        """The method of the Player class. Takes no parameters. Initializes the required data members.\
        All data members are private."""
        self.__position = position_param
        self.__tokens = [['P', -1], ['Q', -1]]

        debug = True

        if debug: print('here 303')
        self.print_locations()

    def get_position(self):
        return self.__position

    def get_completed(self):
        print('in get_completed')

    def get_token_p_step_count(self):
        return self.__tokens[0][1]


    def get_space_name(self, token_steps):
        print('in get_space_name')


    def get_token_q_step_count(self):
        return self.__tokens[1][1]


    def print_locations(self):
        debug = True
        if debug: print(f"  P: {self.__tokens[0][1]}")
        if debug: print(f"  Q: {self.__tokens[1][1]}")




class LudoGame:
    """ Constructs the game being played """

    __player_list = None
    __board = []



    def print_player_locations(self):
        debug = True

        for player in self.__board:
            if debug: print(player.get_position() + ':')
            player.print_locations()





    def get_player_by_position(self, position):
        for player in self.__board:
            if player.get_position() == position:
                return player

        return 'Player not found!'


    def play_game(self, player_list, turn_list):
        """Creates all player objects and stores them in self.__player_list.
         Takes the number rolled and decides based on a priority list which
          piece for the player should be moved"""

        debug = True

        print(f'version: {sys.version}')

        if debug: print(player_list)
        if debug: print(turn_list)

        if debug: print(type(player_list))
        if debug: print(type(turn_list))

        if debug: print(type(player_list[0]))
        print('here 99')
        if debug: print(type(turn_list[0]))
        print('here 100')


        if debug: print(player_list[0])
        if debug: print(turn_list[0][0])
        print('here 101')
        if debug: print(turn_list[0][1])

        for position in player_list:
            if debug: print(position)
            tmp_player = Player(position)
            self.__board.append(tmp_player)
            if debug: print('400')
            self.print_player_locations()
