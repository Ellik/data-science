def get_median(sequence):
    prep_sequence = sorted(sequence)
    median_index = int(len(prep_sequence) / 2)
    if len(prep_sequence) % 2 == 0:
        print(prep_sequence[median_index - 1])
        print(prep_sequence[median_index])
        return int((prep_sequence[median_index - 1] + prep_sequence[median_index]) / 2)
    return prep_sequence[median_index]


print(get_median([5, 2, 1, 3, 4]))
print(get_median([3, 3, 7, 9]))
