def find_k_largest_vals(arr, k):
    print(find_k_largest_vals([5, 1, 3, 6, 8, 2, 4, 7], 3))
    arr.sort(reverse=True)
    return arr[:k]
