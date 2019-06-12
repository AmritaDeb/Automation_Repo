import xlsxwriter
import xlrd

# workbook = xlrd.open_workbook("actiTimeLoginTC.xlsx")
# worksheet = workbook.sheet_by_name("Login")
# print(username)

workbook = xlsxwriter.Workbook("new_data.xlsx")
worksheet = workbook.add_worksheet("Login")
credentials = (['UserName','Password'],['amy','@123'],['sid','@541'])
row = 0
col = 0
for un,pw in credentials:
    worksheet.write(row,col,un)
    worksheet.write(row,col+1,pw)
    row+=1
workbook.close()




