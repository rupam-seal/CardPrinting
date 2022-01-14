from tkinter import *
from tkinter import filedialog, messagebox

from gold import Gold
from diamond import Diamond
from utils.insert_default_value import InsertDefault
from utils.src import Source

from utils.entry_state import EntryStates

'''
    Gui class: [all the tkinter entry and buttons]
'''
class Gui():
    def __init__(self):
        # window
        self.window = Tk()
        self.window.geometry("1000x620")
        self.window.configure(bg = Source().COLOR_WHITE)
        self.window.iconbitmap("assets/card.ico")
        self.window.title("Card Printing Designer")

        # canvas and background
        self.background()

        # tkinter entry
        self.entry()

        # tkinter button
        self.button()

        # inserting default value to the entry
        InsertDefault(self).insert_default_value_to_entry()

        # default entry state is gold state
        gold_state = EntryStates("normal", "disabled", Source().COLOR_DARK)
        gold_state.state(self)


        # mainLoop
        self.run()

    # inserting background to the window
    def background(self):
        self.canvas = Canvas(
            self.window,
            bg = Source().COLOR_WHITE,
            height = 620,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"assets/background.png")
        self.background = self.canvas.create_image(
            489.5, 308.5,
            image=self.background_img)

    # inserting entry's to the window
    '''
    Gold Input
        - modify no.
        - select image from file
        - select qr from file | genarate qr from link
        - jewellery name
        - adress
        - customer name
        - date
        - product name
        - weight
        - karate
        - AU - gold value
        - AG - silver value
        - cu - copper value
        - oth - other value
    Diamond Input
        - modify no.
        - select image from file
        - select qr from file | genarate qr from link
        - jewellery name
        - adress
        - customer name
        - date
        - product name
        - weight
        - karate
        - colour
        - clarity
        - cut
        - finish

    '''
    
    # Entry method
    def entry(self):
        # ----------------------------------------- modify entry ----------------------------------------------------
        self.entry0_img = PhotoImage(file = f"assets/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            256.0, 38.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry0.place(
            x = 230.0, y = 23,
            width = 52.0,
            height = 28)

        # ---------------------------------------- product image entry -------------------------------------------------
        self.entry1_img = PhotoImage(file = f"assets/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            110.5, 105.0,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry1.place(
            x = 59.0, y = 90,
            width = 103.0,
            height = 28)

        # ------------------------------------------- qr image entry ----------------------------------------------------
        self.entry2_img = PhotoImage(file = f"assets/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            233.5, 105.0,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry2.place(
            x = 182.0, y = 90,
            width = 103.0,
            height = 28)

        # ---------------------------------------- jewellery name entry ---------------------------------------------------
        self.entry3_img = PhotoImage(file = f"assets/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            110.5, 172.0,
            image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry3.place(
            x = 59.0, y = 157,
            width = 103.0,
            height = 28)


        # ------------------------------------------- adress entry ---------------------------------------------------------
        self.entry4_img = PhotoImage(file = f"assets/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            233.5, 172.0,
            image = self.entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry4.place(
            x = 182.0, y = 157,
            width = 103.0,
            height = 28)

        # ----------------------------------------- customer name entry ----------------------------------------------------
        self.entry5_img = PhotoImage(file = f"assets/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            172.0, 239.0,
            image = self.entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry5.place(
            x = 59.0, y = 224,
            width = 226.0,
            height = 28)

        # ---------------------------------------------- date entry ---------------------------------------------------------
        self.entry6_img = PhotoImage(file = f"assets/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            110.5, 306.0,
            image = self.entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry6.place(
            x = 59.0, y = 291,
            width = 103.0,
            height = 28)

        # ------------------------------------------- product name entry -----------------------------------------------------
        self.entry7_img = PhotoImage(file = f"assets/img_textBox7.png")
        self.entry7_bg = self.canvas.create_image(
            233.5, 306.0,
            image = self.entry7_img)

        self.entry7 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry7.place(
            x = 182.0, y = 291,
            width = 103.0,
            height = 28)


        # ------------------------------------------ product weight entry -----------------------------------------------------
        self.entry8_img = PhotoImage(file = f"assets/img_textBox8.png")
        self.entry8_bg = self.canvas.create_image(
            110.5, 373.0,
            image = self.entry8_img)

        self.entry8 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry8.place(
            x = 59.0, y = 358,
            width = 103.0,
            height = 28)

        # ------------------------------------------ product karate entry ----------------------------------------------------
        self.entry9_img = PhotoImage(file = f"assets/img_textBox9.png")
        self.entry9_bg = self.canvas.create_image(
            233.5, 373.0,
            image = self.entry9_img)

        self.entry9 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry9.place(
            x = 182.0, y = 358,
            width = 103.0,
            height = 28)

        # -------------------------------------------- gold value entry -------------------------------------------------------
        self.entry10_img = PhotoImage(file = f"assets/img_textBox10.png")
        self.entry10_bg = self.canvas.create_image(
            84.5, 471.0,
            image = self.entry10_img)

        self.entry10 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry10.place(
            x = 59.0, y = 456,
            width = 51.0,
            height = 28)

        # ------------------------------------------- silver value entry -------------------------------------------------------
        self.entry11_img = PhotoImage(file = f"assets/img_textBox11.png")
        self.entry11_bg = self.canvas.create_image(
            159.5, 471.0,
            image = self.entry11_img)

        self.entry11 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry11.place(
            x = 134.0, y = 456,
            width = 51.0,
            height = 28)

        # ------------------------------------------- copper value entry -------------------------------------------------------
        self.entry12_img = PhotoImage(file = f"assets/img_textBox12.png")
        self.entry12_bg = self.canvas.create_image(
            234.5, 471.0,
            image = self.entry12_img)

        self.entry12 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry12.place(
            x = 209.0, y = 456,
            width = 51.0,
            height = 28)

        # --------------------------------------------- other value entry -------------------------------------------------------
        self.entry13_img = PhotoImage(file = f"assets/img_textBox13.png")
        self.entry13_bg = self.canvas.create_image(
            309.5, 471.0,
            image = self.entry13_img)

        self.entry13 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry13.place(
            x = 284.0, y = 456,
            width = 51.0,
            height = 28)

        # ------------------------------------------------ color entry -----------------------------------------------------------
        self.entry14_img = PhotoImage(file = f"assets/img_textBox14.png")
        self.entry14_bg = self.canvas.create_image(
            84.5, 540.0,
            image = self.entry14_img)

        self.entry14 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry14.place(
            x = 59.0, y = 525,
            width = 51.0,
            height = 28)

        # ------------------------------------------------ clarity entry ----------------------------------------------------------
        self.entry15_img = PhotoImage(file = f"assets/img_textBox15.png")
        self.entry15_bg = self.canvas.create_image(
            159.5, 540.0,
            image = self.entry15_img)

        self.entry15 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry15.place(
            x = 134.0, y = 525,
            width = 51.0,
            height = 28)

        # ------------------------------------------------- cut entry --------------------------------------------------------------
        self.entry16_img = PhotoImage(file = f"assets/img_textBox16.png")
        self.entry16_bg = self.canvas.create_image(
            234.5, 540.0,
            image = self.entry16_img)

        self.entry16 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry16.place(
            x = 209.0, y = 525,
            width = 51.0,
            height = 28)

        # -------------------------------------------------- finish entry ----------------------------------------------------------
        self.entry17_img = PhotoImage(file = f"assets/img_textBox17.png")
        self.entry17_bg = self.canvas.create_image(
            309.5, 540.0,
            image = self.entry17_img)

        self.entry17 = Entry(
            bd = 0,
            bg = Source().COLOR_DARK,
            fg = Source().COLOR_WHITE,
            insertbackground = Source().COLOR_WHITE,
            highlightthickness = 0)

        self.entry17.place(
            x = 284.0, y = 525,
            width = 51.0,
            height = 28)

    # [2] inserting button to the window
    '''

    Gold Button
        - gold_front
        - gold_back

    Diamond Button
        - diamond_front
        - diamond_back

    Other Button
        - modify
        - card_one
        - card_two
        - card_three
        - card_four
        - about

    '''
    # Button method
    def button(self):
        # ----------------------------------------------------- modify button ----------------------------------------------------------
        self.img2 = PhotoImage(file = f"assets/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.modify(self),
            relief = "flat")

        self.b2.place(
            x = 294, y = 28,
            width = 60,
            height = 23)

        # -------------------------------------------------- gold tab button ----------------------------------------------------------
        self.img0 = PhotoImage(file = f"assets/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.gold_card(self),
            relief = "flat")

        self.b0.place(
            x = 51, y = 28,
            width = 70,
            height = 20)
        # -------------------------------------------------- diamond tab button --------------------------------------------------------
        self.img1 = PhotoImage(file = f"assets/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.diamond_card(self),
            relief = "flat")

        self.b1.place(
            x = 131, y = 28,
            width = 70,
            height = 20)

        # -------------------------------------------------- open item image ----------------------------------------------------------
        self.img5 = PhotoImage(file = f"assets/img5.png")
        self.b5 = Button(
            image = self.img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.open_product_image(self),
            relief = "flat")

        self.b5.place(
            x = 58, y = 63,
            width = 94,
            height = 19)

        # ---------------------------------------------------- open qr image ----------------------------------------------------------
        self.img6 = PhotoImage(file = f"assets/img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.open_qr_image(self),
            relief = "flat")

        self.b6.place(
            x = 179, y = 63,
            width = 94,
            height = 19)

        # ------------------------------------------- gold button print ---------------------------------------------------
        self.img3 = PhotoImage(file = f"assets/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.print_gold_card(self),
            relief = "flat")

        self.b3.place(
            x = 87, y = 568,
            width = 100,
            height = 29)

        # ------------------------------------------ diamond button print ---------------------------------------------------
        self.img14 = PhotoImage(file = f"assets/img14.png")
        self.b14 = Button(
            image = self.img14,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.print_diamond_card(self),
            relief = "flat")

        self.b14.place(
            x = 205, y = 568,
            width = 100,
            height = 29)

        # -------------------------------------------------- Gold ----------------------------------------------------------
        self.img7 = PhotoImage(file = f"assets/img7.png")
        self.b7 = Button(
            image = self.img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.gold_card(self),
            relief = "flat")

        self.b7.place(
            x = 606, y = 122,
            width = 70,
            height = 20)


        # -------------------------------------------------- Diamnond ----------------------------------------------------------
        self.img8 = PhotoImage(file = f"assets/img8.png")
        self.b8 = Button(
            image = self.img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.diamond_card(self),
            relief = "flat")

        self.b8.place(
            x = 700, y = 122,
            width = 70,
            height = 20)

        # ----------------------------------------------------- card one -------------------------------------------------------------
        self.img9 = PhotoImage(file = f"assets/img9.png")
        self.b9 = Button(
            image = self.img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.about(self),
            relief = "flat")

        self.b9.place(
            x = 600, y = 190,
            width = 26,
            height = 28)

        # ----------------------------------------------------- card two -------------------------------------------------------------
        self.img10 = PhotoImage(file = f"assets/img10.png")
        self.b10 = Button(
            image = self.img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.about(self),
            relief = "flat")

        self.b10.place(
            x = 650, y = 190,
            width = 26,
            height = 28)

        # ----------------------------------------------------- card three -------------------------------------------------------------
        self.img11 = PhotoImage(file = f"assets/img11.png")
        self.b11 = Button(
            image = self.img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.about(self),
            relief = "flat")

        self.b11.place(
            x = 700, y = 190,
            width = 26,
            height = 28)

        # ----------------------------------------------------- card four -------------------------------------------------------------
        self.img12 = PhotoImage(file = f"assets/img12.png")
        self.b12 = Button(
            image = self.img12,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.about(self),
            relief = "flat")

        self.b12.place(
            x = 750, y = 190,
            width = 26,
            height = 28)

        # ---------------------------------------------------- about button ------------------------------------------------------------
        self.img13 = PhotoImage(file = f"assets/img13.png")
        self.b13 = Button(
            image = self.img13,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.about(self),
            relief = "flat")

        self.b13.place(
            x = 904, y = 34,
            width = 54,
            height = 19)

    # tkinter mainloop and window size
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

'''
    ButtonCommand: [all the onClick function of tkinter buttons]
'''
class ButtonCommand(Gui):

    def modify(self):
        print("modify")

    # gold_card:
    # only show the entry which is used by gold card
    # diamond card entry gets disabled]
    def gold_card(self):
        gold_state = EntryStates("normal", "disabled", Source().COLOR_DARK)
        gold_state.state(self)

    # diamond_card:
    # only show the entry which is used by diamond card
    # gold card entry gets disabled
    def diamond_card(self):
        gold_state = EntryStates("disabled", "normal", Source().COLOR_DARK)
        gold_state.state(self)

    # open image from file
    # set the path to the entry
    def open_product_image(self):
        path = filedialog.askopenfilename()
        self.entry1.insert(END, path)
        print(path)

    def open_qr_image(self):
        print("open_qr_image")

    def print_gold_card(self):
        gold = Gold(self)
        gold.set_value()
        gold.print_card()

    def print_diamond_card(self):
        diamond = Diamond(self)
        diamond.set_value()
        diamond.print_card()

    def about(self):
        messagebox.showinfo("Card Printing Designer","- Created By Rupam Seal\n- Version 1.0.1")