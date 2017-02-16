# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import six


_NotPassed = object()

def color(r_or_rgb, g=_NotPassed, b=_NotPassed):
    if isinstance(r_or_rgb, six.string_types):
        return r_or_rgb
    raise TODO("convert rgb to hex")
