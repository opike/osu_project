""" Test clean up script """
from LudoGame.LudaGame import LudoGame

# from . import LudoGame
# from .general.utils import GeneralUtils


def main():  # pylint: disable=R0912
    """Begin main"""
    # print("something")
    ludo_game = LudoGame()

    # players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4),
             ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
             ('A', 5), ('A', 1), ('A', 5), ('A', 4)]


    # [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1),
    #  ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1),
    #  ('A', 5), ('A', 4)]

    # moves_original = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6),
    #                   ('B', 4),
    #          ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
    #          ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    # moves = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4),
    #          ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
    #          ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('A', 2), ('A', 6),
    #          ('A', 6), ('A', 2)]


    # moves = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4),
    #          ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
    #          ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('A', 2), ('A', 6),
    #          ('A', 6), ('A', 2)]

    players = ['A', 'B']

    moves = [('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 4)]

    # foo = ('A', -10)
    # print(foo[0])
    # print(foo[1])


    ludo_game.play_game(players, moves)



    # GeneralUtils.process_env_variables()
    #
    # tasks = ["clean.test_clean_up"]
    #
    # parser = argparse.ArgumentParser()
    #
    # parser.add_argument(
    #     "-d",
    #     "--debug",
    #     action="store_true",
    #     help="Debug mode. Generates more verbose console" " messages",
    # )
    #
    # parser.add_argument(
    #     "-f", "--test_function", default=None, help="Test function"
    # )
    #
    # parser.add_argument(
    #     "-u", "--username", help="Username", default="test_user@hipocampo.com"
    # )
    #
    # args = parser.parse_args()
    #
    # GeneralUtils.set_debug_mode(args.debug)
    #
    # GeneralUtils.run_tasks(args, tasks)


def main2():
    players = ['A', 'B']
    # turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6),
    #                   ('B', 4),
    #          ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
    #          ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    turns = [('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 4)]

    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))



if __name__ == "__main__":
    main2()
