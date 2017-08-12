#!/usr/bin/env python3

f = open('Data/portfolio.csv', 'r')
headers = next(f)       # Skip a single input
#print(f.read())

total = 0.0

print('{:>12s} {:>12s} {:>12s} {:>12s}'.format('Name','Date','Share','Price'))

for line in f:
    line = line.strip()
    part = line.split(',')
    part[0] = part[0].replace('"','')   #part[0] = part[0].strip('"')
    part[1] = part[1].replace('"','')
    part[2] = int(part[2])
    part[3] = float(part[3])
    total = part[2] + part[3]
    print('{:>12s} {:>12s} {:>12d} {:>12.2f}'.format(part[0], part[1], part[2], part[3]))
f.close()

print("\nTotal:",total)
