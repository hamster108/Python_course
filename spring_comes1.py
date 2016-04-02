#!/home/elizaveta/miniconda3/bin/python3
import argparse
import os.path
import os
import subprocess
##def change_image(x, y):
##    if os.path.isfile(x):
##        result = 'convert '+ str(x) + ' -resize ' + str(y) + '%'
##        print(subprocess.call(result, shell=True))
    
parser = argparse.ArgumentParser(description="Changes the picture's size ")
parser.add_argument("percent", type = int,
                     help="% of squeeze")
parser.add_argument("way", type = str,
                    help="path to image")
parser.add_argument("--new_way", type = str, default = ' ',
                    help="path to converted image")
args = parser.parse_args()


result = 'convert '+ str(args.way) + ' -resize ' + str(args.percent) + '%'
if args.percent:
    if os.path.isfile(args.way):
        if args.new_way:
            result += ' ' + str(args.new_way)
        result += str(args.way)
        print(subprocess.call(result, shell=True))
    elif os.path.isdir(args.way):
        for dir, dubdirs, files in os.walk(args.way):
            for name in files:
                filename = os.path.join(root, name)
                result = 'convert '+ filename + ' -resize ' + str(args.percent) + '%' + filename + '%'

    
    else:
        print('There is no image')
