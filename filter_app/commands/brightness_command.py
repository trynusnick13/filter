from filter_app.commands.command import ConcreteCommand
from filter_app.image.base_image import Image
from filter_app.filters.change_brightness import ChangeBrightness
import PIL


class BrightnessCommand(ConcreteCommand):

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
        brightness_filter = ChangeBrightness(image=self.image, name_of_filter='change brightness command' + self.image.name)
        return brightness_filter.apply_filter()


if __name__ == '__main__':
    img = PIL.Image.open("/Users/nicktrynus/Projects/filter/filter_app/tests/test_data/photos/test1.png")
    base_image = Image("rotate photo", img)
    test_image = BrightnessCommand(base_image).execute()
    # test_image.apply_filter()
    PIL.Image._show(test_image.pillow_image)


