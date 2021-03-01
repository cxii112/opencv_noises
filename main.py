import cv2
import numpy as np
import random
import uuid
import progressbar

import gen
from smooth import bilinear
from smooth import bicubic
from pb import set_widgets
from masking import grayscale


def raw_noise(height: int = 500, width: int = 500):
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

    noise = raw_noise(gen.args.height * 2, gen.args.width * 2)
    # noise = bilinear(noise, gen.args.step * 2)
    noise = bicubic(noise, gen.args.step * 2)
    noise = image_from_noise(noise, grayscale.lines)
    # noise = cv2.resize(noise, (gen.args.height * 2, gen.args.width * 2))
    # noise = image_from_noise(noise, grayscale_lines_masking)
    # noise = cv2.blur(noise, (15, 15))
    img = noise
    # img = cv2.resize(img, (gen.args.height, gen.args.width))
    # cv2.imshow(file_name, img)
    # cv2.waitKey(0)

    print(f'Generated file: {file_name}')
    cv2.imwrite(file_name, img)
