def breakline(column):
    for i in range (column):
        print '+----',

def normalline(column):
    for i in range (column):
    print '|    ',

def grid(row, column):
    effective_row= row/4
    rows_left= row-(row/4)

    for i in range(
