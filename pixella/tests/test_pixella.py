#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pixella
----------------------------------

Tests for `pixella` module.
"""

import pytest



from pixella import pixella


def test_downsample():
    downsampler = pixella.Downsampler()
    result = downsampler.downsample('brain.png')
    from PIL import Image
    assert result == Image.open('out.png')

def test_getpixels_getimages():
    downsampler = pixella.Downsampler()
    result = downsampler.get_pixels('wbrgb.png')
    desired_values = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
    assert result == desired_values
