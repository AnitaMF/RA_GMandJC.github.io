## Sequence analysis ## 

This tool finds the longest DNA duplicated sequence (and its length) & it calculates GC content of the sequence 

[GC content](https://en.wikipedia.org/wiki/GC-content#:~:text=In%20molecular%20biology%20and%20genetics,)%20or%20cytosine%20(C).) is the percentage of guanine (G) or cytosine (C) nucleotides within a sequence. Within a long region of genomic sequence, genes are often characterised by having a higher GC-content in contrast to the background GC-content for the entire genome. DNA with low GC-content is less stable than DNA with high GC-content.  


### USAGE 

**Input**: fasta or GeneBank files 

Choose at least one analysis (both can be executed as well): 
--duplicate, -dp : finds the longest DNA duplicated sequence
--GC_content, -GC : calculates GC content of the sequence 

Run this code in the command line:
```sh 
python sequence_analysis.py --path file_path --duplicate --GC_content
```



