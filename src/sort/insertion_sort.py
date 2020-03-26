<<<<<<< HEAD:src/sort/insertion_sort.py
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i + 1] = key

    return array
=======
>>>>>>> bab410c96886ceb91a3d142b1de3fab8cd22e8b3:sort/insertion_sort.py
