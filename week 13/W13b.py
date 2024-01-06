from openpyxl import load_workbook

# Load the workbook from an Excel file
wb = load_workbook("./week 13/student_list.xlsx")

ws1 = wb.active
# Get the reference of the active (first) worksheet

# Get the entire column (Column A)
col = ws1["A"]
for cell in col:
    print(cell.value)

print('----------------------------------')
# Get the entire row (Row 1)
row = ws1["1"]
for cell in row:
    print(cell.value)
