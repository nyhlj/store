from DBUtils import *

import random
from select import select
from turtle import update


# 银行库
bank = {}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
# 开户成功的信息模板
myinfo = '''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''

# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''


def print_welcome():
    print(welcome, end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i, bank_choice[i]))
    print("**********************************")


# 输入帮助方法：chose是打印选项
def inputHelp(chose, datatype="str"):
    while True:
        print("请输入", chose, ":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i


# 判断是否存在该银行选项
def isExists(chose, data):
    if chose in data:
        return True
    return False


# 获取随机码
def getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string


# 通过账号获取账户信息
def findByAccount(account):
    sql0 = "select * from user where account = %s"
    param0 = [account]
    data0 = select(sql0, param0)
    for i in account:
        if i == data0:
            return data0
    return None


# 银行的开户方法
def bank_addUser(username, password, country, province, street, door, money):
    # 查询是否已满
    sql = "select count(*) from user"
    param = []
    data = select(sql, param)
    if data >= 100:
        return 3
    # 查询是否存在
    sql1 = "select * from user where username  = %s"
    param1 = [username]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        return 2
    # 插入数据
    sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [getRandom(), username, password, country, province, street, door, money, "2021-10-29", bank_name]
    update(sql2, param2)
    return 1


# 银行的存钱方法
def bank_saveMoney(username, money):
    for i in bank.keys():
        # sql
        sql3 = "select * from user where username = %s"
        param3 = [username]
        data3 = select(sql3, param3)
        if len(data3) != 0:
            sql4 = "update user set money = money + %s"
            param4 = [money]
            update(sql4, param4)
            # if bank[i]["account"] == ac:
            #     print(bank[i]["money"])
            #     bank[i]["money"] += money
            return True
    return False


# 银行的查询功能
def bank_selectUser(account, password):
    uname = findByAccount(account)

    sql5 = "select * from user where uname = %s"
    param5 = [uname]
    data5 = select(sql5, param5)
    if len(data5) != 0:
        sql6 = "select param5 from user where password = %s"
        param6 = [password]
        data6 = select(sql6, param6)
        if data6 == param6:
            for i in uname:
                print(i)
        else:
            print("密码错误")
    else:
        print("账户不存在")

    # if uname != None and len(uname) != 0:
    #     if password == bank[uname]["password"]:
    #         user = bank[uname]
    #         print(myinfo.format(account=user["account"],
    #                         username=uname,
    #                         password=user["password"],
    #                         country=user["country"],
    #                         province=user["province"],
    #                         street=user["street"],
    #                         door=user["door"],
    #                         money=user["money"],
    #                         bank_name=user["bank_name"]
    #                         ))
    #     else:
    #         print("用户密码错误！")
    # else:
    #     print("该用户不存在！")


# 银行的取钱功能
def bank_takeMoney(account, password, money):
    uname = findByAccount(account)
    if uname != None:
        sql7 = "select * from user where password =%s"
        param7 = [password]
        data7 = (sql7, param7)
        if data7 == param7:
            sql8 = "select * from user where money = %s"
            param8 = [money]
            data8 = (sql8, param8)
            if data8 > money:
                sql9 = "uodate user set money = money - %s"
                param9 = [money]
                update(sql9,param9)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 0

    #     if bank[uname]["password"] == password:
    #         if bank[uname]["money"] < money:
    #             return 3
    #         else:
    #             bank[uname]["money"] -= money
    #             return 0
    #     else:
    #         return 2
    # else:
    #     return 0


# 银行的转账功能
def bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney):
    status = bank_takeMoney(outputaccount, outputpassword, outputmoney)

    sql10 = "select * from user where account = %s"
    param10 = [outputaccount]
    data10 = (sql10,param10)

    sql11 = "select * from user where password = $s"
    param11 = [outputpassword]
    data11 = (sql11,param11)

    sql12 = "select * from user where money = %s"
    param12 = [outputmoney]
    data12 = (sql12,param12)

    sql13 = "select * from user where account = %s"
    param13 = [inputaccount]
    data13 = (sql13,param13)
    if data10 == 1:
        return status
    elif data11 == 2:
        return status
    elif data12 == 3:
        return status

    if data13 != None and findByAccount(data13) != None:
        bank_saveMoney(inputaccount, outputmoney)
        return 0
    else:
        return 1


# 开户方法
def addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province = inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money = inputHelp("银行卡余额", "int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username, password, country, province, street, door, money)
    # 判断1   2   3
    if status == 1:
        user = bank[username]
        print("恭喜开户成功！以下是您的开户信息：")
        print(myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")


# 存钱
def saveMoney():
    account = inputHelp("账号")
    m = inputHelp("存入的金额", "int")

    flag = bank_saveMoney(account, m)

    if flag:
        print("存储成功!您的个人信息为：")
        uname = findByAccount(account)
        user = bank[uname]
        print(myinfo.format(account=user["account"],
                            username=uname,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")


# 取钱
def takeMoney():
    account = inputHelp("账户")
    password = inputHelp("密码")
    tmoney = inputHelp("取出金额", "int")

    f = bank_takeMoney(account, password, tmoney)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account, password)


# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass = inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额", "int")

    f = bank_transformMoney(output, input, outputpass, outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output, outputpass)


# 查询账户方法
def selectUser():
    account = inputHelp("账号")
    password = inputHelp("密码")

    bank_selectUser(account, password)


# 核心程序
while True:

    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose, bank_choice):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")
