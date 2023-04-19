def close_sum(a, b, t):
    a.sort()
    b.sort()

    min_difference = float('inf')
    result = []

    for x in a:
        i = binary_search(b, t - x)

        if i < len(b) and abs(x + b[i] - t) < min_difference:
            min_difference = abs(x + b[i] - t)
            result = [x, b[i]]

    return result
