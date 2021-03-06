#!/usr/bin/env python3
# port2.py

import csv

def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total shares*price for CSV file with name, date, shares, price data
    '''
    if errors not in {'warn', 'raise', 'silent'}:
        raise ValueError("error must be 'warn', 'silent', 'raise'")

    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)        # Skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno,'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise
                else:
                    pass
                continue    # Skip to the next row
            total += row[2] * row[3]
    return total

total = portfolio_cost('Data/missing.csv', errors='silent')
print("Total cost: ", total)
