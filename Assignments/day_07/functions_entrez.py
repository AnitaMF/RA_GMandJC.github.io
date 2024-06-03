from Bio import Entrez

def get_full_taxonomy_info(bacteria):
    # Search for taxonomy IDs
    handle = Entrez.esearch(db="taxonomy", term=bacteria, retmax=30)
    record = Entrez.read(handle)
    handle.close()
    
    ret_max = record.get('RetMax', '0')
    id_list = record.get('IdList', [])
    
    print(f"Maximum Records Returned: {ret_max}")
    print(f"ID List: {id_list}")

    if not id_list:
        print("No taxonomy found.")
        return []
    
    tax_infos = []
    for tax_id in id_list:
        handle = Entrez.efetch(db="taxonomy", id=tax_id, retmode="xml")
        record = Entrez.read(handle)
        handle.close()
        
        # Extract full taxonomy
        tax_info = {}
        for entry in record[0]['LineageEx']:
            tax_info[entry['Rank']] = entry['ScientificName']
        
        tax_infos.append(tax_info)
    
    return tax_infos

def download_nucleotide(bacteria, filename="sequence.gb"):
    handle = Entrez.esearch(db="nucleotide", term=bacteria, rettype="gb", idtype= "acc", retmax=1)
    record = Entrez.read(handle)
    count = int(record.get('Count', '0'))
    handle.close()
    
    if count > 0:
        nucleotide_id = record["IdList"][0]
        handle = Entrez.efetch(db="nucleotide", id=nucleotide_id, rettype="gb", retmode="text")
        gb_data = handle.read()
        handle.close()
        
        with open(filename, "w") as file:
            file.write(gb_data)
        
        print(f"GB data saved to {filename}")
    else:
        print("No nucleotide records found for the specified bacteria.")
