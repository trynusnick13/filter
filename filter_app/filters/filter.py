from abc import ABCMeta, abstractmethod



class Filter(metaclass=ABCMeta):

    def __init__(self, image):
        pass

    @abstractmethod
    def apply_filter(self):
        pass


class ImageFilter(Filter):

    def __init__(self, image, name_of_filter):
        self.image = image
        self.name_of_filter = name_of_filter

    def apply_filter(self):
        pass


class CompoundFilter(Filter):

    def __init__(self, filters):
        self.filters = filters

    def apply_filter(self):
        # handover execution to the filters in the filters list
        pass
    