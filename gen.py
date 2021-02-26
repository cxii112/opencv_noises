import argparse
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='Parse path to output image, type, image width and height.')
parser.add_argument('out_path',
                    type=dir_path,
                    help='directory for output image.')
parser.add_argument('-t', '--type',
                    type=str,
                    action='store',
                    dest='type',
                    choices=['jpg', 'png'],
                    help='set file type.')
parser.add_argument('--width',
                    type=int,
                    action='store',
                    dest='width',
                    default=500,
                    help='set image width.')
parser.add_argument('--height',
                    type=int,
                    action='store',
                    dest='height',
                    default=500,
                    help='set image height.')
parser.add_argument('-s', '--step',
                    type=int,
                    action='store',
                    required=True,
                    default=10,
                    dest='step',
                    help='set step in pixels for smoothing function.')
args = parser.parse_args()
