import numpy as np

import smooth
import masking
import noise


def no_base(base):
    print(f'There are no base \'{base}\'')
    exit(0)


def no_effect(base, effect):
    print(f'There are no effect \'{effect}\' in \'{base}\'')
    exit(0)


def raw_image(width, height, steps):
    return smooth.cubic2(
        noise.simple(
            height // steps + 1,
            width // steps + 1),
        width, height)


def image_from_noise(data: np.ndarray, coloring):
    print('Coloring...')
    result = []
    for row in range(0, len(data)):
        temp = []
        for col in range(0, len(data[row])):
            temp.append(coloring(data[row][col]))
        result.append(temp)
    return np.array(result)


def generate(args):
    print('Generating new image')
    if args.base == 'alpha':
        if args.effect == 'simple':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.alpha.simple)
        elif args.effect == 'lines':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.alpha.lines)
        else:
            no_effect(args.base, args.effect)
    elif args.base == 'color':
        if args.effect == 'simple':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.color.simple)
        elif args.effect == 'levels':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.color.levels)
        else:
            no_effect(args.base, args.effect)
    elif args.base == 'grayscale':
        if args.effect == 'simple':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.simple)
        elif args.effect == 'simple-reverse':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.simple_reverse)
        elif args.effect == 'lines':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.lines)
        elif args.effect == 'lines-many':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.lines_many)
        elif args.effect == 'sin':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.sin)
        elif args.effect == 'log':
            return image_from_noise(raw_image(
                args.width, args.height, args.steps
            ), masking.grayscale.log)
        else:
            no_effect(args.base, args.effect)
    else:
        no_base(args.base)
