from PIL import Image
from utils.certificate_no import CertificateNo

from utils.draw import Draw
from utils.print import Print
from utils.save_img import SaveImage
from utils.src import Source
from utils.clear_entry import ClearEntry
from utils.insert_default_value import InsertDefault

'''
    default background image
    background_front: [default front background]
    background_back: [default back background]
'''
background_front = Image.open(Source().default_gold_front)
background_back = Image.open(Source().default_gold_back)

'''
    Fonts
'''
font_title = Source().font_title
font_text = Source().font_text

'''
    Color
'''
color_title = Source().COLOR_TITLE
color_text = Source().COLOR_TEXT

class Diamond:
    def __init__(self, obj):
        self.obj = obj

    def set_value(self):
        '''
            '''''''''''''''''''''''''''''''''''''''''''''''''FRONT CARD STYLE'''''''''''''''''''''''''''''''''''''''''''''''''
        '''

        # product image
        product_image = Draw(self.obj.entry1, background_front, 2300, 600)
        product_image.adding_image(1800, 1400)

        # jewellery name on front of the card
        jewellery_front_name = Draw(self.obj.entry3, background_front, background_front.width, 100, color_title, font_title, 190)
        jewellery_front_name.title_text("u")

        # Customer name
        customer_name = Draw(self.obj.entry5, background_front, 1038, 755, color_text, font_text, 90)
        customer_name.adding_text()

        # date
        date_in = Draw(self.obj.entry6, background_front, 1038, 1055, color_text,  font_text, 90)
        date_in.adding_text()

        # product name
        product_name = Draw(self.obj.entry7, background_front, 1038, 1205, color_text,  font_text, 90)
        product_name.adding_text()

        # product weight
        product_weight = Draw(self.obj.entry8, background_front, 1038, 1355, color_text,  font_text, 90)
        product_weight.adding_text_with_unit("Gm")

        # product karate
        product_karate = Draw(self.obj.entry9, background_front, 1038, 1505, color_text,  font_text, 90)
        product_karate.adding_text_with_unit("Ct")

        # gold value
        colour_value = Draw(self.obj.entry14, background_front, 600, 2000, color_text,  font_text, 90)
        colour_value.adding_text()

        # silver value
        clarity_value = Draw(self.obj.entry15, background_front, 600, 2170, color_text,  font_text, 90)
        clarity_value.adding_text()

        # copper value
        cut_value = Draw(self.obj.entry16, background_front, 1670, 2000, color_text,  font_text, 90)
        cut_value.adding_text()

        # other value
        finish_value = Draw(self.obj.entry17, background_front, 1670, 2170, color_text,  font_text, 90)
        finish_value.adding_text()

        # certificate_no
        number = CertificateNo().get_no()

        print(number)

        certificate_no = Draw(number, background_front, 1038, 905, color_text,  font_text, 90)
        certificate_no.adding_certificate_number()

        '''
            '''''''''''''''''''''''''''''''''''''''''''''''''BACK CARD STYLE'''''''''''''''''''''''''''''''''''''''''''''''''
        '''

        # QR code
        qr_img = Draw(self.obj.entry2, background_back, 3790, 200)
        qr_img.adding_qr_img(450, 450)

        # jewellery name on back of the card
        jewellery_back_name = Draw(self.obj.entry3, background_back, background_back.width, 350, color_text,  font_title, 125)
        jewellery_back_name.title_text("u")

        # adress
        jewellery_back_adress = Draw(self.obj.entry4, background_back, background_back.width, 500, color_text,  font_text, 90)
        jewellery_back_adress.title_text("l")

    def print_card(self):
        global background_front, background_back

        front_card = SaveImage(background_front, "saved/front_format", "saved/front_print_format")
        front_card.save()
        gold_card_front_print = Print("front_print_format")
        gold_card_front_print.print_hard_copy()

        back_card = SaveImage(background_back, "saved/back_format", "saved/back_print_format")
        back_card.save()
        gold_card_back_print = Print("back_print_format")
        gold_card_back_print.print_hard_copy()

        ClearEntry(self.obj).clear()
        InsertDefault(self.obj).insert_default_value_to_entry()

        background_front = Image.open(Source().default_gold_front)
        background_back = Image.open(Source().default_gold_back)