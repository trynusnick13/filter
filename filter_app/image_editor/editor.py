import ntpath
import numpy as np
import tkinter as tk
from PIL import Image as pillowImg
from copy import deepcopy
from tkinter import filedialog
from filter_app.commands.history import CommandHistory
from filter_app.filters.filter import CompoundFilter
from filter_app.image.base_image import Image


class ImageEditor:
    dict_of_chains = {}

    def __init__(self):
        self.command_history = CommandHistory()
        self.image = None

    def load_image(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()            # asking a user for file path using built-in tkinter
        file_path_copy = deepcopy(file_path)                # copy for file name, in order to save original path intact
        file_path_to_open = file_path                       # file path to one specific photo
        im = pillowImg.open(file_path_to_open)              # opening photo using Pillow 8.0.1
        tail = ntpath.split(file_path_copy)
        file_name = tail[1]                                 # getting file name from file path
        self.image = Image(file_name, im)
        # print(tail[1], im.format, im.mode, im.size)

    def create_chain(self, commands):
        chain1 = CompoundFilter("face detect filters")
        self.dict_of_chains[chain1.name] = chain1
        for command in commands:
            chain1.add(command)

    def filtering(self):
        while True:
            self.load_image()
            break
