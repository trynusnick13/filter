import PIL
from PIL import Image, ImageDraw
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image


class SepiaFilter(ImageFilter):
    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter

    def _sepia(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        depth = 30
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                s = (a + b + c) // 3
                a = s + depth * 2
                b = s + depth
                c = s
                if a > 255:
                    a = 255
                if b > 255:
                    b = 255
                if c > 255:
                    c = 255
                draw.point((i, j), (a, b, c))
        return Image("sepia filter", self.image)

    def apply_filter(self):
        return self._sepia()


if __name__ == '__main__':
    img = PIL.Image.open("./photos/test4.png")
    base_image = Image("sepia photo", img)
    test_image = SepiaFilter(base_image, "sepia filter")
    test_image.apply_filter()
    PIL.Image._show(test_image.apply_filter())
