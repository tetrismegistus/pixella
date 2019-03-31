# -*- coding: utf-8 -*-
from PIL import Image


class Downsampler:
    def __init__(self, filename):
        self.filename = filename

    def downsample(self):
        return Image.open('out.png')

    def get_pixels_as_rows(self):
        img = Image.open(self.filename)
        w, h = img.size
        pixel_list = list(img.getdata())
        return [pixel_list[i * w:(i + 1) * w] for i in range(h)]
