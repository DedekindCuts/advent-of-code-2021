def count_increases(input_file, window: int = 1):
    with open(input_file, 'r') as reader:
        vals = [int(x) for x in reader.readlines()]
    totals = [sum(vals[i:i+window]) for i in range(len(vals)-window+1)]
    return sum([x[0]>x[1] for x in zip(totals, [float('Inf')]+totals[:-1])])

if __name__ == "__main__":
    assert count_increases('test_input.txt') == 7, 'Expected 7'
    print(f"Part 1: {count_increases('input.txt')}")
    assert count_increases('test_input.txt', window=3) == 5, 'Expected 5'
    print(f"Part 2: {count_increases('input.txt', window=3)}")
