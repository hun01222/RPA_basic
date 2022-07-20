from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Hello"
wb.save("sample.xlsx")
wb.close()
