from PIL import Image, ImageEnhance
import PIL
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image
from filter_app.config_filter.config_default import DEFAULT_FACTOR

class ChangeBrightness(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter

    def _change_brightness(self):
        enhancer = ImageEnhance.Brightness(self.image)
        # factor = int(input("enter a factor "))
        im_convert = enhancer.enhance(DEFAULT_FACTOR)
        return Image("updated brightness", im_convert)





    def apply_filter(self):
        return self._change_brightness()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("bright photo", img)
    test_image = ChangeBrightness(base_image, "change brightness")
    PIL.Image._show(test_image.apply_filter())