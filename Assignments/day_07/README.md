# Get taxonomy and nucleotide sequence for organism of interest 

This tool can be used to get the full taxonomic profile & nucleotide sequence (gb format) for an organism of interest 

## Here's an example of how you can execute the code:

    get_taxo_sequence.py your_email@example.com organism_name 

or without providing an email:

    get_taxo_sequence.py *x* organism_name 

## Here' s an example of how the results look for Escherichia coli: 

    get_taxo_sequence.py your_email@example.com Escherichia coli

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


