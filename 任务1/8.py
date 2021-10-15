N = int(input("您想计算多少"))
for i in range(1, N+1):
    for j in range(1, i+1):
        print("{}*{}={}".format(i, j, i*j), end='\t')
    print('')
