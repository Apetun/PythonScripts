"""Batch convert images to greyscale.

Install dependencies:
  pip install pillow docopt

Note: If you do not provide an output path, the generated files will be saved
in a folder named "Converted"

Usage:
  greyscale.py <in_path> [<out_path>]
  greyscale.py -h | --help
  greyscale.py --version

Arguments:
  <in_path>   Input directory
  <out_path>  Output directory [default: ./Converted]

Options:
  -h, --help  Show this help screen.
  --version     Show version.
"""
import docopt
from PIL import Image
import glob
import os
import sys


def process_image(in_path, out_path):
    image = Image.open(in_path)
    grey = image.convert('L')
    grey.save(out_path)


def main(in_path, out_path):
    if not os.path.isdir(in_path):
        print('Error: <in_path> must be a directory', file=sys.stderr)
        return

    if out_path is None:
        dirname = os.path.dirname(in_path)
        out_path = dirname + '/Converted'

    if not os.path.exists(out_path):
        print('Creating directory', out_path)
        os.mkdir(out_path)

    for in_file in glob.glob(in_path + '/*'):
        filename = os.path.basename(in_file)
        _, ext = os.path.splitext(filename)

        if (not os.path.isfile(in_file) or
                ext[1:] not in ['jpg', 'jpeg', 'gif', 'png']):
            print('Skipping', filename)
            continue
        else:
            print('Processing', filename)

        out_file = out_path + '/' + filename
        process_image(in_file, out_file)


if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='Greyscale converter v1.0')
    main(args['<in_path>'], args['<out_path>'])
