# Calculating frequencies from read counts 

This program processes a CSV file representing a table of read counts for various variables, such as bacteria or genes. Each row in the CSV file corresponds to a sample, and each column represents a different variable.

The program converts the counts of each variable within each sample into frequencies. It achieves this by first calculating the total count for each sample and then dividing each count by this total.

Finally, the program generates a new CSV file containing the updated table with frequencies instead of raw counts.

## Here's an example of how you can execute the code using the provided sample data:

    python count_to_frequencies.py readCount_bacteria.csv

## Here's an example of how can verify the results:

    pytest 