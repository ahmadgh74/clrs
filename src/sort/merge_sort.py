def __merge(array, p, q, r):
    left = array[p:q + 1]
    right = array[q + 1:r + 1]
    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def __merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        __merge_sort(array, p, q)
        __merge_sort(array, q + 1, r)
        __merge(array, p, q, r)


def merge_sort(array):
    __merge_sort(array, 0, len(array))
    return array
