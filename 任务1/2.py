max_shu=float("-inf")
zo_shu=0
ping_shu=0
for i in range(10):
    number=float(input("请输入数:"))
    zo_shu += number
    ping_shu=zo_shu/10
    if number >max_shu:
        max_shu=number

print("最大数：",max_shu)
print("和：",zo_shu)
print("平均数;",ping_shu)
