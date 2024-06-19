## Sequence analysis ## 

This tool finds the longest DNA duplicated sequence (and its length) & it calculates GC content of the sequence 

Identifying *Duplicated sequences* can be useful for different reasons: 

- Common during library preparations and can signal PCR biases- [more info](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/8%20Duplicate%20Sequences.html)

- Necesary for [phase-variation events](https://pubmed.ncbi.nlm.nih.gov/12624211/) 

[GC content](https://en.wikipedia.org/wiki/GC-content#:~:text=In%20molecular%20biology%20and%20genetics,) is the percentage of guanine (G) or cytosine (C) nucleotides within a sequence.Genes are often characterised by having a higher GC-content in contrast to the background GC-content for the entire genome. DNA with low GC-content is less stable than DNA with high GC-content.  


### USAGE 

1) Install dependencies 

```sh
pip install -r requirements.txt
```

**Input**: fasta or GeneBank files 

2) 
**Choose at least one analysis (both can be executed as well):**

--duplicate, -dp : finds the longest DNA duplicated sequence

--GC_content, -GC : calculates GC content of the sequence 

Run this code in the command line:
```sh 
python sequence_analysis.py --path file_path --duplicate --GC_content
```



