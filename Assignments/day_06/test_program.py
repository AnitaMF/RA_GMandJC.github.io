import csv
import pytest
import sys

def check_row_sums(filename):
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile)
        next(csvreader)  
        
        row_sums = []
        for row in csvreader:
            row_sum = sum(float(value) for key, value in row.items() if key != 'id')
            row_sums.append(row_sum)
    
    assert all(0.9 <= row_sum <= 1 for row_sum in row_sums), "Calculation failed: Not all row sums are in the range of 0.9 to 1."
    print("Calculation was successful: All row sums are in the range of 0.9 to 1.")

def test_check_row_sums():
    filename = "readCount_bacteria_frequencies.csv"
    check_row_sums(filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the CSV filename as an argument.")
    else:
        filename = sys.argv[1]
        check_row_sums(filename)
