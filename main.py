import cv2
import numpy as np
import random
import uuid
import progressbar
import math

import gen


def set_widgets(message: str, max_value: int):
    widgets = [
        f'{message}...',
        ' (', progressbar.Counter(), f'/{max_value}) ',
        progressbar.Bar(left='[', right=']'),
        progressbar.ETA()
    ]
    return widgets


def linear_interpolation(f0: float, f1: float, x0: int, x1: int, x: int) -> float:
    return f0 + ((f1 - f0) / (x1 - x0)) * (x - x0)


def bilinear_interpolation(fx0y0: float, fx1y0: float, fx0y1: float, fx1y1: float,
                           x0: int, x1: int, y0: int, y1: int,
                           x: int, y: int):
    return linear_interpolation(
        linear_interpolation(fx0y0, fx1y0, x0, x1, x),
        linear_interpolation(fx0y1, fx1y1, x0, x1, x),
        y0, y1, y
    )


def gen_raw_noise(height: int = 500, width: int = 500):
    result = []
    widgets = set_widgets('Generating noise', height)
    with progressbar.ProgressBar(max_value=height, widgets=widgets) as bar:
        for row in range(0, height):
            bar.update(row)
            temp = []
            for col in range(0, width):
                temp.append(random.random())
            result.append(temp)
    return np.array(result)


def double_linear_smoothing(data: np.ndarray, step: int = 10):
    widgets = set_widgets('Smoothing', len(data[0]) + len(data))
    with progressbar.ProgressBar(max_value=(len(data[0]) + len(data)), widgets=widgets) as bar:
        for row in range(0, len(data)):
            bar.update(row)
            start = 0
            end = step - 1
            while end < len(data[row]):
                shift = 1
                while start + shift < end:
                    data[row][start + shift] = linear_interpolation(
                        data[row][start], data[row][end], start, end, start + shift)
                    shift += 1
                start = end
                if end + step - 1 < len(data[row]):
                    end += step - 1
                else:
                    if len(data[row]) - 1 == end:
                        break
                    end = len(data[row]) - 1

        for col in range(0, len(data[0])):
            bar.update(len(data) + col)
            start = 0
            end = step - 1
            while end < len(data):
                shift = 1
                while start + shift < end:
                    data[start + shift][col] = linear_interpolation(
                        data[start][col], data[end][col], start, end, start + shift)
                    shift += 1
                start = end
                if end + step - 1 < len(data):
                    end += step - 1
                else:
                    if len(data) - 1 == end:
                        break
                    end = len(data) - 1
    return data


def bilinear_smoothing(data: np.ndarray, step: int = 10):
    result = data
    widgets = set_widgets('Smoothing', len(data))
    with progressbar.ProgressBar(max_value=(len(data)), widgets=widgets) as bar:
        start_row = 0
        end_row = step - 1
        while end_row < len(data):
            start_col = 0
            end_col = step
            while end_col < len(data[0]):
                shift_row = 0
                while start_row + shift_row <= end_row:
                    shift_col = 0
                    while start_col + shift_col <= end_col:
                        result[start_row + shift_row][start_col + shift_col] = bilinear_interpolation(
                            data[start_row][start_col],
                            data[start_row][end_col],
                            data[end_row][start_col],
                            data[end_row][end_col],
                            start_col,
                            end_col,
                            start_row,
                            end_row,
                            start_col + shift_col,
                            start_row + shift_row
                        )
                        shift_col += 1
                    shift_row += 1
                start_col = end_col
                if end_col + step < len(data[0]):
                    end_col += step - 1
                else:
                    if end_col == len(data[0]) - 1:
                        break
                    end_col = len(data[0]) - 1
            start_row = end_row
            if end_row + step < len(data):
                end_row += step - 1
            else:
                if end_row == len(data) - 1:
                    break
                end_row = len(data) - 1
            bar.update(end_row)
    return result


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
    pass


def sin_coloring(current: float):
    result = int(abs(math.sin(current)) * 255)
    return [result, result, result, 255]


def log_coloring(current: float):
    result = int(abs(math.log10(current)) * 255)
    return [result, result, result, 255]


def image_from_noise(data: np.ndarray, coloring):
    result = []
    widgets = set_widgets('Coloring', len(data))
    with progressbar.ProgressBar(max_value=len(data), widgets=widgets) as bar:
        for row in range(0, len(data)):
            bar.update(row)
            temp = []
            for col in range(0, len(data[row])):
                temp.append(coloring(data[row][col]))
            result.append(temp)
    return np.array(result)


if __name__ == '__main__':
    file_name = gen.args.out_path + str(uuid.uuid1()) + f'.{gen.args.type}'
    print(
        f"""Settings:
    size: {gen.args.height}x{gen.args.width}
    step: {gen.args.step}
    outfile: {file_name}""")

    noise = gen_raw_noise(gen.args.height, gen.args.width)
    # noise = double_linear_smoothing(noise, gen.args.step)
    noise = bilinear_smoothing(noise, gen.args.step)
    noise = image_from_noise(noise, grayscale_lines_masking)

    img = noise

    print(f'Generated file: {file_name}')
    cv2.imwrite(file_name, img)
