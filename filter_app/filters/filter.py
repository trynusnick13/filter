from abc import ABCMeta, abstractmethod
from filter_app.commands import *
from filter_app.commands.command import Command
from filter_app.image.base_image import Image
from filter_app.commands.history import CommandHistory


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
        self.local_history = CommandHistory()

    def apply_filter(self):
        active_image = self.image
        while True:
            print(self.filters.keys())
            filter_ = input("Choose FILTER or enter 1 to exit, print 2 to Undo ")

            if filter_ == "1":
                return active_image, self.local_history.history
            if filter_ == "2":
                active_image = self.local_history.pop()
            elif filter_ in self.filters:
                if isinstance(self.filters[filter_], Command):
                    self.filters[filter_].make_backup()
                    active_image = self.filters[filter_].execute(active_image)
                    self.local_history.push(self.filters[filter_])
                    print(self.local_history.history)
                else:
                    self.filters[filter_].apply_filter(active_image)

    def add(self, filter_):
        self.filters[filter_.name] = filter_
