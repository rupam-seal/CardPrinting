from PIL import Image, ImageFont, ImageDraw
import pyqrcode
import png

class Draw:
    '''
        draw: [default card background]
        entry: [using entry attribute to get the correct value from the tkinter entry and insert it into the 'draw']
        x: [x coordinate of the image - using x we can put text and image to the desired place on x axis on 'draw']
        y: [y coordinate of the image - using y we can put text and image to the desired place on y axis on 'draw']
        color
        font
        font_size
    '''
    def __init__(self, entry, draw, x=None, y=None, color=None, font=None, font_size=None):
        self.entry = entry
        self.draw = draw
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.font_size = font_size

    '''
    title text
        - get the text from tkinter entry
        - paste the text on default background image
        - text has to be center of default background image
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
                case = [case of the text "u" or "l"]
    '''

    def title_text(self, case: str):
        font = ImageFont.truetype(self.font, self.font_size)

        img_editable = ImageDraw.Draw(self.draw)

        title_text = self.entry.get()

        # : if user pass "u", text will apear uppercase
        # : otherwise text will apear as default

        # : this validatition is given because if user
        #   wants to put some custom case text to center
        #   of the default background image
        if case == "u":
            title_text = title_text.upper()
        else:
            title_text = title_text

        # w: width of the text
        # h: height of the text
        w, h = img_editable.textsize(title_text, font=font)

        # W: width of the default background image
        # H: height of the default background image
        image = Image.open("format/background_front.jpg")
        W, H = image.size

        # performing calculation to center the text on image
        
        # DIAGRAM
        # ====    ====    ====    ====
        #        |____________|
        #         text size(w)
        # |___________________________|
        #        image size(W)
        # 
        # |____|
        # margin-left

        # let:
        # ====     : 50px
        # ==== * 2 : 100px (textSize)
        # ==== * 4 : 200px (imageSize)
        
        # net-margin  = W - w
        #             = 200px - 100px
        #             = 100px (net margin of left right)
        # margin-left = 100px/2
        #             = 50px

        # [centerText = (width of image(W) - width of text(w)) / 2]

        img_editable.text(((W-w)/2, self.y), title_text,
                          (self.color), font=font)
    
    '''
    adding normal text
        - get the text from tkinter entry
        - set the text to default background image
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
    '''
    def adding_text(self):
        font = ImageFont.truetype(self.font, self.font_size)

        in_txt = self.entry.get()

        img_editable = ImageDraw.Draw(self.draw)

        img_editable.text((self.x, self.y), in_txt, (self.color), font=font)

    '''
    adding unique number text
        - get the unique number text from {certificate_no class}
        - paste the text on default background image
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
    '''
    def adding_certificate_number(self):
        font = ImageFont.truetype(self.font, self.font_size)

        img_editable = ImageDraw.Draw(self.draw)

        img_editable.text((self.x, self.y), self.entry,
                          (self.color), font=font)

    '''
    adding text + unit
        - get the text from tkinter entry
        - pasting text + unit to the background image [99.99%]
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
                unit: [gm, ct, %  value]
    '''
    def adding_text_with_unit(self, unit):
        font = ImageFont.truetype(self.font, self.font_size)

        in_txt = self.entry.get()

        img_editable = ImageDraw.Draw(self.draw)

        img_editable.text((self.x, self.y), in_txt +
                          f"{unit}", (self.color), font=font)

    '''
    adding image
        - get the path of the image from tkinter entry
        - paste it on default background image
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
                image_x: [crop value of x axis]
                image_y: [crop value of y axis]
    '''
    def adding_image(self, image_x, image_y):
        self.img = Image.open(self.entry.get()).resize(
            (image_x, image_y), Image.ANTIALIAS)
        self.draw.paste(self.img, (self.x, self.y))
        
    '''
    creating and adding qr image from link
        - get the link from tkinter entry
        - create qr code image using link and save
        - open image
        - paste it on default background image
    method: user can pass
                x: [text x axis location]
                y: [text y axis location]
                qr_img_x: [crop value of x axis]
                qr_img_y: [crop value of y axis]
    '''
    def adding_qr_img(self, qr_img_x, qr_img_y):
        s = self.entry.get()

        url = pyqrcode.create(s)

        url.png('saved/qr.png', scale=6)

        qr_img = Image.open(
            "saved/qr.png").resize((qr_img_x, qr_img_y), Image.ANTIALIAS)

        self.draw.paste(qr_img, (self.x, self.y))