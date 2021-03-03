import numpy as np
from scipy.interpolate import CubicSpline


def cubic1(noise: np.ndarray, dest_len: int) -> np.ndarray:
    max_len = len(noise)
    x0 = np.linspace(0, dest_len - 1, max_len)
    y0 = noise
    xs = np.linspace(0, dest_len - 1, dest_len)
    f = CubicSpline(x0, y0, bc_type='natural')
    result = np.array([f(i) for i in xs])
    return result


def cubic2(noise: np.ndarray, width: int, height: int) -> np.ndarray:
    rows = []
    for row in noise:
        rows.append(cubic1(row, width))
    rows = np.array(rows)
    result = []
    rows = np.rot90(rows, 1)
    for row in rows:
        result.append(cubic1(row, height))
    result = np.array(result)
    result = np.rot90(result, -1)
    return result
