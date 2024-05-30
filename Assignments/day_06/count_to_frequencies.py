import sys
import csv
import os
from frequency_functions import total_rowSum, count_to_frequencies, row_total_sum

filename = sys.argv[1]
base_name = os.path.splitext(os.path.basename(filename))[0]
output_filename = f"{base_name}_frequencies.csv"


with open(filename) as csvfile:
    TNF_count = list(csv.DictReader(csvfile))
    
    total_rowSum(TNF_count)
    frequencies = count_to_frequencies(TNF_count, row_total_sum)


if frequencies:
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = frequencies[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in frequencies:
            writer.writerow(row)

print(f"Frequency saved to {output_filename}")