# NCBI taxonomy and nucleotide sequence 
- This tool can be used to get the full taxonomic profile & nucleotide sequence (gb format) for an organism of interest 

- to run the code you will need to provide the name of the organims of interes & your email (optional)

- To get a nucleotide sequence you will need to provide the name of the *species* 

- the code required modules can be install by running: 

    pip install -r requirements.txt

## Here's an example of how you can execute the code:

    get_taxo_sequence.py your_email@example.com organism_name 

or without providing an email:

    get_taxo_sequence.py X organism_name 

## Here' s an example of how the results look for Escherichia coli: 

    get_taxo_sequence.py X Escherichia coli

    Maximum Records Returned: 1
    ID List: ['561']
    Taxonomy Information for Escherichia:
    no rank: cellular organisms
    superkingdom: Bacteria
    phylum: Pseudomonadota
    class: Gammaproteobacteria
    order: Enterobacterales
    family: Enterobacteriaceae    

    GB data saved to sequence.gb


