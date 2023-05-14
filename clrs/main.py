from leetcode.T1054 import Solution


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution
    lt = [3, 3, 1, 1, 1, 1, 2, 2, 2]
    ret = sol.dfs(sol, 0, lt)
    print(lt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
