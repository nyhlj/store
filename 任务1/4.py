a=int(input("输入第一条边:"))
b=int(input("输入第二条边:"))
c=int(input("输入第三条边:"))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
        print("这是等边三角形")
    elif (a==b or a==c or b==c):
        print("这是等腰三角形")
    elif (a**2+b**2==c**2) or (a**2+b**2==c**2) or (a**2+b**2==c**2):
        print("这是直角三角形")
    else:
        print("这是普通三角形")
else :
    print("这不是三角形")
