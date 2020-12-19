from PIL import Image, ImageEnhance
import PIL
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image


class Contrast(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter

    def _contrast(self):
        enhancer = ImageEnhance.Contrast(self.image)
        factor = int(input("enter a factor "))
        im_convert = enhancer.enhance(factor)
        return im_convert


    def apply_filter(self):
        return self._contrast()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("contrast photo", img)
    test_image = Contrast(base_image, "change contrast")
    PIL.Image._show(test_image.apply_filter())