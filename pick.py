"""
Module Docstring
"""

__author__ = "Grant Schowalter"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from random import random

def main(args):
    print(args)
    underdog = int(args.underdog)
    favorite = int(args.favorite)

    underdog_val = underdog * random()
    favorite_val = favorite * random()

    print(underdog_val)
    print(favorite_val)
    value = random()
    winner = underdog if underdog_val < favorite_val else favorite

    print("{} wins".format(winner))
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("underdog", help="favorite team")
    parser.add_argument("favorite", help="underdog team")

    # Optional argument flag which defaults to False
    parser.add_argument("-u", "--underdogpower", action="store", dest="under", default="1")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-s", "--starpower", action="store", dest="star", default="1")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)