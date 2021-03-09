from args import args

import cv2
import numpy as np
import uuid

import actions as action

if __name__ == '__main__':
    file_name = args.output + str(uuid.uuid1()) + f'.{args.type}'
    img: np.ndarray
    if args.action == 'gen':
        try:
            img = action.generate(args)
            cv2.imwrite(file_name, img)
            print(f'Generated file: {file_name}')
        except cv2.error as e:
            print(f'Error occurred: \n{e}')
    elif args.action == 'edit':
        try:
            img = action.edit(args)
            cv2.imwrite(file_name, img)
            print(f'Generated file: {file_name}')
        except cv2.error as e:
            print(f'Error occurred: \n{e}')
