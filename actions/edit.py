import numpy as np
import cv2
import noise
import smooth
import editing


def no_base(base):
    print(f'There are no base \'{base}\'')
    exit(0)


def no_effect(base, effect):
    print(f'There are no effect \'{effect}\' in \'{base}\'')
    exit(0)


def new_img(mask: np.ndarray, source: np.ndarray, base, effect):
    print('Editing...')
    result = []
    if base == 'channels':
        if effect == 'levels-rgb':
            for row in range(0, len(source)):
                temp = []
                for col in range(0, len(source[row])):
                    temp.append(editing.channels.levels_rgb(mask[row][col],
                                                            source[row][col]))
                result.append(temp)
            return np.array(result)
        elif effect == 'levels-ymc':
            for row in range(0, len(source)):
                temp = []
                for col in range(0, len(source[row])):
                    temp.append(editing.channels.levels_ymc(mask[row][col],
                                                            source[row][col]))
                result.append(temp)
            return np.array(result)
        elif effect == 'levels-bmc':
            for row in range(0, len(source)):
                temp = []
                for col in range(0, len(source[row])):
                    temp.append(editing.channels.levels_bmc(mask[row][col],
                                                            source[row][col]))
                result.append(temp)
            return np.array(result)
        else:
            no_effect(base, effect)
    else:
        no_base(base)


def edit(args):
    print('Editing image')
    source = cv2.imread(args.input)
    width = len(source[0])
    height = len(source)
    pix_per_step = min(height, width) // args.steps
    return new_img(smooth.cubic2(
        noise.simple(height // pix_per_step + 1,
                     width // pix_per_step + 1),
        width, height),
        source,
        args.base, args.effect)
