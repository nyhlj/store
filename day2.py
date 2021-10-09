import random
import time
jinbi=5000
cishu=15
cai=3
randint = random.randint(1, 30)  # 随机产生的数字
while True:
    if jinbi==0:
        break
    if cishu==0:
        break
    if cai ==0:
        time.sleep(10)
        cai+=3
    print(randint)
    num=input("请输入一个数字")
    if num.isdigit():
        num=int(num)
        if num == randint:
            jinbi+=3000
            cai-=1
            print("恭喜猜对了，获得3000金币，还有",jinbi,"金币, 还剩{0}次".format(str(cishu - 0)))
        elif num >randint:
            jinbi -= 500
            cishu -= 1
            cai-=1
            print("猜大了，扣除500金币，还有",jinbi,"金币, 还剩{0}次".format(str(cishu - 0)))
        elif num <randint:
            jinbi -= 500
            cishu -= 1
            cai-=1
            print("猜小了，扣除500金币，还有",jinbi,"金币, 还剩{0}次".format(str(cishu - 0)))
    else:
        jinbi -= 500
        cishu -= 1
        cai-=1
        print("别瞎输入,扣除500金币，还有",jinbi,"金币, 还剩{0}次".format(str(cishu - 0)))





