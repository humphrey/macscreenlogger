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


started_at = time.localtime()
directory = PurePath.joinpath(args.basedir, time.strftime("%Y-%m-%d"))
prefix = f'{time.strftime("%Y%m%d")}'

Path(directory).mkdir(parents=True, exist_ok=True)


region = args.region or '-10000,-10000,20000,20000'

# prev_mins = None

while True:

  minutes = time.localtime().tm_hour * 60 +  time.localtime().tm_min
  output_file = f'{directory}/{prefix}_{str(minutes).rjust(5, "0")}.jpg'

  if Path(output_file).exists():
    time.sleep(30)
    continue
    
  cmd = [
    'screencapture',              # MacOS provided command which takes screenshots
    '-x',                         # Do not make sound
    '-R', region,                 # Capture my entire multi-screen area.  This also downscales the retina screen
    '-t', 'jpg',                  # JPG to make files smaller
    f'{directory}/{prefix}_{str(minutes).rjust(5, "0")}.jpg',     # Filename
  ]
  print(' '.join(cmd))
  subprocess.run(cmd)
