from PIL import Image

a4_paper_img = Image.open("test/img_a4_paper.png")

card = Image.open("format/background_front.jpg").resize((1006, 635), Image.ANTIALIAS)
a4_paper_img.paste(card, (415, 18))

a4_paper_img.save("test/img_print_paper.png")