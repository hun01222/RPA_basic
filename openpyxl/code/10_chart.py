from openpyxl.chart import BarChart, Reference
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
bar_chart = BarChart()
bar_chart.add_data(bar_value, titles_from_data=True)  # 제목에서 가져옴
bar_chart.title = "성적표"
bar_chart.style = 20  # 미리 정해진 스타일 사용
bar_chart.y_axis.title = "점수"
bar_chart.x_axis.title = "번호"

ws.add_chart(bar_chart, "E1")

wb.save("sample_chart.xlsx")

# openpyxl 홈페이지 참조.
