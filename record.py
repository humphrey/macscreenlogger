#!/usr/bin/python3

import time
import subprocess
from pathlib import Path, PurePath
import argparse
import sys


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('basedir', type=PurePath)
parser.add_argument('--region', nargs="?", type=str, help='X,Y,W,H')
args = parser.parse_args()

region = args.region or '-10000,-10000,20000,20000'


def get_output_file(mkdir=True):
  now = time.localtime()
  directory = PurePath.joinpath(args.basedir, time.strftime("%Y-%m-%d", now))
  if mkdir:
    Path(directory).mkdir(parents=True, exist_ok=True)
  minutes = now.tm_hour * 60 + now.tm_min
  return f'{directory}/{time.strftime("%Y%m%d", now)}_{str(minutes).rjust(5, "0")}.jpg'


while True:
  output_file = get_output_file()

  if Path(output_file).exists():
    time.sleep(30)
    continue
    
  cmd = [
    'screencapture',              # MacOS provided command which takes screenshots
    '-x',                         # Do not make sound
    '-R', region,                 # Capture my entire multi-screen area.  This also downscales the retina screen
    '-t', 'jpg',                  # JPG to make files smaller
    output_file,     # Filename
  ]
  print(' '.join(cmd))
  subprocess.run(cmd)
