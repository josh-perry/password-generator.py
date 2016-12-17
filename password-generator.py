'''
Make a password generator that generates a random password of desired length specified by user input.

For example:
Enter desired password length>> 7
hY@rSdA
'''

import random
import string
import argparse
import sys


def create_character_list(args):
    """Create the list of allowed characters to generate passwords from"""
    possible_chars = []

    if args.uppercase_ascii:
        possible_chars += string.ascii_uppercase

    if args.lowercase_ascii:
        possible_chars += string.ascii_lowercase

    if args.numerical:
        possible_chars += string.digits

    if args.punctuation:
        possible_chars += string.punctuation

    return possible_chars


def generate_password(possible_chars, length):
    """Generate a password of specified length using the characters provided."""
    password = ""

    for i in xrange(length):
        password += random.choice(possible_chars)

    return password


def main(args):
    """Generate the number of passwords requested"""
    # Create the list of allowable characters
    possible_chars = create_character_list(args)

    # Generate [args.count] passwords
    for c in xrange(args.count):
        # Generate and print to stdout
        p = generate_password(possible_chars, args.length)
        print(p)


def check_args(args):
    """Checks to see if at least one of the character options was set"""
    if not (args.uppercase_ascii and args.lowercase_ascii and args.numerical and args.punctuation):
        return False

    return True


if __name__ == '__main__':
    """Take and parse arguments and passing them to main"""
    parser = argparse.ArgumentParser(description="Generate passwords")
    parser.add_argument("--uppercase_ascii", "-A", help="Use uppercase ASCII", default=False, action="store_true")
    parser.add_argument("--lowercase_ascii", "-a", help="Use lowercase ASCII", default=False, action="store_true")
    parser.add_argument("--numerical", "-n", help="Use numerical characters", default=False, action="store_true")
    parser.add_argument("--punctuation", "-p", help="Use punctuation characters", default=False, action="store_true")
    parser.add_argument("--length", "-l", help="Generate a password of this length", default=8, type=int)
    parser.add_argument("--count", "-c", help="How many passwords to generate", default=1, type=int)

    args = parser.parse_args()

    if not check_args(args):
        sys.exit("No allowable characters specified!")

    # Parse arguments
    main(args)
