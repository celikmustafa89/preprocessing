# coding=utf-8
import re
import os
import string

__author__ = 'USER'


def main(*args):
    """ Preprocess the files for corpus

       1. Remove empty lines
       2. Regex that removes the punctuations
       3. replace TAB to space
       4. remove dublicate spaces
       5. convert uppercase to lowercase
       6. regex for number finding

    :param args:
    :return:
    """

    # gets the file name
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    write_file = open("birlesmis.txt", 'w')
    for file in files:
        if file == "main.py" or file == "birlesmis.txt":
            continue
        with open(file) as read_file:
            for line in read_file:
                if line == "" or line == " " or line == "\n":
                    continue
                else:
                    line = remove_new_line(line)
                    # line = remove_punctuation(line)
                    # line = replace_tab_with(line, " ")
                    # line = remove_duplicate_spaces(line)
                    # line = convert_to_lowercase(line)
                    # line = replace_numbers_with(line, "\"NUM\"")
                    write_file.write(line)  # write to file
    write_file.close()


def remove_punctuation(line):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in line if ch not in exclude)


def replace_tab_with(line, character):
    return line.replace('\t', character)


def remove_duplicate_spaces(line):
    return line.replace("  ", " ")


def convert_to_lowercase(line):
    return line.lower()


def replace_numbers_with(line, character):
    return re.sub(r'[0-9]+', character, line)

def remove_new_line(line):
    return line.replace("\n", "")

if __name__ == "__main__":
    main()