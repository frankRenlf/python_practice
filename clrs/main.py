from leetcode.T2465 import Solution
from algorithms.sort import Sorts


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test(arr):
    arr[0] = 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    ret = sol.distinctAverages([4, 1, 4, 0, 3, 5])
    print(ret)

    # st = Sorts()
    # arr = [7, 2, 1, 3, 11, 2, 10, 4, 5, 19]
    # st.quick(arr)
    # print(arr)
