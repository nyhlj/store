'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import  random
#商品
shop=[
#     0      1
    ["刀🔪",999],#0
    ["斧子",200],#1
    ["👍",90000],#2
    ["coco",150],#3
    ["枸杞",900],#4
]
youhui=[
    ["9",10],
    ["5",5],
    ["1",2],
    ["0",1],
]
#初始化余额
money=random.randint(0,99999)
print(money)
#购物车
mycart=[]
#展示商品
while False==0:
    for index,value in enumerate(shop):
        print(index,":",value)
    chose=input("请输入商品编号")
    if chose.isdigit():#str判断引号内是否为数字
        chose=int(chose)#转换成整型
        you_huijuan = random.choice(youhui)
        print(you_huijuan)
        i=you_huijuan[0]
        # i=int(you_huijuan[0])
        print(i)
        if chose <len(shop):#判断输入的内容是否小于列表的长度
            if money>shop[chose][1]:#判断money是否大于商品的价格
                mycart.append(shop[chose])#把商品加入购物车
                money=money-shop[chose][1]#money减去商品的价格
                print("恭喜你成功加入购物车，您的余额为：",money)
            else:
                print("gun")
        else:
            print("没有此商品")
    elif chose=="q"or chose=="Q":
        print("=================")
        for index, value in enumerate(mycart):
            print(index, ":", value)
        print("您的余额为：",money)
        break
    else:
        print("别瞎弄")
