import cv2
import numpy as np
import uuid
import progressbar

from args import args
import smooth
from utils import set_widgets
from masking import grayscale
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
    step: {args.step}
    outfile: {file_name}""")

    noise = noise.simple(args.height, args.width)
    # noise = smooth.bicubic(noise, args.step * 2)
    print('Smoothing')
    noise = smooth.cubic2(noise, args.step)
    noise = image_from_noise(noise, grayscale.simple)
    # noise = cv2.blur(noise, (15, 15))
    img = noise
    # img = cv2.resize(img, (args.height, args.width))

    print(f'Generated file: {file_name}')
    cv2.imwrite(file_name, img)
