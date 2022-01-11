from tkinter import *

class ClearEntry():
    def __init__(self, obj):
        self.obj = obj

    # clear all the entry after complete the task
    def clear(self):
        self.obj.entry_product_img.delete(0, END)
        self.obj.entry_qr_img.delete(0, END)
        self.obj.entry_jewellery_name.delete(0, END)
        self.obj.entry_adress.delete(0, END)
        self.obj.entry_customer_name.delete(0, END)
        self.obj.entry_date.delete(0, END)
        self.obj.entry_product_name.delete(0, END)
        self.obj.entry_product_weight.delete(0, END)
        self.obj.entry_product_karate.delete(0, END)
        self.obj.entry_gold_value.delete(0, END)
        self.obj.entry_silver_value.delete(0, END)
        self.obj.entry_coper_value.delete(0, END)
        self.obj.entry_other_value.delete(0, END)
