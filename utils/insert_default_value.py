from datetime import date

from utils.src import Source

class InsertDefault:
    def __init__(self, obj):
        self.obj = obj

    # Method inserting default value to the entry
    def insert_default_value_to_entry(self):
        # inserting current date/month/year to the date entry
        # Month abbreviation, day and year
        self.today = date.today()
        self.dateEntry = self.today.strftime("%b-%d-%Y")
        self.obj.entry6.insert(0, self.dateEntry)

        # inserting '0.00' to the silver entry
        self.obj.entry11.insert(0, "0.00")
        # inserting '0.00' to the other entry
        self.obj.entry13.insert(0, "0.00")
        # inserting '0.00' to the copper entry
        self.obj.entry12.insert(0, "0.00")