# -*- coding: utf-8 -*-
"""
Raw access to device. Only exposes .pixel() and .clear().
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

MAX_X = 320
MAX_Y = 240


def pixel(x, y, c):
    """
    pixel changes the color of pixel at x, y into c.

    :param x: X coordinate of pixel to be changed
    :param y: Y coordinate of pixel to be changed
    :param c: color to be changed to. Color must be constructued using
              canvator.color function().
    :return: Nothing

    Raises an exception if x or y are out of bound.
    """
    pass


def clear(c):
    """
    Clears the screen to given color.

    :param c: Color must be constructued using canvator.color function().
    :return: Nothing
    """
    pass
