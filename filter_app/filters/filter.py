from abc import ABCMeta, abstractmethod
from filter_app.commands import *
from filter_app.commands.command import Command

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
        self.filters = {}
        self.image = image
        self.name = name

    def apply_filter(self):
        while True:
            print(self.filters.keys())
            filter_ = input("Choose FILTER or enter 1 to exit ")

            if filter_ == "1":
                break
            elif filter_ in self.filters:
                if isinstance(self.filters[filter_], Command):
                    self.filters[filter_].execute()

    def add(self, filter_):
        self.filters[filter_.name] = filter_
