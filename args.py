import argparse
import os
from sys import platform


def dir_path(string):
    if os.path.isdir(string):
        if string[-1] != '/' and string[-1] != '\\':
            if platform.lower().find('win') != -1:
                string += '\\'
            else:
                string += '/'
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='Parse path to output image, type, image width and height')
parser.add_argument('out_path',
                    type=dir_path,
                    help='directory for output image')
parser.add_argument('action',
                    type=str,
                    choices=['gen', 'edit'],
                    help='defines mode')
parser.add_argument('-t', '--type',
                    type=str,
                    action='store',
                    dest='type',
                    choices=['jpg', 'png'],
                    help='set file type')
parser.add_argument('--width',
                    type=int,
                    action='store',
                    dest='width',
                    default=500,
                    help='set image width')
parser.add_argument('--height',
                    type=int,
                    action='store',
                    dest='height',
                    default=500,
                    help='set image height')
parser.add_argument('-s', '--steps',
                    type=int,
                    action='store',
                    required=True,
                    default=10,
                    dest='steps',
                    help='set steps in pixels for smoothing function')
args = parser.parse_args()
