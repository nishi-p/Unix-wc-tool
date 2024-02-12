import sys
import os

# Print out the number of bytes in a file
def numberOfBytes(filename):
  if sys.argv[1] == "-c":
    print(os.path.getsize(filename), end = " ")
    print(filename)
  
# Print out the number of lines in a file
def numberOfLines(filename):
  if sys.argv[1] == "-l":
    with open(filename, "r", encoding = "utf8") as f:
      # f.readlines() reads the file in a single go and returns the lines of the files as list string elements
      print(len(f.readlines()), end = " ") 
    print(filename)
  
# Print out the number of words in a file
def numberOfWords(filename):
  if sys.argv[1] == "-w":
    with open(filename, "r", encoding = "utf8") as f:
      fileContent = f.read()
      wordList = fileContent.split()
      wordCount = len(wordList)
      print(wordCount, end = " ")
    print(filename)
  
# Print out the number of characters in a file
def numberOfCharacters(filename):
  if sys.argv[1] == "-m":
    with open(filename, "r", encoding = "utf8") as f:
      fileContentWordList = f.read().strip().split()
      charLen = sum(len(word) for word in fileContentWordList)
      print(charLen, end = " ")
    print(filename)
    

# Read from standard input if filename is not provided

def main():
  if sys.argv[1] not in ["-c", "-l", "-w", "-m"]:
    numberOfBytes(filename)
    numberOfLines(filename)
    numberOfWords(filename)
    numberOfCharacters(filename)
  else:
      filename = sys.argv[2]
      if sys.argv[1] == "-c":
        numberOfBytes(filename)
      elif sys.argv[1] == "-l":
        numberOfLines(filename)
      elif sys.argv[1] == "-w":
        numberOfWords(filename)
      elif sys.argv[1] == "-m":
        numberOfCharacters(filename)
        
if __name__ == "__main__":
  main()