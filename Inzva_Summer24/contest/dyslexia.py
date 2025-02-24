num, mod = list(map(int, input().split()))
nums = []
while num > 0:
    nums.append(num%10)
    num = num // 10
n = len(nums)


    