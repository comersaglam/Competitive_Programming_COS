from itertools import combinations

def can_pay_salaries(employees, stacks, stack_combinations):
    if not employees:
        return True  # All salaries have been matched

    salary = employees[0]
    for comb, total in stack_combinations.items():
        if total == salary:
            # Try this combination
            new_stacks = stacks.copy()
            for s in comb:
                new_stacks.remove(s)

            new_combinations = {k: v for k, v in stack_combinations.items() if not any(c in comb for c in k)}
            # Check if rest of the salaries can be paid
            if can_pay_salaries(employees[1:], new_stacks, new_combinations):
                return True

    return False

def main():
    Q = int(input())
    for _ in range(Q):
        N, M = map(int, input().split())
        employees = list(map(int, input().split()))
        stacks = list(map(int, input().split()))

        employees.sort(reverse=True)
        stack_combinations = {(): 0}
        for r in range(1, len(stacks) + 1):
            for comb in combinations(stacks, r):
                stack_combinations[comb] = sum(comb)

        result = "YES" if can_pay_salaries(employees, stacks, stack_combinations) else "NO"
        print(result)

if __name__ == "__main__":
    main()
