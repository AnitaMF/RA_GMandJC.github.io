import sys
from functions_entrez import get_full_taxonomy_info, download_nucleotide
from Bio import Entrez

def main():
    # Get input from user
    if len(sys.argv) > 1:
        user_email = sys.argv[1]
    else:
        user_email = input("Please enter your email address (or type 'X' to skip): ")

    if len(sys.argv) > 2:
        user_bacteria = sys.argv[2]
    else:
        user_bacteria = input("Please enter the name of the bacteria: ")
#email is optional 
    if user_email.lower() != 'x':
        Entrez.email = user_email

    bacteria = user_bacteria

    tax_infos = get_full_taxonomy_info(bacteria)
    for tax_info in tax_infos:
        print(f"Taxonomy Information for {bacteria}:")
        for rank, name in tax_info.items():
            print(f"{rank}: {name}")
        print()

    # Download nucleotide FASTA for the given bacteria
    download_nucleotide(bacteria)

if __name__ == "__main__":
    main()
