for i in range(-9,0):
    for j in range(1,10):
         if(j==i*(-1)):
             print(j,"*",i*(-1),"=",i*j*(-1))
             break
         else:
             if(i*j*(-1)>9):
                 print(j,"*",i*(-1),"=",i*j*(-1),end="  ")
             else:
                 print(j,"*",i*(-1),"=",i*j*(-1),end="   ")