n = int(input())
mystr = input()
robot_dict = {"R":0, "O":0, "B":0, "T":0} 

def isrobot():
    if robot_dict["R"]>0 and robot_dict["O"]>1 and robot_dict["B"]>0 and robot_dict["T"]>0: return True
    else: return False

substr_len = float("inf")
left = right = 0

#* RRlOOBBTTr
while right < n or isrobot():
    if not isrobot():
        robot_dict[mystr[right]] += 1
        right += 1
    elif isrobot():
        substr_len = min(substr_len, right-left)
        robot_dict[mystr[left]] -= 1
        left += 1

print(substr_len) if substr_len != float("inf") else print(-1)

