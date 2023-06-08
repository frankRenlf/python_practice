from leetcode.T2352 import Solution
from algorithms.sort import Sorts
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test(arr):
    arr[0] = 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    arr1 = np.array([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
    arr = [1, 2]
    ret = np.linalg.norm(arr)
    randidx = np.random.permutation(arr1.shape[0])
    print(randidx)
    # Take the first K examples as centroids
    centroids = arr1[randidx[:2]]
    print(centroids)
    # st = Sorts()
    # arr = [7, 2, 1, 3, 11, 2, 10, 4, 5, 19]
    # st.quick(arr)
    # print(arr)
