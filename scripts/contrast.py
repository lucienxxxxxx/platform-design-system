#!/usr/bin/env python3
"""Calculate contrast ratio of two opaque sRGB hex colors."""
import argparse
import re

def luminance(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise argparse.ArgumentTypeError('use opaque #RRGGBB colors')
    channels = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in channels]
    return sum(x * weight for x, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('foreground', type=luminance)
parser.add_argument('background', type=luminance)
args = parser.parse_args()
ratio = (max(args.foreground, args.background) + .05) / (min(args.foreground, args.background) + .05)
print(f'Contrast: {ratio:.2f}:1; normal text 4.5:1: {"pass" if ratio >= 4.5 else "fail"}; large text / applicable non-text 3:1: {"pass" if ratio >= 3 else "fail"}.')
print('Opaque pairs only; this does not assess actual rendering or full accessibility.')
