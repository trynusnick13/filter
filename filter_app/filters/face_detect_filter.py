import cv2
from matplotlib import pyplot as plt
from filter_app.config_filter.config_facedetect import CASC_PATH
from filter_app.filters.filter import ImageFilter
from filter_app.image.base_image import Image
import PIL
import numpy


class FaceDetectFilter(ImageFilter):
    cascPath = CASC_PATH

    def __init__(self, image, name_of_filter):
        self.image = image.pillow_image
        self.name_of_filter = name_of_filter
        self.opencv_image = cv2.cvtColor(numpy.array(self.image), cv2.COLOR_RGB2BGR)

    def _detect_faces(self):
        faceCascade = cv2.CascadeClassifier(self.cascPath)
        gray = cv2.cvtColor(self.opencv_image, cv2.COLOR_RGB2GRAY)
        self.faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.25,
            minNeighbors=6,
            minSize=(30, 30)

        )

    def _put_rectangle_on_face(self):
        for (x, y, width, height) in self.faces:
            cv2.rectangle(self.opencv_image, (x, y), (x + width, y + height), (255, 105, 180), 2)
        self.opencv_image = cv2.cvtColor(numpy.array(self.opencv_image), cv2.COLOR_BGR2RGB)
        im_pil = PIL.Image.fromarray(self.opencv_image)
        return Image("updated image", im_pil)

    @staticmethod
    def _save_image(filename='untitled', image=None):
        cv2.imwrite(filename, image)

    def apply_filter(self):
        self._detect_faces()
        return self._put_rectangle_on_face()




if __name__ == '__main__':
    pil_image = PIL.Image.open('./photos/test1.png')
    base_image = Image("18 people", pil_image)
    a = FaceDetectFilter(base_image, 'face detect filter')
    a.apply_filter()
    # find_face('./photos/test0.jpg')
