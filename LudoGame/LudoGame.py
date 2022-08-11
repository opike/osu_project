
post_ready_to_go_values = [1, 15, 29, 43]
pre_home_squares_values = [50, 8, 22, 36]

home_yard = ('H', -1)
ready_to_go = ('R', 0)
end_square = ('E', 57)


debug = True

# Definition of terms
# POSITION: A,B,C, etc.
# LOCATION: -1, 0, 1-57
# STEPS: # of steps to adjust a location

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
        self.__tokens = [['P', home_yard[1]], ['Q', home_yard[1]]]

        if debug: print('here 300')
        self.print_locations()

        # if debug: print(ord(self.__position) - 65)
        self.__pre_home_square_step_count =\
            pre_home_squares_values[ord(self.__position) - 65]

        if debug: print('here 302')
        self.print_locations()

        self.__post_ready_to_go_step_count =\
            post_ready_to_go_values[ord(self.__position) - 65]

        if debug: print('here 303')
        self.print_locations()
        # self.__position = The player start position (A, B, C, or D)
        # Start and end Space of the player (Hardcoded)
        # self.___step_count_of_token_p = -1
        # self.___step_count_of_token_q = -1
        # is_stacked = false


    def get_position(self):
        return self.__position

    def set_token_step_count(self, token, step_count):
        # if debug: print(f'in set_token_step_count')
        if token == 'P':
            self.__tokens[0][1] = step_count
        else:
            self.__tokens[1][1] = step_count

    def get_completed(self):
        # if debug: print(f'in get_completed')
        for token in self.__tokens:
            if token[1] != end_square[1]:
                return False
        return True

    def print_locations(self):
        if debug: print(f"  P: {self.__tokens[0][1]}")
        if debug: print(f"  Q: {self.__tokens[1][1]}")

        #to notify when the game will end

        # return true or false

    def get_token_p_step_count(self):
        """ to get value of self.___step_count_of_token_p outside its class"""
        # if debug: print(f'in get_token_p_step_count')
        return self.__tokens[0][1]

        # return of self.___step_count_of_token_p

    def get_token_q_step_count(self):
        """ to get value of self._step_count_of_token_q outside its class"""
        # if debug: print(f'in get_token_q_step_count')
        return self.__tokens[1][1]


    def is_any_token_on_space(self, space):
        ret_val = False
        if self.get_space_name(self.get_token_p_step_count()) == space:
            return True
        if self.get_space_name(self.get_token_q_step_count()) == space:
            return True
        return ret_val


        # return of self._step_count_of_token_q

    def get_space_name(self, token_steps):
        """ determine the location of a token"""
        # if debug: print(f'in get_space_name')

        if token_steps == home_yard[1]:
            return home_yard[0]
        elif token_steps == ready_to_go[1]:
            return ready_to_go[0]
        elif token_steps == end_square[1]:
            return end_square[0]
        elif 57 > token_steps > 50:
            return self.__position +\
                   str(token_steps-50)
        else:
            tmp_val = token_steps + (self.__post_ready_to_go_step_count - 1)
            tmp_val = tmp_val if tmp_val < 57 else tmp_val - 56
            return str(tmp_val)


class LudoGame:
    """ Constructs the game being played """

    __player_list = None
    __board = []

    # __positions = ['A', 'B']

    # __six_count = 0

    def __init__(self):
        """The constructor of the LudoGame class. Takes no parameters. Initializes the required data members.\
        All data members are private."""

        # print(player_list)
        # print(turn_list)

        # counter = 1
        # for position in self.__positions:
        #     # self.board.append((position, [self.home_yard, self.home_yard]))
        #     tmp_player = Player(position)
        #     self.__board.append(tmp_player)
            # counter += 1

        # print('here 1')
        # print(self.__board)

    def print_player_locations(self):
        for player in self.__board:
            if debug: print(player.get_position() + ':')
            player.print_locations()

    def get_player_by_position(self, position):
        # if debug: print(f'in get_player_by_position')
        for player in self.__board:
            if player.get_position() == position:
                return player

        return 'Player not found!'


    def get_player_on_location(self, location):
        """to determine if there is a player on a space"""
        if location > 56 or location < 1:
            return 'not pertinent'

        for player in self.__board:
            if player.is_any_token_on_space(location):
                return player

        # No player on that location
        return None

    def get_locations_by_player(self, player_position):
        for player, locations in self.__board:
            if player == player_position:
                return locations

    def is_game_done(self):
        # Check that there's only one player left
        if debug: print('here 200')
        winner_count = 0
        for player in self.__board:
            # TODO: add token Q
            if player.get_token_p_step_count() == 57 and \
                    player.get_token_q_step_count() == 57:
                winner_count += 1

        return len(self.__board) - 1 == winner_count

    def move_token(self, player, token_name, steps_to_move):
        """moves one token on the board, updates the total steps,
         kicks out other opponent's tokens and stacking """
        # if debug: print(f'in move_token')


        if token_name == 'P':
            if debug: print('here 50')
            current_pos = player.get_token_p_step_count()
        else:
            if debug: print('here 60')
            current_pos = player.get_token_q_step_count()

        projected_location = current_pos + steps_to_move

        if debug: print(f'About to move player {player.get_position()} piece {token_name}'
              f' steps {steps_to_move}')


        if current_pos == -1 and steps_to_move == 6:
            # Home yard
            if debug: print('here 70')
            if debug: print(token_name)
            player.set_token_step_count(token_name, 0)
        # elif current_pos == 0:
        #     # ready to go
        #     player.set_token_step_count(token_name, current_pos + steps_to_move)
        # don't know yet if we need special handling
        elif current_pos > 50:
            # home(safe) zone (51 - 56)
            if projected_location == 57:
                player.set_token_step_count(token_name, 57)
            elif projected_location > 57:
                # handle bouncing
                if debug: print(f"Token {player.get_position()}{token_name} bounced")
                player.set_token_step_count(token_name,
                        114 - projected_location)
            else:
                player.set_token_step_count(token_name,
                                            projected_location)
        else:
            opponent = self.get_player_on_location(current_pos + steps_to_move)
            if opponent is not None:
                # handle kicking out
                if opponent.get_token_p_step_count() == projected_location:
                    opponent.set_token_step_count("P", -1)
                else:
                    opponent.set_token_step_count("Q", -1)
            player.set_token_step_count(token_name, current_pos + steps_to_move)






            # Are we kicking out an opponent?


        # check the potential destination
        # can they move to that spot and what type of spot is it?
        # return Nothing

    def select_token(self, player, steps):
        # Select the token we want to move
        if debug: print('foo')
        # if anyone is at home
        token_p_loc = player.get_token_p_step_count()
        token_q_loc = player.get_token_q_step_count()

        # Check for exit home yard
        if token_p_loc == -1 and steps == 6:
            return 'P'
        elif token_q_loc == -1 and steps == 6:
            return 'Q'

        # Check for stacked tokens
        if token_p_loc == token_q_loc:
            if 0 < token_p_loc < 57:
                return 'PQ'

        # Check for enter end game
        if token_p_loc + steps == 57:
            return 'P'
        elif token_q_loc + steps == 57:
            return 'Q'

        # Check for kick out opponent
        if (((token_p_loc + steps > 0) and (token_p_loc + steps < 51)) and
            (self.get_player_on_location(token_p_loc + steps) is not None) and
            (self.get_player_on_location(token_p_loc + steps).get_position() !=
             player.get_position())):
            return 'P'
        elif (((token_q_loc + steps > 0) and (token_q_loc + steps < 51)) and
              (self.get_player_on_location(
                  token_q_loc + steps) is not None) and
              (self.get_player_on_location(
                    token_q_loc + steps).get_position() !=
                 player.get_position())):
            return 'Q'


        # Move the furthest away token that is not in the home yard.
        if -1 < token_p_loc < 51:
            if token_p_loc < token_q_loc or token_q_loc == -1:
                return 'P'

        if -1 < token_q_loc < 51:
            if token_q_loc < token_p_loc or token_p_loc == -1:
                return 'Q'

        return None


    def play_game(self, player_list, turn_list):
        """Creates all player objects and stores them in self.__player_list.
         Takes the number rolled and decides based on a priority list which
          piece for the player should be moved"""

        if debug: print(player_list)
        if debug: print(turn_list)

        # six_count = 0
        # previous_position = None

        # Initialize the board
        for position in player_list:
            if debug: print(position)
            tmp_player = Player(position)
            self.__board.append(tmp_player)
            if debug: print('400')
            self.print_player_locations()

        move_limit = 100
        move_count = 0

        self.print_player_locations()

        for turn in turn_list:
            if debug: print(f"Processing move #{move_count}")
            current_player = self.__board[0] if turn[0] == 'A' else self.__board[1]
            die_roll = turn[1]

            if debug: print(f"Player {current_player.get_position()} rolls {die_roll}")

            # Handle six count first
            # if previous_position == current_player.get_position():
            #     if die_roll == 6 && six_count == 2:
            #
            # else:
            #     previous_position = current_player.get_position()
            #     six_count = 0



            # for token in player_locations:
            if debug: print('here 10')
            token = self.select_token(current_player, die_roll)

            if token is None:
                if debug: print(f"Player {current_player.get_position()} can't move")
            elif token == 'PQ':
                self.move_token(current_player, 'P', die_roll)
                self.move_token(current_player, 'Q', die_roll)
            else:
                self.move_token(current_player, token, die_roll)

            if debug: print('here 20')
            self.print_player_locations()
            move_count += 1
            if move_count == move_limit:
                if debug: print("Move limit reached")
                break

            if self.is_game_done():
                if debug: print(f"Game finished."
                      f" Player {current_player.get_position()} wins.")



            # iterate over the tokens
                # for a token, figure out the potential move (new position)
                # 1. If we have anyone at home, and the role is a 6
                # 2



        ret_val = []

        if debug: print('here 10')
        if debug: print(len(self.__board))

        for player in self.__board:
            ret_val.append(player.get_space_name(
                player.get_token_p_step_count()))
            ret_val.append(player.get_space_name(
                player.get_token_q_step_count()))

        return ret_val



        # Read through the items in turn_list, take the next element and update the state
        # of the board according to that element






        # return List_of_strings - the current spaces of all the tokens for each player after the turn
