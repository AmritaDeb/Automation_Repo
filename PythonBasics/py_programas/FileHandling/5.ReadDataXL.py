import xlrd

workbook = xlrd.open_workbook("actiTimeLoginTC.xlsx")
worksheet = workbook.sheet_by_name("Login")
print(worksheet.cell(0,1).value)

print(xlrd.open_workbook("actiTimeLoginTC.xlsx").sheet_by_name("Login").cell(0,2).value)

row = []
col = []

