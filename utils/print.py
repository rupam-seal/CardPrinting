import os

class Print:
    def __init__(self, path):
        self.path = path

    def print_hard_copy(self):
        os.startfile(f"saved\{self.path}.png", "print")