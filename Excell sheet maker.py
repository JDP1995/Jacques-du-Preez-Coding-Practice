# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a

from openpyxl import Workbook

#creating the workbook

workbook = Workbook()

#selecting the worksheet we will use

worksheet= workbook.active

#laying out the top row column titles

worksheet["a1"] = "Title"
worksheet["a2"] ="Summary"
worksheet["c1"]="Source"

# Saving the new excell file in the apprpriate folder

folder_path = ("C:\\Users\\User\\Documents\\test folder\\")
workbook.save(folder_path + "Testfile.xlsx")



