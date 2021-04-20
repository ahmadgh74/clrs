def find_max_subarray_bf(array):
    left_index = 0
    right_index = len(array) - 1
    sum_ = float('-inf')
    array_len = len(array)
    for li in range(0, array_len):
        for ri in range(li + 1, array_len + 1):
            tmp_sum = sum(array[li:ri])
            if tmp_sum >= sum_:
                sum_ = tmp_sum
                left_index = li
                right_index = ri

    return left_index, right_index - 1, sum_
