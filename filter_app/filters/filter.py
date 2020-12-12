from abc import ABCMeta, abstractmethod
from filter_app.commands import *


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

    def __init__(self, name, image=None):
        self.filters = []
        self.image = image
        self.name = name

    def apply_filter(self):
        # handover execution to the filters in the filters list
        pass

    def add(self, filter_):
        self.filters.append(filter_)
        pass
