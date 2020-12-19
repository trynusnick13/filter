from PIL import Image
import PIL
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image


class BlackAndWhiteFilter(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter

    def _black_and_white(self):
        bw_image = self.image.convert("L")
        return bw_image

    def apply_filter(self):
        return self._black_and_white()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("black and white photo", img)
    test_image = BlackAndWhiteFilter(base_image, "black and white filter")
    test_image.apply_filter()
    PIL.Image._show(test_image.apply_filter())


