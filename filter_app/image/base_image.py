class Image:
    def __init__(self, name, pillow_image):
        self.name = name
        self.pillow_image = pillow_image

    def save_file(self, path='./', name='untitled1.png'):
        self.pillow_image.save(name)
