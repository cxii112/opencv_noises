import math as m


def simple(current: float):
    # result = ((current + 1) ** 3 * 1000) % 256
    result = abs(current) * 256
    return [result, result, result, 255]


def simple_reverse(current: float):
    # result = ((current + 1) ** 3 * 1000) % 256
    result = 256 - abs(current) * 256
    return [result, result, result, 255]


def lines(current: float):
    current = abs(current) % 1
    peaks = 10
    r = 5
    result = (m.sin(peaks * (current - (1 / peaks))) ** (2 * r)) * 255
    return [result, result, result, 255]


def lines_many(current: float):
    current = abs(current) % 1
    peaks = 60
    r = 5
    result = (m.sin(peaks * (current - (1 / peaks))) ** (2 * r)) * 255
    return [result, result, result, 255]


def sin(current: float):
    result = int(abs(m.sin(current)) * 255)
    return [result, result, result, 255]


def log(current: float):
    result = int(abs(m.log10(current)) * 255)
    return [result, result, result, 255]
