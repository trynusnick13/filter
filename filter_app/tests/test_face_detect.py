from filter_app.filters.face_detect_filter import FaceDetectFilter
import PIL

# "/Users/nicktrynus/Projects/filter/filter_app/filters/haarcascade_frontalface_default.xml"
"filter_app/filters/haarcascade_frontalface_default.xml"
def test_faces_png():
    pil_image = PIL.Image.open('./test_data/photos/test1.png')
    testing_filter = FaceDetectFilter(pil_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 18

def test_faces_jpg():
    pil_image = PIL.Image.open('./test_data/photos/test0.jpg')
    testing_filter = FaceDetectFilter(pil_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 1

def test_negative_faces():
    pil_image = PIL.Image.open('./test_data/photos/dog-test.jpg')
    testing_filter = FaceDetectFilter(pil_image, 'face detect filter')
    testing_filter._detect_faces()
    assert len(testing_filter.faces) == 0




