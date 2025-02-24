#include <iostream>
#include <vector>
#include <stack>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::stack<std::pair<int, int>> stack; // will hold pairs of (value, number of times value has been seen)

    for (int i = 0; i < n; ++i) {
        int ele = arr[i];
        if (stack.empty()) {
            stack.push({ele, 1});
        } else if (ele == stack.top().first) {
            stack.top().second += 1;
        } else {
            stack.push({ele, 1});
        }
        if (stack.top().second == stack.top().first) {
            stack.pop();
        }
    }

    int cnt = 0;
    while (!stack.empty()) {
        cnt += stack.top().second;
        stack.pop();
    }
    std::cout << cnt << std::endl;

    return 0;
}