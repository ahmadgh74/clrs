import numpy as np


def _split(matrix, n):
    center = n // 2
    return matrix[:center, :center], matrix[:center, center:], matrix[center:, :center], matrix[center:, center:]


def _combine(m00, m01, m10, m11):
    return np.vstack([np.hstack([m00, m01]), np.hstack([m10, m11])])


def _square_matrix_multiply(matrix_a, matrix_b, n):
    if n == 1:
        return matrix_a * matrix_b
    else:
        new_n = n // 2
        a00, a01, a10, a11 = _split(matrix_a, n)
        b00, b01, b10, b11 = _split(matrix_b, n)

        p1 = _square_matrix_multiply(a00, b01 - b11, new_n)
        p2 = _square_matrix_multiply(a00 + a01, b11, new_n)
        p3 = _square_matrix_multiply(a10 + a11, b00, new_n)
        p4 = _square_matrix_multiply(a11, b10 - b00, new_n)
        p5 = _square_matrix_multiply(a00 + a11, b00 + b11, new_n)
        p6 = _square_matrix_multiply(a01 - a11, b10 + b11, new_n)
        p7 = _square_matrix_multiply(a00 - a10, b00 + b01, new_n)

        c00 = p5 + p4 - p2 + p6
        c01 = p1 + p2
        c10 = p3 + p4
        c11 = p1 + p5 - p3 - p7
        return _combine(c00, c01, c10, c11)


def square_matrix_multiply(matrix_a, matrix_b):
    return _square_matrix_multiply(matrix_a, matrix_b, len(matrix_a))
