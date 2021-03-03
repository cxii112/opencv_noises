from args import args

import cv2
import numpy as np
import uuid
from tqdm import tqdm

import smooth
from utils import set_widgets
import masking
import noise


def image_from_noise(data: np.ndarray, coloring):
    result = []
    # widgets = set_widgets('Coloring', len(data))
    # with progressbar.ProgressBar(max_value=len(data), widgets=widgets) as bar:
    # bar_row = tqdm(range(len(data)), position=0, desc='Rows', ncols=80)
    # bar_col = tqdm(range(len(data[0])), position=1, desc='Cols', ncols=80, leave=False)
    # bar_row.update(0)
    # bar_col.update(0)
    for row in tqdm(range(0, len(data)), position=0, desc='Rows', ncols=80):
        # bar.update(row)
        temp = []
        for col in tqdm(range(0, len(data[row])), position=1, desc='Cols', ncols=80, leave=False):
            temp.append(coloring(data[row][col]))
            # bar_col.update()
        # bar_row.update()
        # bar_col.clear()
        result.append(temp)
    # bar_col.close()
    # bar_row.close()
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
