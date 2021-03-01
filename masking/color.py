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
