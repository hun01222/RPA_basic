from openpyxl.utils.cell import coordinate_from_string
from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

ws.append(["번호", "영어", "수학"])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

col_B = ws["B"]
'''
print(col_B)
for cell in col_B:
    print(cell.value)
'''

col_range = ws["B:C"]  # B, C 함께 가져오기
'''
for cols in col_range:
    for cell in cols:
        print(cell.value)
'''

row_title = ws[1]
'''
for cell in row_title:
    print(cell.value)
'''

row_range = ws[2:6]  # 2부터 6까지 가져오기
'''
for rows in row_range:
    for cell in rows:
        print(cell.value, end=" ")
    print()


row_range = ws[2:ws.max_row]
for rows in row_range:
    for cell in rows:
        #print(cell.value, end=" ")
        #print(cell.coordinate, end=" ")
        xy = coordinate_from_string(cell.coordinate)
        #print(xy, end=" ")
        print(xy[0], end="")
        print(xy[1], end=" ")
    print()
'''

# print(tuple(ws.rows))
# for row in tuple(ws.rows):
#    print(row[1].value)

# print(tuple(ws.columns))

for row in ws.iter_rows(min_row=1, max_row=5, min_col=2, max_col=3):  # 범위지정
    print(row[0].value, row[1].value)


wb.save("sample.xlsx")
