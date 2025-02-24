n = int(input())

library = {}
for i in range(n):
    k, book = input().split()
    k = int(k)
    if k == 2:
        if book in library:
            library[book] += 1
        else:
            library[book] = 1
    elif k == 1:
        if library.get(book, 0) == 0:
            print("NO")
        elif library.get(book, 0) > 0:
            print("YES")
            library[book] -= 1