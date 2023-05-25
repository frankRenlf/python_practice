from leetcode.T2451 import Solution
from sorts.merge import Merge


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sol = Solution()
    # ret = sol.oddString(["az", "za", "az"])
    # print(ret)
    merge1 = Merge([19, 2, 1, 3, 11, 2, 10, 4, 5, 19])
    ret = merge1.sort()
    print(ret)
