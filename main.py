from args import args

import cv2
import numpy as np
import uuid
import progressbar

import smooth
from utils import set_widgets
import masking
import noise


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
    file_name = args.out_path + str(uuid.uuid1()) + f'.{args.type}'
    print(
        f"""Settings:
    size: {args.height}x{args.width}
    step: {args.steps}
    outfile: {file_name}""")

    noise = noise.simple(args.height // args.steps + 1,
                         args.width // args.steps + 1)
    print('Smoothing')
    raw_image = smooth.cubic2(noise, args.width, args.height)
    img = image_from_noise(raw_image, masking.grayscale.gauss_lines)

    cv2.imwrite(file_name, img)
    print(f'Generated file: {file_name}')
