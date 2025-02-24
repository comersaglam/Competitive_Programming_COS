n = int(input())
password = list(input())

start = 0
end = n - 1

while start < end:
    if password[start] == password[end] and password[start] != '#':
        start += 1
        end -= 1
    elif password[start] == password[end] == '#':
        print(-1)
        break
    elif password[start] == '#':
        password[start] = password[end]
        start += 1
        end -= 1
    elif password[end] == '#':
        password[end] = password[start]
        start += 1
        end -= 1
    
    else:
        print(-1)
        break
else:
    if n % 2 == 1 and password[n // 2] == '#':
        print(-1)
    else:
        print(''.join(password))