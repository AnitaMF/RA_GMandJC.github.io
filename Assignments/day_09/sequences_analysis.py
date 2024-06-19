import argparse
import re 
from Bio import SeqIO

def open_file(path, file_type):
    sequence = ''
    for seq_record in SeqIO.parse(path, file_type):
        sequence = str(seq_record.seq)
    return sequence

def longest_duplicate(sequence):
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        match = re.search(regex, sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result, len(result)

def GC_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def main():
    parser = argparse.ArgumentParser(description= "analyze DNA sequences to find duplications and GC content")
    parser.add_argument('--path', help="path to fasta/GeneBank file", required=True)
    parser.add_argument('--duplicate', '-dp', action= "store_true", help= "Find the longest duplicated sequence")
    parser.add_argument('--GC_content', '-GC', action= "store_true", help= "Calculate GC content")
    args = parser.parse_args()

    if not args.duplicate and not args.GC_content:
        parser.error('No action requested, add --duplicate or --GC_content')

    path = args.path
    file_type = 'fasta' if path.endswith('.fasta') or path.endswith('.fa') else 'genbank'
    sequence = open_file(path, file_type)

    if args.duplicate:
        duplicate_sequence, duplicate_length = longest_duplicate(sequence)
        print(f'The longest duplicated sequence is: {duplicate_sequence} and its length is: {duplicate_length}')

    if args.GC_content:
        gc_content = GC_content(sequence)
        print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
