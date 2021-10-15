def recursion(n):
    if n==1:
        return 1
    else:
        return  n*recursion(n-1)
sum=0
for i in range(1,21):
    sum+=recursion(i)
    print(i,'!=',sum)