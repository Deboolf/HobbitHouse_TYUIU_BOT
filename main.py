import pandas as pd
import openpyxl as xl
from openpyxl.descriptors import String

def sel_cell(sheet, cell):
    res = sheet.sheet_view.selection[0].sqref = cell
    return res

tb = xl.open("Test.xlsx")
ws = tb.worksheets[0]
sel_cell(ws, "B3")

curCell = ws.selected_cell
ws.__setitem__(curCell, 9)
tb.save("Test.xlsx")
tb.close()

#h = pd.ExcelFile("Test.xlsx")
#df = Da
#print(pd.read_excel("Test.xlsx","Лист1", usecols="C"))