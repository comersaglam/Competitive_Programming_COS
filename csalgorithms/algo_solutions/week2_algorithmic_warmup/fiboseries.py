a = 1
b = 1
i = 1
sum = 0
kalan = 0
mylist =[1,1]
while True:
    i += 1
    if kalan == 0:
            
        a, b = b, int((a+b)%10)
        if i%10 ==0:
            mylist.append(b)
            i = 1
        else:
            mylist.append(b)
        if b == 1:
            kalan = 1
    if kalan == 1:
        a, b = b, (a+b)%10
        if i%10 ==0:
            mylist.append(b)
            i = 1
        else:
            mylist.append(b)
        if b == 1:
            break
        else:
            kalan = 0
mylist.pop(-1)
mylist.pop(-1)
print(mylist)
sum1 = 0
for i in mylist:
    sum1 += i*i
print(sum1)        
