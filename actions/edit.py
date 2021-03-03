import numpy as np
import noise
import smooth
import editing


def new_img(mask: np.ndarray, source: np.ndarray):
    print('Editing...')
    result = []
    for row in range(0, len(source)):
        temp = []
        for col in range(0, len(source[row])):
            temp.append(editing.rgb.levels_bmc(mask[row][col],
                                               source[row][col]))
        result.append(temp)
    return np.array(result)


def edit(source: np.ndarray, steps: int):
    print('Editing image')
    width = len(source[0])
    height = len(source)
    pix_per_step = min(height, width) // steps
    raw_noise = noise.simple(height // pix_per_step + 1,
                             width // pix_per_step + 1)
    mask = smooth.cubic2(raw_noise, width, height)
    img = new_img(mask, source)
    return img
