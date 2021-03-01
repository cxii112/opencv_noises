import math as m


def simple(current: float):
    # result = ((current + 1) ** 3 * 1000) % 256
    result = current ** 2 * 255
    return [result, result, result, 255]


def lines(current: float):
    result = current * 50
    check_lines = [0.2, 0.5, 0.8]
    for value in check_lines:
        if abs(current - value) <= 0.025:
            result = (current + value) * 255
    return [result, result, result, 255]


def sin(current: float):
    result = int(abs(m.sin(current)) * 255)
    return [result, result, result, 255]


def log(current: float):
    result = int(abs(m.log10(current)) * 255)
    return [result, result, result, 255]