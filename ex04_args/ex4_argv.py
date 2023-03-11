from sys import argv, exit

if __name__ == "__main__":

    # Check at least one argument specified
    if len(argv) == 1:
        print(f"{argv[0]}: No argugment provided!")
        exit(1)

    # Get help with -h or -help
    if len(argv) == 2 and argv[1] in ['-h', '--help']:
        print(f"{argv[0]}: Exercise 4 - Dealing with Command Line Arguments")

    # At least three arguments that are flags
    elif len(argv) == 2 and argv[1] in ['-v', '--version', '-d', '--debug']:
        print(f"Exercise 4: Flags - {argv[1]}")

    # At least three arguments that are options
    elif len(argv) == 3 and argv[1] in ['--option1', '--option2', '--option3']:
        print(f"Exercise 4: Optional argument - {argv[1]} {argv[2]}")

    # Additional “positional” arguments
    elif len(argv) == 2 and argv[1] in ['pos1', 'pos2', 'pos3']:
        print(f"Exercise 4: Positional argument - {argv[1]}")

    # Invalid arugment
    else:
        print("Invalid argument provided!")
