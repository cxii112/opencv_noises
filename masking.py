import math


def simple_masking(current: float):
    if current > 0.9:
        return [0, 0, 0, 0]
    elif current > 0.7:
        return [0, 0, 0, 255]
    elif current > 0.5:
        return [0, 0, 0, 0]
    elif current > 0.3:
        return [0, 0, 0, 255]
    else:
        return [0, 0, 0, 0]


def colorful_masking(current: float):
    result: list
    if current > 0.5:
        result = [255, 0, 0, 255]
    elif current > 0.3:
        result = [0, 255, 0, 255]
    elif current > 0.1:
        result = [0, 0, 255, 255]
    else:
        result = [0, 0, 0, 255]
    return result


def grayscale_masking(current: float):
    result: list
    color = 255 * current
    result = [color, color, color, 255]
    return result


def grayscale_lines_masking(current: float):
    result = current * 50
    check_lines = [0.2, 0.5, 0.8]
    for value in check_lines:
        if abs(current - value) <= 0.025:
            result = (current + value) * 255
    return [result, result, result, 255]


def sin_coloring(current: float):
    result = int(abs(math.sin(current)) * 255)
    return [result, result, result, 255]


def log_coloring(current: float):
    result = int(abs(math.log10(current)) * 255)
    return [result, result, result, 255]

