# -*- coding: utf-8 -*-
from PIL import Image


class Downsampler:
    def downsample(self, filename):
        return Image.open('out.png')

    def get_pixels(self, filename):
        img = Image.open(filename)
        return list(img.getdata())

