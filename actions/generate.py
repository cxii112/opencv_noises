import numpy as np

import smooth
import masking
import noise


def image_from_noise(data: np.ndarray, coloring):
    print('Coloring...')
    result = []
    for row in range(0, len(data)):
        temp = []
        for col in range(0, len(data[row])):
            temp.append(coloring(data[row][col]))
        result.append(temp)
    return np.array(result)


def generate(width, height, steps):
    print('Generating new image')
    raw_noise = noise.simple(height // steps + 1,
                             width // steps + 1)
    raw_image = smooth.cubic2(raw_noise, width, height)
    img = image_from_noise(raw_image, masking.grayscale.gauss_lines)
    return img
