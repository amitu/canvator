# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


import canvator as c
from canvator import raw


def main():
    c.local()
    print("c.local()")
    c.clear(c.color("white"))
    raw.pixel(1, 1, c.color("red"))
    c.wait()


if __name__ == "__main__":
    main()
