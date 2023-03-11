import sys
import argparse

parser = argparse.ArgumentParser(description="Print file contents")
parser.add_argument('files', nargs='+', help='[files ...]')
parser.add_argument('-n', '--numbers', type=int, help='Number the output lines')
args = parser.parse_args()

class Cat:
    def print_files(self, filenames: list, lines=None) -> bool:
        """ Print files """
        if args:
            for filename in filenames:
                self.print_file(filename, lines)
            return True
        else:
            print(f"Usage: {sys.argv[0]} [file ...]")
            return False

    def print_file(self, filename: str, lines=None) -> None:
        """ Print a file """
        with open(filename) as file:
            if lines:
                self.print_lines(file, lines)
            else:
                print(file.read(), end="")

    def print_lines(self, file, lines: list) -> None:
        """ Print given number of lines of a file """
        count = 1
        for line in file.readlines():
            print(line, end="")
            if count == lines:
                return
            count += 1

if __name__ == "__main__":
    Cat().print_files(args.files, args.numbers)
