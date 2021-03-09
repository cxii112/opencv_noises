def simple(current: float):
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


def levels(current: float):
    result: list = [0, 0, 0, 255]
    if abs(current) < 0.5:
        result = [255, 0, 255, 255]
    if 1 / 3 <= abs(current) < 0.75:
        result = [0, 255, 255, 255]
    if 0.5 <= abs(current):
        result = [255, 255, 0, 255]
    return result
