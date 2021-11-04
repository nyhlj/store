from threading import Thread
import time

basket = 0
money = 3000
inmoney = 0
class outperson(Thread):
    outname = ""
    outcount = 0
    def run(self) -> None:
        global basket
        global inmoney
        while True:
            if basket<500:
                self.outcount = self.outcount + 1
                basket = basket + 1
                inmoney = inmoney + 3
                print(self.outname,"制作了", self.outcount,"还有",basket)
            elif basket == 500:
                time.sleep(3)
            else:
                print(self.outname,"赚了",inmoney*12)
                break



class inperson(Thread):
    inname = ""
    incount = 0

    def run(self) -> None:
        global basket
        global money
        while True:
            if money > 0:
                if basket > 0:
                    self.incount = self.incount + 1
                    basket = basket - 1
                    money = money - 3
                    print(self.inname,"购买了",self.incount,"还有",basket,"还有",money,"钱")
                elif basket ==0:
                    time.sleep(3)
            else:
                break




o1 = outperson()
o2 = outperson()
o3 = outperson()

i1 = inperson()
i2 = inperson()
i3 = inperson()
i4 = inperson()
i5 = inperson()
i6 = inperson()

o1.outname = "张三"
o2.outname = "李四"
o3.outname = "王五"

i1.inname = "赵云"
i2.inname = "关羽"
i3.inname = "张飞"
i4.inname = "刘备"
i5.inname = "曹操"
i6.inname = "吕布"

o1.start()
o2.start()
o3.start()

i1.start()
i2.start()
i3.start()
i4.start()
i5.start()
i6.start()






















































