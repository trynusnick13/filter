import ntpath
import numpy as np
import tkinter as tk
from PIL import Image as pillowImg
from copy import deepcopy
from tkinter import filedialog
from filter_app.commands.history import CommandHistory
from filter_app.filters.filter import CompoundFilter
from filter_app.image.base_image import Image
from filter_app.commands.FaceDetectCommand import FaceDetectCommand


class ImageEditor:
    dict_of_chains = {}

    def __init__(self):
        self.command_history = CommandHistory()
        self.image = None

    def load_image(self):
        root = tk.Tk()
        root.withdraw()
        file_path = tk.filedialog.askopenfilename()            # asking a user for file path using built-in tkinter
        file_path_copy = deepcopy(file_path)                # copy for file name, in order to save original path intact
        file_path_to_open = file_path                       # file path to one specific photo
        im = pillowImg.open(file_path_to_open)              # opening photo using Pillow 8.0.1
        tail = ntpath.split(file_path_copy)
        file_name = tail[1]                                 # getting file name from file path
        self.image = Image(file_name, im)
        # print(tail[1], im.format, im.mode, im.size)
        file_path = None
        file_path_copy = None
        file_path_to_open = None
        tail = None

    def create_chain(self, commands, name):
        chain1 = CompoundFilter(name, self.image)
        self.dict_of_chains[chain1.name] = chain1
        for command in commands:
            chain1.add(command)

    def create_facedetec_chain(self):
        self.create_chain([FaceDetectCommand(self.image, "face detect")], "face detect filters")

    def user_input(self):
        while True:
            print(self.dict_of_chains.keys())
            action = input("Choose ACTION or enter 1 to exit")
            if action == "1":
                break
            elif action in self.dict_of_chains.keys():
               self.image = self.dict_of_chains[action].apply_filter()

    def filtering(self):
        self.load_image()
        while True:
            if True:
                self.create_facedetec_chain()
                self.user_input()
                self.image.save_file()
            print("Enter 1 to exit")
            a = input()
            if a == '1':
                break
