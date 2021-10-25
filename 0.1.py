import xlrd

wb = xlrd.open_workbook(filename=r"C:\Users\29406\Desktop\day07【excel表读写】\任务\2020年每个月的销售情况.xlsx",encoding_override=True)


def SaleMoneyAYear():
    # =======================================
    # 年销售额
    sum1 = 0
    sum2 = 0
    for i in range(12):
        ts = wb.sheet_by_index(i)
        for j in range(1, ts.nrows):
            getTR = ts.row_values(j)
            money1 = getTR[2] * getTR[4]
            sum1 += money1
        sum2 += sum1
    print("年销售额：{:.2f}".format(sum2))


def Clothes_ProportionOfSaleNumsYear():
    # ======================================
    # 衣服的总销售量（件数）
    sum4 = 0
    for i in range(12):
        ts = wb.sheet_by_index(i)
        sum3 = 0
        for j in range(1, ts.nrows):
            getTR = ts.row_values(j)
            sum3 += int(getTR[4])
        sum4 += sum3
    print(sum4)
    # 遍历并展示所有衣服销售件数占比
    # 遍历并展示所有衣服销售总件数（全年）
    clothesShow = {}
    for i in range(12):
        csn = wb.sheet_by_index(i)
        for j in range(1, csn.nrows):
            getCR = csn.row_values(j)
            if getCR[1] not in clothesShow:
                clothesShow.update({getCR[1]: int(getCR[4])})
            elif getCR[1] in clothesShow:
                clothesShow[getCR[1]] += int(getCR[4])
    # 全服装名称列表
    clslist = []
    for i in range(12):
        csn = wb.sheet_by_index(i)
        for j in range(1, csn.nrows):
            getCR = csn.row_values(j)
            if getCR[1] not in clslist:
                clslist.append(getCR[1])
            else:
                pass
    # 占比，重新赋值字典值
    for j in clslist:
        clothesShow[j] = (clothesShow[j] / sum4) * 100
    print('每种衣服的销售（件数）占比：', clothesShow)


def Clothes_ProportionOfSaleNumsMonth():
    # =====================================
    # 每件衣服的月销售件数
    for i in range(12):
        ts = wb.sheet_by_index(i)
        monthSale = {}
        sum5 = 0
        for j in range(1, ts.nrows):
            getTR = ts.row_values(j)
            sum5 += getTR[4]
            if getTR[1] not in monthSale:
                monthSale.update({getTR[1]: getTR[4]})
            elif getTR[1] in monthSale:
                monthSale[getTR[1]] += getTR[4]
        for x in monthSale:
            monthSale[x] = round((monthSale[x] / sum5) * 100, 2)
        print(ts, "月销售件数占比（%）:", monthSale)


def Clothes_ProportionOfSaleMoneyMonth():
    # ================================
    # 每件衣服的销售额占比(年)
    YearSale = {}
    sum5 = 0
    for i in range(12):
        ts = wb.sheet_by_index(i)
        for j in range(1, ts.nrows):
            getTR = ts.row_values(j)
            sum5 += (getTR[2] * getTR[4])
            if getTR[1] not in YearSale:
                YearSale.update({getTR[1]: getTR[2] * getTR[4]})
            elif getTR[1] in YearSale:
                YearSale[getTR[1]] += (getTR[2] * getTR[4])
    for x in YearSale:
        YearSale[x] = round((YearSale[x] / sum5) * 100, 2)
    print("销售额占比（%）:", YearSale)


# 最畅销的衣服
def MostPopularClothes():
    clothesShow = {}
    for i in range(12):
        csn = wb.sheet_by_index(i)
        for j in range(1, csn.nrows):
            getCR = csn.row_values(j)
            if getCR[1] not in clothesShow:
                clothesShow.update({getCR[1]: int(getCR[4])})
            elif getCR[1] in clothesShow:
                clothesShow[getCR[1]] += int(getCR[4])
    compareNum = 0
    MemStr = ''
    for j in clothesShow:
        if clothesShow[j] > compareNum:
            compareNum = clothesShow[j]
            MemStr = j
        else:
            pass
    print("最畅销的衣服是：", MemStr, "，共售出", int(compareNum), "件")


# 最不畅销的衣服（全年）
def MostNotPopularClothes():
    clothesShow = {}
    for i in range(12):
        csn = wb.sheet_by_index(i)
        for j in range(1, csn.nrows):
            getCR = csn.row_values(j)
            if getCR[1] not in clothesShow:
                clothesShow.update({getCR[1]: int(getCR[4])})
            elif getCR[1] in clothesShow:
                clothesShow[getCR[1]] += int(getCR[4])
    compareNum2 = 9999
    MemStr = ''
    for j in clothesShow:
        if clothesShow[j] < compareNum2:
            compareNum2 = clothesShow[j]
            MemStr = j
        else:
            pass
    print("最不畅销的（全年销售最低的）衣服是：", MemStr, "，共售出", int(compareNum2), "件")


# 每个季度最畅销的衣服
def PopularClothesPerQuarter():
    for i in range(1, 8, 3):
        clothesShow = {}
        for j in range(i, i+3):
            ts = wb.sheet_by_index(j)
            for x in range(1, ts.nrows):
                getTSR = ts.row_values(x)
                if getTSR[1] not in clothesShow:
                    clothesShow.update({getTSR[1]: int(getTSR[4])})
                elif getTSR[1] in clothesShow:
                    clothesShow[getTSR[1]] += int(getTSR[4])
        compareNum4 = 0
        TheClothesName = ''
        for y in clothesShow:
            if clothesShow[y] > compareNum4:
                compareNum4 = clothesShow[y]
                TheClothesName = y
            else:
                pass
        if i == 1:
            print('春季最畅销的衣服是：', TheClothesName, '共售出', compareNum4, '件')
        elif i == 4:
            print('夏季最畅销的衣服是：', TheClothesName, '共售出', compareNum4, '件')
        elif i == 7:
            print('秋季最畅销的衣服是：', TheClothesName, '共售出', compareNum4, '件')
    c1 = {}
    ts = wb.sheet_by_index(0)
    for z in range(1, ts.nrows):
        getTSR2 = ts.row_values(z)
        if getTSR2[1] not in c1:
            c1.update({getTSR2[1]: int(getTSR2[4])})
        elif getTSR2[1] in c1:
            c1[getTSR2[1]] += getTSR2[4]
    ts = wb.sheet_by_index(10)
    for r in range(1, ts.nrows):
        getTSR2 = ts.row_values(r)
        if getTSR2[1] not in c1:
            c1.update({getTSR2[1]: int(getTSR2[4])})
        elif getTSR2[1] in c1:
            c1[getTSR2[1]] += int(getTSR2[4])
    ts = wb.sheet_by_index(11)
    for o in range(1, ts.nrows):
        getTSR2 = ts.row_values(o)
        if getTSR2[1] not in c1:
            c1.update({getTSR2[1]: int(getTSR2[4])})
        elif getTSR2[1] in c1:
            c1[getTSR2[1]] += int(getTSR2[4])
    compareNum5 = 0
    TheClothesName = ''
    for y in c1:
        if c1[y] > compareNum5:
            compareNum5 = c1[y]
            TheClothesName = y
        else:
            pass
    print('冬季最畅销的衣服是：', TheClothesName, '共售出', int(compareNum5), '件')



while True:
    print('请输入对应服务的服务数字：')
    getInp = input()
    if getInp == '1':
        SaleMoneyAYear()
    elif getInp == '2':
        Clothes_ProportionOfSaleNumsYear()
    elif getInp == '3':
        Clothes_ProportionOfSaleNumsMonth()
    elif getInp == '4':
        Clothes_ProportionOfSaleMoneyMonth()
    elif getInp == '5':
        MostPopularClothes()
    elif getInp == '6':
        MostNotPopularClothes()
    elif getInp == '7':
        PopularClothesPerQuarter()
    elif getInp == 'q':
        print('结束，欢迎使用:)')
        break