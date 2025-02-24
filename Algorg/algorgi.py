n = int(input())
capthca = input()

robotstr = {"R":0, "O":0, "B":0, "T":0}
def ismeet():
    if robotstr["R"] >= 1 and robotstr["O"] >= 2 and robotstr["B"] >= 1 and robotstr["T"] >= 1:
        return True
    else: return False

left, right = 0,0
minrobot = float("inf")
while right <= n:
    if ismeet():
        minrobot = min(minrobot, right-left)
        robotstr[capthca[left]] -= 1
        left += 1
    else:
        if right == n: break
        robotstr[capthca[right]] += 1
        right += 1

if minrobot != float("inf"):
    print(minrobot)
else: print(-1)