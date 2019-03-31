#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pixella
----------------------------------

Tests for `pixella` module.
"""

import pytest



from pixella import pixella


def test_downsample_brain():
    downsampler = pixella.Downsampler('brain.png')
    result = downsampler.downsample()
    from PIL import Image
    assert result == Image.open('out.png')


def test_get_pixels_as_rows():
    downsampler = pixella.Downsampler('wbrgb.png')
    result = downsampler.get_pixels_as_rows()
    desired_values = [[(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)],
                      [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    assert result == desired_values
