#!/usr/bin/env python3
"""Copy editable system templates and gallery into a new directory."""
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('destination', type=Path, help='New output directory; must not exist')
args = parser.parse_args()
source = Path(__file__).resolve().parent.parent / 'assets'
destination = args.destination.resolve()
if destination.exists():
    parser.error(f'destination already exists: {destination}')
if source == destination or source in destination.parents:
    parser.error('destination must be outside the skill assets directory')
destination.mkdir(parents=True)
shutil.copytree(source / 'templates', destination / 'templates')
shutil.copytree(source / 'starter', destination / 'preview')
print(f'Created {destination}. Open preview/index.html in a browser.')
