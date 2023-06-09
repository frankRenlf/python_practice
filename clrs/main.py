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
    print("-----")
    # st = Sorts()
    print(arr1)
    print("-----")

    arr1[:,0]=np.log2(arr1[:,0])

    print(arr1)
    # st.quick(arr)
    # print(arr)
