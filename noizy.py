from args import args

import cv2
import numpy as np
import uuid

import actions as action

if __name__ == '__main__':
    file_name = args.output + str(uuid.uuid1()) + f'.{args.type}'
    img: np.ndarray
    if args.action == 'gen':
        img = action.generate(args.width, args.height, args.steps)
        cv2.imwrite(file_name, img)
        print(f'Generated file: {file_name}')
    elif args.action == 'edit':
        source_img = cv2.imread(args.input)
        print(f'Open: {args.input}')
        img = action.edit(source_img, args.steps)
        cv2.imwrite(file_name, img)
        print(f'Generated file: {file_name}')
