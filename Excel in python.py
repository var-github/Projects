import xlrd
# remember to save file as xls not xlsx, save as 97 workbook
# we can set a variable with the location of the file so we can use the variable whenever we need
loc = ("E:\\Varun\\Python\\Python programs\\Book1.xls")

# we set the opened workbook into a variable
exel = xlrd.open_workbook(loc)
# now mention which sheet
sheet = exel.sheet_by_index(0)
# or sheet = exel.sheet_by_name("Sheet1")

# to find a specific cells value
print(sheet.cell_value(0, 0))

# to find number of rows and columns
print(sheet.ncols)
print(sheet.nrows)

# print everthing in row 1
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

# use inbuilt feature
print(sheet.row_values(1))
# will print all row values in row 1
print(sheet.col_values(1))

