
wk = open(file=r'C:\Users\29406\Desktop\day15【异常处理和文件读写】\任务\baidu_x_system.log', encoding='utf-8')
ManiData = ''
dataDic = {}
count = len(wk.readlines())
wk.seek(0)
for j in range(count):
    ManiData = ''
    buf1line = wk.readline()
    for i in buf1line:
        if i == ' ':
            break
        else:
            ManiData += i
    if ManiData not in dataDic:
        dataDic.update({ManiData: 1})
    elif ManiData in dataDic:
        dataDic[ManiData] += 1
print(dataDic)