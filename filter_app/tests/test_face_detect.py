from filter_app.filters.face_detect_filter import FaceDetectFilter
import PIL
from filter_app.image.base_image import Image

def test_faces_png():
    pil_image = PIL.Image.open('./test_data/photos/test1.png')
    base_image = Image("18 people on png", pil_image)
    testing_filter = FaceDetectFilter(base_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 18

def test_faces_jpg():
    pil_image = PIL.Image.open('./test_data/photos/test0.jpg')
    base_image = Image("1 people on jpg", pil_image)
    testing_filter = FaceDetectFilter(base_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 1

def test_negative_faces():
    pil_image = PIL.Image.open('./test_data/photos/dog-test.jpg')
    base_image = Image("dog", pil_image)
    testing_filter = FaceDetectFilter(base_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 0




