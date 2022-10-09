calc=int(input("請輸入正整數:"))
data=str()
result=int(0)
for i in range(1,calc+1):
    res = calc % i
    if res == 0 :
        data=data+" "+str(i)
        result+=1
print(str(calc)+" 的因數有"+ data)
if result > 2:
    print(str(calc)+" 不是質數")
else:
    print(str(calc)+" 是質數")   
