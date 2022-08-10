
post_ready_to_go_values = [1, 15, 29, 43]
pre_home_squares_values = [50, 8, 22, 36]

home_yard = ('H', -1)
ready_to_go = ('R', 0)
end_square = ('E', 57)

# Definition of terms
# POSITION: A,B,C, etc.
# LOCATION: -1, 0, 1-57
# STEPS: # of steps to adjust a location

class Player:
    """The constructor of the player playing the Ludo Game"""
    __position = None
    __tokens = None
    __pre_home_square_step_count = None


    def __init__(self, position_param):
        """The method of the Player class. Takes no parameters. Initializes the required data members.\
        All data members are private."""
        self.__position = position_param
        self.__tokens = [['P', home_yard[1]], ['Q', home_yard[1]]]
        print(ord(self.__position) - 65)
        self.__pre_home_square_step_count =\
            pre_home_squares_values[ord(self.__position) - 65]
        # self.__position = The player start position (A, B, C, or D)
        # Start and end Space of the player (Hardcoded)
        # self.___step_count_of_token_p = -1
        # self.___step_count_of_token_q = -1
        # is_stacked = false


    def get_position(self):
        return self.__position

    def set_token_step_count(self, token, step_count):
        if token == 'P':
            self.__tokens[0][1] = step_count
        else:
            self.__tokens[1][1] = step_count

    def get_completed(self):
        for token in self.__tokens:
            if token[1] != end_square[1]:
                return False
        return True

    def print_locations(self):
        print(f"  P: {self.__tokens[0][1]}")
        print(f"  Q: {self.__tokens[1][1]}")

        #to notify when the game will end

        # return true or false

    def get_token_p_step_count(self):
        """ to get value of self.___step_count_of_token_p outside its class"""
        return self.__tokens[0][1]

        # return of self.___step_count_of_token_p

    def get_token_q_step_count(self):
        """ to get value of self._step_count_of_token_q outside its class"""
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
        if token_steps == home_yard[1]:
            return home_yard[0]
        elif token_steps == ready_to_go[1]:
            return ready_to_go[0]
        elif token_steps == end_square[1]:
            return ready_to_go[0]
        elif (token_steps > self.__pre_home_square_step_count)\
                and (token_steps < self.__pre_home_square_step_count + 7):
            return self.__position +\
                   str(token_steps - self.__pre_home_square_step_count)
        else:
            return str(token_steps)

        # return space the token has landed on as a string
            # H - homeyard
            # R - ready to go
            # E - end
            # E - end

    # def increase_token_steps(self, token_name, step_count):
    #     " to move a token the amount on the dice for that player"
    #     if token_steps == home_yard.value:
    #         return home_yard.key
    #     elif token_steps == ready_to_go.value:
    #         return ready_to_go.key
    #     elif token_steps == end_square.value:
    #         return ready_to_go.key
    #     elif (token_steps > self.pre_home_square_step_count)\
    #             and (token_steps < self.pre_home_square_step_count + 7):
    #         return self.position +\
    #                str(token_steps - self.pre_home_square_step_count)
    #     else:
    #         return str(token_steps)


class LudoGame:
    """ Constructs the game being played """

    __list_of_players = None

    # post_ready_to_go_pos = [1, 15, 29, 43]
    # pre_safe_area_pos = [50, 8, 22, 36]

    # home_yard = -1
    # ready_to_go = 0



    __board = []

    __positions = ['A', 'B', 'C', 'D']

    __six_count = 0

    def __init__(self):
        """The constructor of the LudoGame class. Takes no parameters. Initializes the required data members.\
        All data members are private."""

        # print(player_list)
        # print(turn_list)

        counter = 1
        for position in self.__positions:
            # self.board.append((position, [self.home_yard, self.home_yard]))
            tmp_player = Player(position)
            self.__board.append(tmp_player)
            counter += 1

        print('here 1')
        # print(self.__board)

    def print_player_locations(self):
        print('A:')
        self.__board[0].print_locations()
        print('B:')
        self.__board[1].print_locations()


    def get_player_by_position(self, position):
        for player in self.__board:
            if player.get_position() == position:
                return player

        return 'Player not found!'


    def get_player(self, location):
        """to determine if there is a player on a space"""
        if location > 56 or location < 1:
            return 'not pertinent'

        for player in self.__board:
            if player.is_any_token_on_space(location):
                return player

        # No player on that location
        return None

    def move_token(self, player, token_name, steps_to_move):
        """moves one token on the board, updates the total steps,
         kicks out other opponent's tokens and stacking """


        if token_name == 'P':
            print('here 50')
            current_pos = player.get_token_p_step_count()
        else:
            print('here 60')
            current_pos = player.get_token_q_step_count()

        print(f'About to move player {player.get_position()} piece {token_name}'
              f' steps {steps_to_move}')

        # Handle six count first
        if steps_to_move == 6:
            if self.__six_count == 2:
                # Too many sixes
                self.__six_count = 0
                print('Too many sizes, noop')
                return
            else:
                self.__six_count += 1
        else:
            self.__six_count = 0


        if current_pos == -1 and steps_to_move == 6:
            # Home yard
            print('here 70')
            print(token_name)
            player.set_token_step_count(token_name, 0)
        # elif current_pos == 0:
        #     # ready to go
        #     player.set_token_step_count(token_name, current_pos + steps_to_move)
        # don't know yet if we need special handling
        elif current_pos > 50:
            # home(safe) zone (51 - 56)
            if current_pos + steps_to_move == 57:
                player.set_token_step_count(token_name, 57)
            elif current_pos + steps_to_move > 57:
                print('Exceeded 57, noop')
            else:
                player.set_token_step_count(token_name,
                                            current_pos + steps_to_move)
        else:
            player.set_token_step_count(token_name, current_pos + steps_to_move)

            # Are we kicking out an opponent?
            # players_on_position




        # check the potential destination
        # can they move to that spot and what type of spot is it?



        # return Nothing

    def get_locations_by_player(self, player_position):
        for player, locations in self.__board:
            if player == player_position:
                return locations

    def is_game_done(self):
        print('here 200')
        for player in self.__board:
            # TODO: add token Q
            if player.get_token_p_step_count() == 57:
                return True
        return False

    def play_game(self, player_list, turn_list):
        """Creates all player objects and stores them in self._list_of_players.
         Takes the number rolled and decides based on a priority list which
          piece for the player should be moved"""

        move_limit = 100
        move_count = 0

        self.print_player_locations()

        for turn in turn_list:
            print(f"Processing move #{move_count}")
            current_player = self.__board[0] if turn[0] == 'A' else self.__board[1]
            die_roll = turn[1]

            # for token in player_locations:
            print('here 10')
            self.move_token(current_player, 'P', die_roll)
            print('here 20')
            self.print_player_locations()
            move_count += 1
            if move_count == move_limit:
                print("Move limit reached")
                break

            if self.is_game_done():
                print(f"Game finished."
                      f" Player {current_player.get_position()} wins.")



            # iterate over the tokens
                # for a token, figure out the potential move (new position)
                # 1. If we have anyone at home, and the role is a 6
                # 2



        # Read through the items in turn_list, take the next element and update the state
        # of the board according to that element






        # return List_of_strings - the current spaces of all the tokens for each player after the turn
