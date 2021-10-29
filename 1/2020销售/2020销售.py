import xlrd
from dbutils import *
wb = xlrd.open_workbook(filename=r"C:\Users\29406\Desktop\1\2020年每个月的销售情况.xlsx")

nsheet = wb.nsheets

for i in range(nsheet): # 遍历每个选项卡
    st = wb.sheet_by_index(i) # 获取第n个选项卡
    nrow = st.nrows # 获取有多少行
    for j in range(1,nrow): # 遍历选项卡每一行
        cell = st.row_values(j) # 获取第j行
        sql = "insert into sell value (%s,%s,%s,%s,%s)"
        param = [cell[0],cell[1],cell[2],cell[3],cell[4]]
        update(sql,param)









