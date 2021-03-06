# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division
import re

from string import hexdigits


ColorMap = {'aqua': '#00ffff',
            'black': '#000000',
            'blue': '#0000ff',
            'fuchsia': '#ff00ff',
            'gray': '#808080',
            'green': '#008000',
            'lime': '#00ff00',
            'maroon': '#800000',
            'navy': '#000080',
            'olive': '#808000',
            'purple': '#800080',
            'red': '#ff0000',
            'silver': '#c0c0c0',
            'teal': '#008080',
            'white': '#ffffff',
            'yellow': '#ffff00'}

# Could be better, but it works (trademark)
rgb_pattern = r'rgb\(\s*(\d|\d\d|1\d\d|2[0-4]\d|25[0-6])\s*,\s*(\d|\d\d|1\d\d|2[0-4]\d|25[0-6])\s*,\s*(\d|\d\d|1\d\d|2[0-4]\d|25[0-6])\)'

def map_color(color):
    if color is None:
        return None
    elif color.lower() in ColorMap:
        return ColorMap[color.lower()]
    elif isinstance(color, str):
      rgb_match = re.match(rgb_pattern.strip(), color)

      if len(color) and all(c in hexdigits for c in color):
        return '#%s' % color
      elif rgb_match:
        r = rgb_match.group(1)
        g = rgb_match.group(2)
        b = rgb_match.group(3)
        return '#%02x%02x%02x' % (int(r), int(g), int(b))

    return color
