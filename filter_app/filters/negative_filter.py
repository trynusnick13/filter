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
                pixel_color_vals = self.image.getpixel((i, j))
                red_pixel = 255 - pixel_color_vals[0]
                green_pixel = 255 - pixel_color_vals[1]
                blue_pixel = 255 - pixel_color_vals[2]

                self.image.putpixel((i, j), (red_pixel, green_pixel, blue_pixel))

        return self.image

    def apply_filter(self):
        return self._negative()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("negative photo", img)
    test_image = NegativeFilter(base_image, "negative filter")
    PIL.Image._show(test_image.apply_filter())


