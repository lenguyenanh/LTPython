def uniqueRows(input):
    input = map(tuple, input)
    result = set(input)
    for row in list(result):
        print(row)

if __name__ == "__main__":
    input = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]
    uniqueRows(input)
