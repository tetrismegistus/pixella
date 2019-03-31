#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pixella
----------------------------------

Tests for `pixella` module.
"""
from pixella import pixella


def test_downsample_brain():
    downsampler = pixella.Downsampler('brain.png')
    from PIL import Image
    img = downsampler.get_new_image()
    result = downsampler.downsample(img)
    comparison = Image.open('out.png')
    assert list(comparison.getdata()) == list(result.getdata())


def test_get_pixels_as_rows():
    file = 'wbrgb.png'
    downsampler = pixella.Downsampler(file)
    from PIL import Image
    img = Image.open(file)
    result = downsampler.get_pixels_as_rows(img)
    desired_values = [[(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)],
                      [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    assert result == desired_values


def test_get_new_image_surface_no_size_loss():
    downsampler = pixella.Downsampler('100x100.png')
    result = downsampler.get_new_image()
    w, h = result.size
    assert w == 100
    assert h == 100

def test_get_new_image_no_size_loss():
    downsampler = pixella.Downsampler('100x100.png')
    result = downsampler.get_new_image()
    w, h = result.size
    assert w == 100
    assert h == 100

def test_get_new_image_shrink():
    downsampler = pixella.Downsampler('100x100.png')
    result = downsampler.get_new_image(rescale=True, sample_rate=20)
    w, h = result.size
    assert w == 6
    assert h == 6

