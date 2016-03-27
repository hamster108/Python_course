#!/home/elizaveta/miniconda3/bin/python3
import argparse
import os.path
import shutil
import subprocess
parser = argparse.ArgumentParser()
parser.add_argument("command", choices=['store', 'diff'],
                     help="type of operation")
parser.add_argument("way", type = str,
                    help="path to file")
args = parser.parse_args()
old = args.way
new = args.way.split('/')[-1]
result = 'diff '+ '/home/elizaveta/sad/' + str(new) + ' ' + str(old)
if args.command == 'store':
    if os.path.isfile(args.way):
        shutil.copy(args.way, '/home/elizaveta/sad/')
        
elif args.command == 'diff':
    if os.path.isfile(args.way):
        print(subprocess.call(result, shell=True))

