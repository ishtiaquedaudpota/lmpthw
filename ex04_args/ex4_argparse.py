import argparse

if __name__ == "__main__":
    # Get help with -h or -help
    parser = argparse.ArgumentParser(description='Exercise 4 - Dealing with Command Line Arguments')

    # At least three arguments that are flags
    parser.add_argument('-f1', '--flag1', action='store_true', help='flag1')
    parser.add_argument('-f2', '--flag2', action='store_true', help='flag1')
    parser.add_argument('-f3', '--flag3', action='store_true', help='flag1')

    # At least three arguments that are options
    parser.add_argument('-o1', '--option1', help='Option1')
    parser.add_argument('-o2', '--option2', help='Option2')
    parser.add_argument('-o3', '--option3', help='Option3')

    # Additional “positional” arguments
    parser.add_argument('pos', help='Positional arguments', type=int, nargs='+')

    args = parser.parse_args()

    # flag arguments
    if args.flag1:
        print(f"Flag1 = {args.flag1}")
    elif args.flag2:
        print(f"Flag2 = {args.flag2}")
    elif args.flag3:
        print(f"Flag3 = {args.flag3}")

    # optional arguments
    if args.option1:
        print(f"Option1 = {args.option1}")
    elif args.option2:
        print(f"Option2 = {args.option2}")
    elif args.option3:
        print(f"Option3 = {args.option3}")

    # positional arguments
    if args.pos:
        print(sum(args.pos))
