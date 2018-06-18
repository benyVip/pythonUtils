#coding=utf-8
import openpyxl
import re

wb = openpyxl.load_workbook('/Users/linyoujie/Downloads/1.xlsx')
sheet = wb['sheel']

i = 15000;
for i in range(2,1500):
    num = 'B' + str(i)
    s = sheet[num].value
    filtrate = re.compile(u'[0-9_]')
    v = filtrate.sub(r'',s)
    print v



# workbook = load_workbook('/Users/linyoujie/Downloads/1.xlsx')
# sheets = workbook.get_sheet_names()         #从名称获取sheet

# print sheets
# booksheet = workbook.get_sheet_by_name(sheets[0])
#
# rows = booksheet.rows
# columns = booksheet.columns
#
# print rows
