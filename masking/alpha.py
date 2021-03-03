def simple(current: float):
    result = current * 256
    return [0, 0, 0, result]


def lines(current: float):
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
