from PIL import Image
import PIL
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image


class NegativeFilter(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter

    def _negative(self):
        for i in range(0, self.image.size[0] - 1):
            for j in range(0, self.image.size[1] - 1):
                pixelColorVals = self.image.getpixel((i, j))
                redPixel = 255 - pixelColorVals[0]
                greenPixel = 255 - pixelColorVals[1]
                bluePixel = 255 - pixelColorVals[2]

                self.image.putpixel((i, j), (redPixel, greenPixel, bluePixel))
        PIL.Image._show(self.image)

    def apply_filter(self):
        self._negative()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("black and white photo", img)
    test_image = NegativeFilter(base_image, "black and white filter")
    test_image.apply_filter()
