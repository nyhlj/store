A=56
B=78
while True:
    num=input("请输入")
    if num=="+" or num=="-":
        A = A + B
        B = A - B
        A = A - B
    else:
        break

    print("A等于",A,"B等于",B)