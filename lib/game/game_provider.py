from lib.game.mnk.mnk import MNK


def add_game_argument(parser):
    """
    Adding a --game argument to the argument parser with the available games

    Args:
        parser (ArgumentParser): The initialized parser
    """
    parser.add_argument("-g", "--game", required=True, choices=['0', '1'],
                        help="The type of game. 0: MNK, 1: MNK")


def get_game(args):
    """
    Return the game instance specified in args

    Args:
        args: parsed args from ArgumentParser)
    """
    game_type = args.game
    return MNK() if game_type == '0' else MNK()