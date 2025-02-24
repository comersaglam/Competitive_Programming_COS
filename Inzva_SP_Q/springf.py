n = int(input())
enjoy = list(map(int, input().split()))
modulo = 10**9 + 7
mean = sum(enjoy) / n

count = 1
llist = [enjoy[0]]
rlist = [enjoy[0]]
if enjoy[0] < mean:
    ismall = 1
    isbig = 0
elif enjoy[0] > mean: 
    ismall = 0
    isbig = 1
elif enjoy[0] == mean:
    ismall = 0
    isbig = 0

for book in enjoy[1:]:
    if book > mean:
        if ismall == 1:
            llist.append(book)
        elif ismall == 0:
            count = count * 2 % modulo
            if book > llist[-1]:
                llist.append(book)
            else: rlist.append(book)
        isbig = 1

    elif book < mean:
        if isbig == 1:
            rlist.append(book)
        elif isbig == 0:
            count = count * 2 % modulo
            if book > llist[-1]:
                llist.append(book) 
            else:
                rlist.append(book)
        ismall = 1
    
    elif book == mean:
        count = count * 2 % modulo
        if book >  llist[-1]:
            llist.append(book)
        else:
            rlist.append(book)


print(count % modulo)
llist.reverse()
print(*llist, *rlist[1:])
