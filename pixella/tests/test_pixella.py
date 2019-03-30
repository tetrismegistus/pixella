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

