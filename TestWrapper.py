""" Test clean up script """
from LudoGame.LudoGameF import LudoGame

# from . import LudoGame
# from .general.utils import GeneralUtils


def main():  # pylint: disable=R0912
    """Begin main"""
    # print("something")
    ludo_game = LudoGame()

    # [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1),
    #  ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1),
    #  ('A', 5), ('A', 4)]

    # moves_original = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6),
    #                   ('B', 4),
    #          ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
    #          ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    moves = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4),
             ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3),
             ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('A', 2), ('A', 6),
             ('A', 6), ('A', 2)]

    players = ['A', 'B']

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


if __name__ == "__main__":
    main()
