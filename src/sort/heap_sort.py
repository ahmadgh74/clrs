def _left(i):
    return 2 * i + 1


def _right(i):
    return 2 * i + 2


def _max_heapify(array, i, array_len):
    left_index = _left(i)
    right_index = _right(i)
    if left_index < array_len and array[left_index] > array[i]:
        largest = left_index
    else:
        largest = i
    if right_index < array_len and array[right_index] > array[largest]:
        largest = right_index

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        _max_heapify(array, largest, array_len)


def heap_sort(array):
    array_len = len(array)

    for x in range(array_len // 2 - 1, -1, -1):
        _max_heapify(array, x, array_len)

    for x in range(array_len - 1, -1, -1):
        array[0], array[x] = array[x], array[0]
        _max_heapify(array, 0, x)
    return array
