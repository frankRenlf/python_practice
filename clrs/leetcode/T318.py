# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/6 09:41 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description :
"""


class Solution:
    def maxProduct(self, words):
        max_prod = 0
        word_bits = {}  # Use a dictionary to map the bit representation to max word length

        for word in words:
            word_bit = 0
            for char in word:
                # Shift 1 left by the order of the character (a=0, b=1, c=2, ...)
                word_bit |= 1 << (ord(char) - ord('a'))
            # Keep the longest word for each unique bit representation
            word_bits[word_bit] = max(word_bits.get(word_bit, 0), len(word))

        # Compare each pair of bit representations
        for x in word_bits:
            for y in word_bits:
                if x & y == 0:  # No common characters
                    max_prod = max(max_prod, word_bits[x] * word_bits[y])

        return max_prod

# if __name__ == "__main__":
