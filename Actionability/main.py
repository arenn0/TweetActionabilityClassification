

import csv
import sys
def loadDataset (dirName)
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count += 1
        else:
            print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print('Processed {line_count} lines.')

