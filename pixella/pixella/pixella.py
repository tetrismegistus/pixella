# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw


class Downsampler:
    def __init__(self, filename, rescale=False, sample_rate=10):
        self.filename = filename
        img = Image.open(self.filename)
        self.w, self.h = img.size
        self.pixels_as_rows = self.get_pixels_as_rows(img)
        new_image = self.get_new_image(rescale=rescale, sample_rate=sample_rate)
        self.new_image = self.downsample(new_image, sample_rate=sample_rate, rescale=rescale)

    def downsample(self, img, sample_rate=None, rescale=False):
        drawing = ImageDraw.Draw(img)
        for row in range(0, self.h, sample_rate):
            for col in range(0, self.w, sample_rate):
                fill = self.pixels_as_rows[row][col]
                if rescale:
                    drawing.point([(col / sample_rate, row / sample_rate)], fill=fill)
                else:
                    drawing.rectangle([(col, row), (col + sample_rate, row + sample_rate)], fill=fill)
        return img

    def get_pixels_as_rows(self, img):
        pixel_list = list(img.getdata())
        return [pixel_list[i * self.w:(i + 1) * self.w] for i in range(self.h)]

    def get_new_image(self, rescale=False, sample_rate=None):
        if rescale:
            def rescale(x): return int(x / sample_rate) + 1
            return Image.new('RGB', size=(rescale(self.w), rescale(self.h)))
        else:
            return Image.new('RGB', size=(self.w, self.h))

    @staticmethod
    def save_image(image, filename):
        image.save(filename)
