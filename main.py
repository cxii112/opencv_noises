from args import args

import cv2
import numpy as np
import uuid

# from actions.generate import generate
import actions as action
import masking


def image_from_noise(data: np.ndarray, coloring):
    print('Coloring...')
    result = []
    for row in range(0, len(data)):
        temp = []
        for col in range(0, len(data[row])):
            temp.append(coloring(data[row][col]))
        result.append(temp)
    return np.array(result)


if __name__ == '__main__':
    file_name = args.out_path + str(uuid.uuid1()) + f'.{args.type}'
    print(
        f"""Settings:
    action: {args.action}
    size: {args.height}x{args.width}
    step: {args.steps}
    outfile: {file_name}""")
    raw_img = None
    if args.action == 'gen':
        raw_img = action.generate(args.width, args.heigth, args.steps)
    if raw_img:
        img = image_from_noise(raw_img, masking.grayscale.gauss_lines)
        cv2.imwrite(file_name, img)

    print(f'Generated file: {file_name}')
