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
    result = current * 50
    check_lines = [0.2, 0.5, 0.8]
    for value in check_lines:
        if abs(current - value) <= 0.025:
            result = (current + value) * 255
    return [result, result, result, 255]


def gauss_lines(current: float):
    current = abs(current) % 1
    result = current * 20
    r = 200
    k = 5.01310
    if 0 <= current < (1/3):
        result = (m.exp(-((current - (1/6)) ** 2) / 2)) / (m.sqrt(2 * m.pi))
    elif (1/3) <= current < (2/3):
        result = (m.exp(-((current - 0.5) ** 2)) / 2) / (m.sqrt(2 * m.pi))
    elif (2/3) <= current <= 1:
        result = (m.exp(-((current - (2/3 + 1/6)) ** 2)) / 2) / (m.sqrt(2 * m.pi))
    result = (result * k) ** r * 255
    return [result, result, result, 255]


def sin(current: float):
    result = int(abs(m.sin(current)) * 255)
    return [result, result, result, 255]


def log(current: float):
    result = int(abs(m.log10(current)) * 255)
    return [result, result, result, 255]