'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体

'''

class cup:
    height = 0
    volume = 0
    colour = ""
    material = ""

    def run(self):
        print(self.height ,self.volume,self.colour,self.material)

c = cup()
c.height = 10
c.volume = 20
c.colour = "黑色"
c.material = "玻璃"
c.run()

'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''
class computer:
    size = 0
    price = 0
    cpu = ""
    ram = 0
    standbytime = ""

    def type(self,type):
        print(self.cpu,"可以打字",type)
    def game(self,game):
        print(self.cpu,"可以玩",game )
    def video(self,video):
        print(self.cpu,"可以看",video)

c = computer()
c.size = 16
c.price = 6000
c.cpu = "inter i10"
c.ram = 100000
c.standbytime = "24小时"

c.type("精忠报国")
c.game("原神")
c.video("英雄联盟赛事直播")








