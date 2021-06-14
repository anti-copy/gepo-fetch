"""
The root `gepofetch` command

The does nothing rather than dispatch to subcommands 
"""

import sys
import os


def main():
    if len(sys.argv) > 1:
        print("run command x ")
        pass
    else:
        print("invalid command!")


if __name__ == '__main__':
    main()
