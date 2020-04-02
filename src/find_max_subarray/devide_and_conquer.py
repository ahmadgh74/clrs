def _find_max_crossing_subarray(array, low, mid, high):
    left_sum, sum_, max_left, max_right = float('-inf'), 0, mid, mid + 1
    for i in range(mid, low - 1, -1):
        sum_ += array[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum, sum_ = float('-inf'), 0

    for j in range(mid + 1, high + 1):
        sum_ += array[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    return max_left, max_right, left_sum + right_sum


def _find_max_subarray(array, low, high):
    if high == low:
        return low, high, array[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = _find_max_subarray(array, low, mid)
    right_low, right_high, right_sum = _find_max_subarray(array, mid + 1, high)
    cross_low, cross_high, cross_sum = _find_max_crossing_subarray(array, low, mid, high)
    if cross_sum <= left_sum >= right_sum:
        return left_low, left_high, left_sum
    elif cross_sum <= right_sum >= left_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum


def find_max_subarray(array):
    return _find_max_subarray(array, 0, len(array) - 1)
