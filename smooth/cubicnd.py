import numpy as np


def set_points(default: tuple, step: int, max_len: int) -> tuple:
    result = default
    if result[0] + (step * 3) >= max_len:
        diff = max_len - result[3] // 3
        result = (
            result[3],
            result[3] + diff,
            result[3] + (diff * 2),
            max_len - 1
        )
    else:
        result = (
            result[3],
            result[3] + step,
            result[3] + (step * 2),
            result[3] + (step * 3)
        )
    return result


def interpolate(x: float, f: tuple) -> float:
    a = -0.5 * f[0] + 1.5 * f[1] - 1.5 * f[2] + 0.5 * f[3]
    b = f[0] - 2.5 * f[1] + 2 * f[2] - 0.5 * f[3]
    c = -0.5 * f[0] + 0.5 * f[2]
    d = f[1]
    return a * x ** 3 + b * x ** 2 + c * x + d


def cubic1(data: np.ndarray, step: int = 10) -> np.ndarray:
    result = data
    max_len = len(data)
    points = set_points((0, 0, 0, 0), step, max_len)
    while points[3] < max_len:
        shift = 0
        while shift <= step * 3:
            # x = (shift - (points[1] - points[0])) / (points[1] - points[0])
            x = (shift - (points[1] - points[0])) / step
            f = tuple(data[points[i]] for i in range(0, 4))
            if (shift + points[0] != points[0] and
                    shift + points[0] != points[1] and
                    shift + points[0] != points[2] and
                    shift + points[0] != points[3]):
                result[points[0] + shift] = interpolate(x, f)
            shift += 1
        if points[3] == max_len - 1:
            break
        points = set_points(points, step, max_len)
    return result


def cubic2(data: np.ndarray, step: int = 10) -> np.ndarray:
    result = data
    # points = set_points((0, 0, 0, 0), step, len(data))
    rows = len(data)
    cols = len(data[0])
    row = 0
    while row < rows:
        temp = np.array([data[row][i] for i in range(0, cols)])
        temp = cubic1(
            temp,
            step
        )
        for col in range(0, cols):
            result[row][col] = temp[col]
        if row == rows - 1:
            break
        if row + step > rows:
            row = rows - 1
        else:
            row += step
    for col in range(0, cols):
        temp = np.array([data[i][col] for i in range(0, rows)])
        temp = cubic1(
            temp,
            step
        )
        for row in range(0, rows):
            result[row][col] = temp[row]
    return result
