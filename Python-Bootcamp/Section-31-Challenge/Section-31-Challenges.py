# Challenge 1
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
rows = (
    ('Year', 'Sales'),
    (2017, 150000),
    (2018, 180000),
    (2019, 210000),
    (2020, 125000)
)
for r in rows:
    sheet.append(r)
# =====================================================================================================================
# Challenge 2
sheet = wb.active
sheet.title = 'COMPANY SALES'
# =====================================================================================================================
# Challenge 3
# =====================================================================================================================
# Challenge 4
# =====================================================================================================================
# Challenge 5
# =====================================================================================================================
# Challenge 6
# =====================================================================================================================
# Challenge 7
# =====================================================================================================================
# Challenge 8



wb.save('sales.xlsx')