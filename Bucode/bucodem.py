n = int(input())
n1, n2, n3, n4 = 4,3,2,1

def german_f_list(n, n1, n2, n3, n4):
    modulo = 10**9 + 7
    curr_n = 2
    if n == 1:
        return 9
    while curr_n < n:
        curr_n += 1
        n1, n2 ,n3, n4 = (n1+n2+n3+n4) % modulo, (n1+n2+n3) % modulo, (n1+n2) % modulo, n1 % modulo
    return (2*(n1+n2+n3+n4)) % modulo

print(german_f_list(n, n1, n2, n3, n4))