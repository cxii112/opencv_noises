import progressbar
import numpy as np

from pb import set_widgets


def count_member(x, y, p: tuple):
    return p[0] * (x ** p[1]) * (y ** p[2]) * \
           ((x - 1) ** p[3]) * ((x + 1) ** p[4]) * ((x - 2) ** p[5]) * \
           ((y - 1) ** p[6]) * ((y + 1) ** p[7]) * ((y - 2) ** p[8])


def bicubic(data: np.ndarray, step: int = 10):
    result = data
    params = [
        (- 1 / 36, 1, 1, 1, 1, 0, 1, 0, 1),
        (1 / 12, 1, 0, 1, 1, 0, 1, 1, 0),
        (- 1 / 12, 1, 1, 1, 1, 0, 0, 1, 1),
        (1 / 36, 1, 1, 1, 1, 0, 1, 1, 0),

        (1 / 12, 1, 1, 0, 1, 1, 1, 0, 1),
        (- 1 / 4, 1, 0, 0, 1, 1, 1, 1, 1),
        (1 / 4, 1, 1, 0, 1, 1, 0, 1, 1),
        (- 1 / 12, 1, 1, 0, 1, 1, 1, 1, 0),

        (- 1 / 12, 0, 1, 1, 1, 1, 1, 0, 1),
        (1 / 4, 0, 0, 1, 1, 1, 1, 1, 1),
        (- 1 / 4, 0, 1, 1, 1, 1, 0, 1, 1),
        (1 / 12, 0, 1, 1, 1, 1, 1, 0, 1),

        (1 / 36, 1, 1, 1, 0, 1, 1, 0, 1),
        (- 1 / 12, 1, 0, 1, 0, 1, 1, 1, 1),
        (1 / 12, 1, 1, 1, 0, 1, 1, 1, 1),
        (- 1 / 36, 1, 1, 1, 0, 1, 1, 1, 0)
    ]

    row_points = (0, 0, 0, 0)
    if row_points[3] + step * 3 >= len(data):
        diff = (row_points[3] - len(data)) // 3
        row_points = (row_points[3],
                      row_points[3] + diff - 1,
                      row_points[3] + diff * 2 - 1,
                      len(data) - 1)
    else:
        row_points = (row_points[3],
                      row_points[3] + step - 1,
                      row_points[3] + (step * 2) - 1,
                      row_points[3] + (step * 3) - 1)

    widgets = set_widgets('Smoothing', len(data))
    with progressbar.ProgressBar(max_value=(len(data)), widgets=widgets) as bar:
        while row_points[-1] < len(data):
            col_points = (0, 0, 0, 0)
            if col_points[3] + step * 3 >= len(data):
                diff = (col_points[3] - len(data)) // 3
                col_points = (col_points[3],
                              col_points[3] + diff - 1,
                              col_points[3] + diff * 2 - 1,
                              len(data) - 1)
            else:
                col_points = (col_points[3],
                              col_points[3] + step - 1,
                              col_points[3] + (step * 2) - 1,
                              col_points[3] + (step * 3) - 1)
            while col_points[-1] < len(data[0]):
                row_shift = 0
                while row_points[0] + row_shift <= row_points[-1]:
                    col_shift = 0
                    bar.update(row_points[0] + row_shift)
                    while col_points[0] + col_shift <= col_points[-1]:
                        values = [
                            data[row_points[0]][col_points[0]],
                            data[row_points[0]][col_points[1]],
                            data[row_points[0]][col_points[2]],
                            data[row_points[0]][col_points[3]],

                            data[row_points[1]][col_points[0]],
                            data[row_points[1]][col_points[1]],
                            data[row_points[1]][col_points[2]],
                            data[row_points[1]][col_points[3]],

                            data[row_points[2]][col_points[0]],
                            data[row_points[2]][col_points[1]],
                            data[row_points[2]][col_points[2]],
                            data[row_points[2]][col_points[3]],

                            data[row_points[3]][col_points[0]],
                            data[row_points[3]][col_points[1]],
                            data[row_points[3]][col_points[2]],
                            data[row_points[3]][col_points[3]]
                        ]
                        result[row_points[0] + row_shift][col_points[0] + col_shift] = \
                            data[row_points[0] + row_shift][col_points[0] + col_shift]
                        row_match = (row_points[0] + row_shift == row_points[0] or
                                     row_points[0] + row_shift == row_points[1] or
                                     row_points[0] + row_shift == row_points[2] or
                                     row_points[0] + row_shift == row_points[3])
                        col_match = (col_points[0] + col_shift == col_points[1] or
                                     col_points[0] + col_shift == col_points[1] or
                                     col_points[0] + col_shift == col_points[2] or
                                     col_points[0] + col_shift == col_points[3])
                        if not (row_match and col_match):
                            for i in range(0, 16):
                                result[row_points[0] + row_shift][col_points[0] + col_shift] += count_member(
                                    col_shift / (step * 3 - 1),
                                    row_shift / (step * 3 - 1),
                                    params[i]
                                ) * values[i]
                        col_shift += 1
                    row_shift += 1
                if col_points[-1] == len(data[0]) - 1:
                    break
                if col_points[3] + step * 3 >= len(data):
                    diff = (col_points[3] - len(data)) // 3
                    col_points = (col_points[3],
                                  col_points[3] + diff - 1,
                                  col_points[3] + diff * 2 - 1,
                                  len(data) - 1)
                else:
                    col_points = (col_points[3],
                                  col_points[3] + step - 1,
                                  col_points[3] + (step * 2) - 1,
                                  col_points[3] + (step * 3) - 1)
            if row_points[-1] == len(data) - 1:
                break
            if row_points[3] + step * 3 >= len(data):
                diff = (row_points[3] - len(data)) // 3
                row_points = (row_points[3],
                              row_points[3] + diff - 1,
                              row_points[3] + diff * 2 - 1,
                              len(data) - 1)
            else:
                row_points = (row_points[3],
                              row_points[3] + step - 1,
                              row_points[3] + (step * 2) - 1,
                              row_points[3] + (step * 3) - 1)

    return result