import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    # start at the first line
    line_number = 1

    # open files
    with open("AliceInWonderLand200.txt") as my_file:
        with open("dictionary.txt") as dictionary_file:
            dictionary = [line.strip().upper() for line in dictionary_file]

        # Linear Search
        print("---Linear Search---")
        print("Possible misspelled words:")

        # start searching for misspelled words
        for line in my_file:
            word_list = split_line(line)
            for word in word_list:
                if word.upper() not in dictionary:
                    print(f"Line {line_number}: {word}")
            line_number += 1

    # Binary Search
    print("---Binary Search---")
    print("Possible misspelled words:")

    # start at the beginning again
    line_number = 1

    # open the file again
    with open("AliceInWonderLand200.txt") as my_file:
        for line in my_file:
            word_list = split_line(line)

            # define variables
            for word in word_list:
                key = word.upper()
                lower_bound = 0
                upper_bound = len(dictionary) - 1
                found = False

                # start searching for misspelled words
                while lower_bound <= upper_bound and not found:
                    middle_pos = (lower_bound + upper_bound) // 2

                    if dictionary[middle_pos] < key:
                        lower_bound = middle_pos + 1

                    elif dictionary[middle_pos] > key:
                        upper_bound = middle_pos - 1

                    else:
                        found = True

                if not found:
                    print(f"Line {line_number}: {word}")
            line_number += 1


main()
