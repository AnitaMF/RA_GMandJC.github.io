import pytest
import csv
from frequency_functions import total_rowSum, count_to_frequencies

def test_rowSum():
    filename = "readCount_bacteria.csv"
    with open(filename) as csvfile:
        TNF_count = list(csv.DictReader(csvfile))
        result = total_rowSum(TNF_count)
        assert int(result[1]) == 1918347

