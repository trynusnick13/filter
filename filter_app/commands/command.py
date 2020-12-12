from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, image, backup, args, kwargs):
        pass

    @abstractmethod
    def save_image(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):

    def __init__(self, image, backup, name=None):
        self.image = image
        self.backup = backup
        self.name = name

    def undo(self):
        self.image = self.backup

    def save_image(self):
        self.backup = self.image

    def execute(self):
        pass
