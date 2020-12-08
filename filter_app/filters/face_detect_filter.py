import cv2
from matplotlib import pyplot as plt
from filter_app.config_filter.config_facedetect import CASC_PATH
from filter_app.filters.filter import ImageFilter
import PIL
import numpy


class FaceDetectFilter(ImageFilter):
    cascPath = CASC_PATH

    def __init__(self, pillow_image, name_of_filter):
        self.pillow_image = pillow_image
        self.name_of_filter = name_of_filter
        self.opencv_image = cv2.cvtColor(numpy.array(self.pillow_image), cv2.COLOR_RGB2BGR)

    def _detect_faces(self):
        faceCascade = cv2.CascadeClassifier(self.cascPath)
        gray = cv2.cvtColor(self.opencv_image, cv2.COLOR_BGR2GRAY)
        self.faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)

        )

    def _put_rectangle_on_face(self):
        for (x, y, width, height) in self.faces:
            cv2.rectangle(self.opencv_image, (x, y), (x + width, y + height), (255, 105, 180), 2)
        im2 = self.opencv_image.copy()
        im2[:, :, 0] = self.opencv_image[:, :, 2]
        im2[:, :, 2] = self.opencv_image[:, :, 0]
        plt.imshow(im2)
        plt.xticks([]), plt.yticks([])
        plt.title(f'Found {len(self.faces)} faces!!!')
        plt.show()

    def apply_filter(self):
        self._detect_faces()
        self._put_rectangle_on_face()


if __name__ == '__main__':
    pil_image = PIL.Image.open('./photos/test1.png')
    image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    a = FaceDetectFilter(pil_image, 'face detect filter')
    a.apply_filter()

    # find_face('./photos/test0.jpg')
