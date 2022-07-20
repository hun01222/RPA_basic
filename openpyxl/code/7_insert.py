from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8)
# ws.insert_rows(8,5) #8부터 5개

wb.save("sample_insert_rows.xlsx")
