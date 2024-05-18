
import sys
import text_counts 

def main():
    if len(sys.argv) != 2: 
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]    
    with open(filename) as file: 
        text = file.read()

    num_ch = text_counts.count_ch(text)
    num_lines = text_counts.count_lines(text)
    num_words = text_counts.count_words(text)

    print(f"Number of characters: {num_ch}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")

main()