from filter_app.commands.command import ConcreteCommand
from filter_app.image.base_image import Image
from filter_app.filters.face_detect_filter import FaceDetectFilter
import PIL


class FaceDetectCommand(ConcreteCommand):

    def __init__(self, image):
        self.image = image

    def undo(self):
        self.image = self.backup

    def save_image(self):
        self.backup = self.image

    def execute(self):
        face_detect_filter = FaceDetectFilter(image=self.image, name_of_filter='face detect filter' + self.image.name)
        face_detect_filter.apply_filter()


if __name__ == '__main__':
    pil_image = PIL.Image.open('/Users/nicktrynus/Projects/filter/filter_app/tests/test_data/photos/test1.png')
    base_image = Image("jacky chan", pil_image)
    a = FaceDetectCommand(base_image)
    a.execute()


