from filter_app.commands.command import ConcreteCommand
from filter_app.image.base_image import Image
from filter_app.filters.black_and_white_filter import BlackAndWhiteFilter
import PIL


class BlackAndWhiteCommand(ConcreteCommand):
    apply_name = "Applied black & white filter"

    def __init__(self, image, name=None):
        self.image = image
        self.name = name

    def undo(self):
        self.image = self.backup

    def save_image(self):
        self.backup = self.image

    def execute(self, new_image=None):
        if not(new_image is None):
            self.image = new_image
        black_and_white_filter = BlackAndWhiteFilter(image=self.image, name_of_filter='change brightness command' + self.image.name)
        return black_and_white_filter.apply_filter()


if __name__ == '__main__':
    img = PIL.Image.open("/Users/nicktrynus/Projects/filter/filter_app/tests/test_data/photos/test1.png")
    base_image = Image("rotate photo", img)
    test_image = BlackAndWhiteCommand(base_image).execute()
    # test_image.apply_filter()
    PIL.Image._show(test_image.pillow_image)


