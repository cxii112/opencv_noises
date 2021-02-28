import cv2
import numpy as np
import random
import uuid
import progressbar

import gen
from smoothing import bilinear_smoothing
from pb import set_widgets
from masking import grayscale_lines_masking
from masking import simple_masking


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
    # noise = double_linear_smoothing(noise, gen.args.step)
    # noise = bilinear_smoothing(noise, gen.args.step * 2)
    noise = image_from_noise(noise, simple_masking)
    noise = cv2.resize(noise, (gen.args.height * 2, gen.args.width * 2), interpolation=cv2.INTER_LANCZOS4)
    # noise = image_from_noise(noise, grayscale_lines_masking)
    # noise = cv2.blur(noise, (15, 15))
    img = noise
    # img = cv2.resize(noise, (gen.args.height, gen.args.width))
    # cv2.imshow(file_name, img)
    # cv2.waitKey(0)

    print(f'Generated file: {file_name}')
    cv2.imwrite(file_name, img)
