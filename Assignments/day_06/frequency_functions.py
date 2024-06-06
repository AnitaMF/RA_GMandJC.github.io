import csv

row_total_sum = []

def total_rowSum(TNF_count):
    for row in TNF_count:
        curr_row_sum = sum(float(value) for value in row.values() if value)
        row_total_sum.append(curr_row_sum)
    return row_total_sum

def count_to_frequencies(TNF_count, row_total_sum):
    frequencies = []
    for i, row in enumerate(TNF_count):
        if i < len(row_total_sum):
            row_sum = row_total_sum[i]
            if row_sum != 0:
                frequencies.append({key: float(value)/row_sum if value else 0 for key, value in row.items()})
    return frequencies 

