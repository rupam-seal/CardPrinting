from PIL import Image

from utils.src import Source

class SaveImage:
    def __init__(self, background: str, card_path: str, a4_format_save: str):
        self.background = background
        self.card_path = card_path
        self.a4_format_save = a4_format_save

    def save(self):
        self.background.save(f"{self.card_path}.png")
        formate_a4 = Image.open(Source().print_format)
        resize_card = Image.open(f"{self.card_path}.png").resize((980, 600), Image.ANTIALIAS)
        formate_a4.paste(resize_card, (445, 90))
        formate_a4.save(f"{self.a4_format_save}.png")