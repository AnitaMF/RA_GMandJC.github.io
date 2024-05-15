
import sys

def count_ch(text):
    return len(text)

def count_lines(text):
    return text.count('\n') + 1

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) != 2: 
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]    
    with open(filename) as file: 
        text = file.read()

    num_ch = count_ch(text)
    num_lines = count_lines(text)
    num_words = count_words(text)

    print(f"Number of characters: {num_ch}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")

main()