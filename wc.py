#!/usr/bin/env python

import sys
import os


def operations(filename, op):
    if op == "-c":
        numberOfBytes(filename)
    elif op == "-l":
        numberOfLines(filename)
    elif op == "-w":
        numberOfWords(filename)
    elif op == "-m":
        numberOfCharacters(filename)
    print(filename)


# Print out the number of bytes in a file
def numberOfBytes(filename):
    print(os.path.getsize(filename), end=" ")


# Print out the number of lines in a file
def numberOfLines(filename):
    with open(filename, "r", encoding="utf8") as f:
        # f.readlines() reads the file in a single go and returns the lines of the files as
        # list string elements
        print(len(f.readlines()), end=" ")


# Print out the number of words in a file
def numberOfWords(filename):
    with open(filename, "r", encoding="utf8") as f:
        fileContent = f.read()
        wordList = fileContent.split()
        wordCount = len(wordList)
        print(wordCount, end=" ")


# Print out the number of characters in a file
def numberOfCharacters(filename):
    with open(filename, "r", encoding="utf8") as f:
        fileContentWordList = f.read().split()
        charLen = sum(len(word) for word in fileContentWordList)
        print(charLen, end=" ")

        """
        Count characters including whitespaces
        res = re.split(r'(\s)', fileRead)                        
        res = [x for x in res if x != '']
        print(len(res), end=" ")                       
        """


def main():
    try:
        if len(sys.argv) == 3:  # python wc.py -c/-l/-w/-m test.txt
            op = sys.argv[1]
            if "-" in op:
                filename = sys.argv[2]
                operations(filename, sys.argv[1])
            else:
                print("Incorrect syntax. "
                      "The command line argument should follow the syntax: python "
                      "<filename.py> -c/-l/-w/-m test.txt")
        else:
            if sys.argv[1] in ["-c", "-l", "-w", "-m"]:  # python wc.py -c/-l/-w/-m
                filename = input("Filename is missing. Enter the filename: ")
                operations(filename, sys.argv[1])
            else:  # python wc.py test.txt
                filename = sys.argv[1]
                numberOfBytes(filename)
                numberOfLines(filename)
                numberOfWords(filename)
                print(filename)
    except:
        print("An exception has occurred. "
              "The command line argument should follow the syntax: "
              "1. python <filename.py> -c/-l/-w/-m test.txt"
              "2. python <filename.py> test.txt"
              "3. python <filename.py> -c/-l/-w/-m")


if __name__ == "__main__":
    main()
