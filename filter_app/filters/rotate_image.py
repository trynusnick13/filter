from PIL import Image
import PIL
import numpy as np
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image


class Rotate(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter
        self.np_image = np.asarray(self.image)

    def _rotate_image(self):
        im_rot = np.rot90(self.np_image)
        return Image("rotated image", PIL.Image.fromarray(im_rot))

    def apply_filter(self):
        return self._rotate_image()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("rotate photo", img)
    test_image = Rotate(base_image, "rotate photo")
    test_image.apply_filter()
    PIL.Image._show(test_image.apply_filter())
