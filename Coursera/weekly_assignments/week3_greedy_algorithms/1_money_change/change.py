    #*
def change(money):
    x = 0
    x += money//5
    if x % 2 == 1:
        x = (x+1)/2
    else:
        x = x/2
    money = money%5
    x += money
    

    return int(x)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
