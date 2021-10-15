names = [
    ["曹操",56,"男",106,"IBM", 500 ,50],
    ["大乔",19,"女",230,"微软", 501 ,60],
    ["小乔", 19, "女", 210, "Oracle", 600, 60],
    ["许褚", 45, "男", 230, "Tencent", 700 , 10]]
num=0
num1=0
nan=0
nv=0
xin=0
nian=0
names.append(["刘备", 45, "男", 220, "alibaba", 500, 30])
for i in range(len(names)):
    for j in range(7):
        if j == 5:
            num += names[i][j]
            xin = num / len(names)
        if j==1:
            names[i][j] = int(names[i][j])
            num1 += names[i][j]
            nian=num1/len(names)

        if j == 2:
            if names[i][j] == "男":
                nan+= 1
            if names[i][j] == "女":
                nv+= 1
print("平均工资是：",xin)
print("平均年龄是",nian)
print("添加新成员后：")
for x in names:
    print(x,end='\n')
print("男人数：",nan,"女人数:",nv)

