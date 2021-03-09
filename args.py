import argparse
import os
from sys import platform
from settings import PROG_NAME


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


def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)


parser = argparse.ArgumentParser(prog=f'{PROG_NAME}.py',
                                 description='Application for generate or editing images using noise')
parser.epilog = f'Run {PROG_NAME}.py <action> -h to see more details'
subparsers = parser.add_subparsers(title='You can use next commands',
                                   dest='action')

generate = subparsers.add_parser('gen', help='App will generate new image from noise')
generate.add_argument('base',
                      type=str,
                      action='store',
                      choices=['alpha', 'color', 'grayscale'],
                      help='set group of color masks')
generate.add_argument('effect',
                      type=str,
                      action='store',
                      choices=['simple',
                               'lines',
                               'levels',
                               'simple-reverse',
                               'lines-many',
                               'sin',
                               'log'],
                      help='set effect')
generate.add_argument('output',
                      type=dir_path,
                      help='output image directory')
generate.add_argument('--width',
                      type=int,
                      action='store',
                      dest='width',
                      default=500,
                      help='set image width')
generate.add_argument('--height',
                      type=int,
                      action='store',
                      dest='height',
                      default=500,
                      help='set image height')
generate.add_argument('-s', '--steps',
                      type=int,
                      action='store',
                      required=True,
                      default=10,
                      dest='steps',
                      help='set steps in pixels for interpolation function')
generate.add_argument('-t', '--type',
                      type=str,
                      action='store',
                      dest='type',
                      choices=['jpg', 'png'],
                      help='set file type')

edit = subparsers.add_parser('edit', help='App will editing existing image')
edit.add_argument('base',
                  type=str,
                  action='store',
                  choices=['channels'],
                  help='set group of color masks')
edit.add_argument('effect',
                  type=str,
                  action='store',
                  choices=['levels-rgb',
                           'levels-ymc',
                           'levels-bmc'],
                  help='set effect')
edit.add_argument('input',
                  type=file_path,
                  help='input file name')
edit.add_argument('output',
                  type=dir_path,
                  help='directory for output image')
edit.add_argument('-s', '--steps',
                  type=int,
                  action='store',
                  required=True,
                  default=10,
                  dest='steps',
                  help='set steps in pixels for smoothing function')
edit.add_argument('-t', '--type',
                  type=str,
                  action='store',
                  dest='type',
                  choices=['jpg', 'png'],
                  help='set file type')

args = parser.parse_args()
