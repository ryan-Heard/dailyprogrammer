import pprint
pp = pprint.PrettyPrinter(indent=4)

def data_format():
    grids = []
    tmp_grid  = []

    with open('grids.txt') as file:
        for line in file:
            if 'Grid' in line:
                if len(tmp_grid) > 0:
                    grids.append(tmp_grid)
                    tmp_grid = []
            else:
                line = line.strip().rstrip().split()
                if len(line) > 0:
                    tmp_grid.append(line)

    return grids

def target_diagonal_value(arr):
    n = len(arr[0]);

    return n*((n*n)+1)/2

def get_diagonal_value(arr):
    n = len(arr[0])
    total = 0

    for pos in range(0, n):
        total += int(arr[pos][pos])

    return total

def diagonal_scan(arr):
    targeted = []

    for i in range(0,len(arr)):
        targeted.append(0);


data = data_format()

for i in data:
    print(get_diagonal_value(i))
