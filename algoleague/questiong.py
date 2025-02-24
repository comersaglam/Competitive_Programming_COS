# Practice makes it perfect
# inzva community built algoleague for every algorithm enthusiast hungry 
# for self-improvement and friendly competition. Have fun and good luck!
from collections import deque

n = int(input())
maxids= list(map(int,input().split()))


def lex_max_list(n, max_id_list):
    lexico_max_list = []
    used_ids_max = set()
    available_ids_max = sorted(range(1, n + 1), reverse=True)

    for max_id in max_id_list:
        if max_id not in used_ids_max:
            lexico_max_list.append(max_id)
            used_ids_max.add(max_id)
            available_ids_max.remove(max_id)
        else:
            for i in available_ids_max:
                if i not in used_ids_max and i < max_id:
                    lexico_max_list.append(i)
                    used_ids_max.add(i)
                    available_ids_max.remove(i)
                    break
    
    return lexico_max_list


def lex_min_list(n, max_id_list):
    lexico_min_list = []
    used_ids_min = set()
    available_ids_min = sorted(range(1, n + 1))

    for max_id in max_id_list:
        if max_id not in used_ids_min:
            lexico_min_list.append(max_id)
            used_ids_min.add(max_id)
            available_ids_min.remove(max_id)
        else:
            for i in available_ids_min:
                if i not in used_ids_min:
                    lexico_min_list.append(i)
                    used_ids_min.add(i)
                    available_ids_min.remove(i)
                    break

    return lexico_min_list

print(*lex_min_list(n, maxids))
print(*lex_max_list(n, maxids))