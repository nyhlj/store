dict={"k1":"v1","k2":"v2","k3":"v3"}
for a,b in dict.items():
    print(a)#循环遍历出所有的key
    print(b)#循环遍历出所有的value
print(dict)
dict["k4"]="v4"
print(dict)#在字典中增加键值对